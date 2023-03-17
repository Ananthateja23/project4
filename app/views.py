from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def rolex(request):
    return HttpResponse("Ava peruu dilli")
def avengers(request):
    return HttpResponse("<h1>Avengers Assemble to war</h1>")