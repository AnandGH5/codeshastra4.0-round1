from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from authen.models import *
def home(request):
 if request.user.is_authenticated:
        pr = Profile.objects.get(user=request.user)
        return render(request, 'mainhome.html', {'profile': pr})			
 return render(request, 'mainhome.html')

def aboutus(request):
 if request.user.is_authenticated:
        pr = Profile.objects.get(user=request.user)
        return render(request, 'about-us.html', {'profile': pr})
 return render(request, 'about-us.html')

def faq(request):
 if request.user.is_authenticated:
        pr = Profile.objects.get(user=request.user)
        return render(request, 'faq.html', {'profile': pr})
 return render(request, 'faq.html')