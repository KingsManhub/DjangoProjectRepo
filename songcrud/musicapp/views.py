from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def hello(request):
    return HttpResponse("<h1> EasyGoingGuy(00): First Zuri Django Project </h1>")
