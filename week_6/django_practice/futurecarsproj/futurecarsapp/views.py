from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Where we're going we don't need roads...")

def newmake(request):
    return HttpResponse("newmake")
def makeid(request, id):
    return HttpResponse("makeid")
def edit(request, id):
    return HttpResponse("edit")
def cars(request, id):
    return HttpResponse("cars")
def newcar(request, id):
    return HttpResponse("newcar")
def modelid(request, id, model_id):
    return HttpResponse("modelid")
def modeledit(request, id, model_id):
    return HttpResponse("modeledit")