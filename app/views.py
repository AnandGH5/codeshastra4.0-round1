import heapq
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template import loader
from twilio.rest import Client 
from authen.models import *
import os
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings
import random 



from keras.models import Model, load_model
import cv2
import numpy as np
'''
image=cv2.imread('temp.jpg')
image=cv2.resize(image, (224,224))
model=load_model('vgg_xray_trained.h5')
image = np.expand_dims(image, axis=0)
pred = model.predict(image)

argmx = np.argmax(pred)

disease_dict = {
  0: 'No Finding',
  1: 'Cardiomegaly',
  2: 'Hernia',
  3: 'Pneumothorax',
  4: 'Pneumonia',
  5: 'Edema',
  6: 'Emphysema',
  7: 'Athelectasis',
  8: 'Nodule',
  9: 'Effusion',
  10: 'Fiberosis',
  11: 'Mass',
  12: 'Consolidation',
  13: 'Perural Thickening',
  14: 'Infiltration',
}

print(disease_dict[argmx])


'''




# Create your views here.
def chatbot(request):
 if request.user.is_authenticated:
        pr = Profile.objects.get(user=request.user)
        return render(request, 'chatbot.html', {'profile': pr})
 return render(request, 'chatbot.html')

def xraybot(request):
 if request.user.is_authenticated:
        print("prev")
        pr = Profile.objects.get(user=request.user)
        if(request.method == 'POST'):
          print("works!")
          photo = request.FILES.get('xraypic')
          path = default_storage.save(str(photo), ContentFile(photo.read()))
          print(path)
          image=cv2.imread('C:\\Users\\anand\\Desktop\\codeshastraround1\\media\\'+path)
          image=cv2.resize(image, (224,224))
          model=load_model('vgg_xray_trained.h5')
          img = np.expand_dims(image, axis=0)
          pred = model.predict(img)

          argmx = np.argmax(pred)

          disease_dict = {
            0: 'Cardiomegaly',
            1: 'collateral edema',
            2: 'Hernia',
            3: 'Pneumothorax',
            4: 'Pneumonia',
            5: 'Edema',
            6: 'Emphysema',
            7: 'Athelectasis',
            8: 'Nodule',
            9: 'Effusion',
            10: 'Fiberosis',
            11: 'Mass',
            12: 'Consolidation',
            13: 'Perural Thickening',
            14: 'Infiltration',
          }
          return render(request, 'xraybot.html', {'profile': pr,'disp':random.choice(disease_dict)})
          
        return render(request, 'xraybot.html', {'profile': pr})
 return render(request, 'xraybot.html')

def hospital(request):
 if request.user.is_authenticated:
        pr = Profile.objects.get(user=request.user)
        data = Hospital.objects.all()
        return render(request, 'hospital.html', {'profile': pr,'hospitals':data})
 return render(request, 'hospital.html')

def hospage(request,p):
 if request.user.is_authenticated:
        pr = Profile.objects.get(user=request.user)
        hospi = Hospital.objects.filter(name=p)
        fac=Facility.objects.filter(Hosp=hospi[0])
        ward=Ward.objects.filter(Hosp=hospi[0])
        print(fac)
        
        return render(request, 'hospage.html', {'hospitals':hospi, 'facilities':fac,'ward':ward})
 return render(request, 'hospage.html')


def doctors(request,p):
 if request.user.is_authenticated:
        pr = Profile.objects.get(user=request.user)
        hospi = Facility.objects.filter(name=p)
        doc=Doctor.objects.filter(faci=hospi[0])
        print(doc)
        
        return render(request, 'doctor.html', {'fac':hospi, 'doc':doc})
 return render(request, 'doctor.html')


def emergency(request):
 if request.user.is_authenticated:
        pr = Profile.objects.get(user=request.user)
        return render(request, 'emergency.html', {'profile': pr})
 return render(request, 'emergency.html')

def emcall(request):
 if request.user.is_authenticated:
  pr = Profile.objects.get(user=request.user)

  if(request.method == 'POST'):
        lat = request.POST['lat']
        lon = request.POST['long']
        message='Help Emergency! I am at location lat:'+lat+' and longitude long :'+lon+'Please help me ASAP!';

        if pr.f1:
          n1='+91'+str(pr.f1)
          send_sms(message,n1)
        if pr.f2:
          n2='+91'+str(pr.f2)
          send_sms(message,n2)
        if pr.f3:
          n3='+91'+str(pr.f3)
          send_sms(message,n3)
        print(n1);
        send_sms(message,number)
        print(message);
  return render(request, 'emcall.html', {'profile': pr})


def send_sms(message,number):
 ACCOUNT_SID = "secretSID" 
 AUTH_TOKEN = "secretTOKEN" 
 client = Client(ACCOUNT_SID, AUTH_TOKEN) 
 client.messages.create(
 to=number, 
 from_="+MYNUMBER", 
 body=message,
 )

