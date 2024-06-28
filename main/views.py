from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
# Create your views here.

def say_hello(request):
  return render(request, 'hello.html', {'date': datetime.today()})