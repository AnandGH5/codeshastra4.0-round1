from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.http import HttpResponse, HttpResponseRedirect
from . import  views
from django.views.generic import RedirectView




urlpatterns = [
    url(r'^register/', views.register,name='register'),
    url(r'^login/', views.login,name='login'),
    url(r'^logout/', views.logout,name='logout'),
    # url(r'^dashboard/', views.dashboard),
    url(r'^forgotpassword/', views.forgotpassword,name='forgotpassword'),
    url(r'^(?P<p>[\w\-\_]+)/resetpassword/$',views.resetpassword, name='resetpassword'),
]
