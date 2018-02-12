from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.conf.urls import url
from app import views

urlpatterns = [
    url(r'^chatbot$', views.chatbot, name='chatbot'),    
    url(r'^xrayanalyzebot$', views.xraybot, name='xraybot'),    
    url(r'^hospital$', views.hospital, name='hospital'),
    url(r'^emergency$', views.emergency, name='emergency'), 
    url(r'^emcall$', views.emcall, name='emcall'), 
    url(r'hospital/(?P<p>[\w\-\_\ \,\.]+)/$', views.hospage,name='specifichosp'),
    url(r'hospital/fac/(?P<p>[\w\-\_\ \,\.]+)/$', views.doctors,name='doctors'),
]