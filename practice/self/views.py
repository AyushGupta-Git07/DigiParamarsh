from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("kem choo")

def all_self(request):
    return render(request, 'self/all_self.html')

def order(request):
    return HttpResponse("This is the order page")