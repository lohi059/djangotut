from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request,'home/home.html')
def lohi(request):
    return HttpResponse('<h1>lohi</h1>')