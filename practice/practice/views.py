from django.http import  HttpResponse
from django.shortcuts import render

def home(request):
   # return HttpResponse("Hello ji , Chai pee lo 10 rupay ki")
    return render(request,'index.html')

def shop(request):
    return HttpResponse("Aa gye muh uthake fir se paise hai tere pe Gareeb ")

def Contact(request):
    return HttpResponse("9192 baaki aap khud samajhdar ho")