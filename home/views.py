from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(requesst):
    context = {"text": "First"}
    return render(requesst, "index.html", context=context)
