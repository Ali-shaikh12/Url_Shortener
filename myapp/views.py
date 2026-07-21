import json
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from django.db import IntegrityError
from django.utils import timezone

from .models import LongToShort
# Create your views here.

def get_country(request):
	return request.META.get("HTTP_CF_IPCOUNTRY") or request.META.get("HTTP_X_COUNTRY") or "Unknown"


def get_device(request):
	user_agent = request.META.get("HTTP_USER_AGENT", "").lower()
	mobile_keywords = ["android", "iphone", "ipad", "mobile", "windows phone"]
	if any(keyword in user_agent for keyword in mobile_keywords):
		return "Mobile"
	return "Desktop"

def Home_page(request):
	context = { 
	"submitted" : False,
	"error" : False 
	}

	if request.method == "POST":
		data = request.POST 
		long_url = data.get('longurl', '').strip()
		custom_name = data.get('custom_name', '').strip()

		try:
			obj = LongToShort(long_url = long_url, short_url = custom_name) 
			obj.save()

			date = obj.date 
			clicks = obj.clicks

			context["long_url"] = long_url 
			context["short_url"] = request.build_absolute_uri(f"/{custom_name}")
			context["custom_name"] = custom_name
			context["date"] = date 
			context["clicks"] = clicks 
			context["submitted"] = True		  

		except IntegrityError: 
			context["error"] = True	

	return render(request,"index.html",context)


def redirect_url(request,short_url):
	obj = get_object_or_404(LongToShort, short_url = short_url)
	country = get_country(request)
	device = get_device(request)
	country_clicks = obj.country_clicks or {}

	obj.clicks = obj.clicks + 1
	country_clicks[country] = country_clicks.get(country, 0) + 1
	obj.country_clicks = country_clicks
	obj.last_country = country
	obj.last_device = device
	obj.last_clicked_at = timezone.now()

	if device == "Mobile":
		obj.mobile_clicks = obj.mobile_clicks + 1
	else:
		obj.desktop_clicks = obj.desktop_clicks + 1

	obj.save()

	return redirect(obj.long_url)

def all_analytics(request):
	rows = LongToShort.objects.all().order_by("-date")
	return render(request,"all_analytics.html", {"rows": rows})

def analytics(request, short_url):
	obj = get_object_or_404(LongToShort, short_url = short_url)
	country_clicks = obj.country_clicks or {}

	context = {
		"obj": obj,
		"short_url": request.build_absolute_uri(f"/{obj.short_url}"),
		"countries": json.dumps(list(country_clicks.keys())),
		"clicks": json.dumps(list(country_clicks.values())),
		"desktop": obj.desktop_clicks,
		"mobile": obj.mobile_clicks,
	}
	return render(request,"analytics.html", context)
