from django.contrib import admin
from django.urls import path,include

from . import views

urlpatterns = [
    path('',views.Home_page),
    path('all_analytics',views.all_analytics),
    path('analytics/<slug:short_url>',views.analytics),
    path('<slug:short_url>',views.redirect_url)
]
