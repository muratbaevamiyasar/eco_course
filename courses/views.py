from django.shortcuts import render
from .models import Lecture, Practice, Resource


def home(request):

    return render(request,"home.html")


def lectures(request):

    lectures = Lecture.objects.all()

    return render(request,"lectures.html",{"lectures":lectures})


def practice(request):

    practice = Practice.objects.all()

    return render(request,"practice.html",{"practice":practice})


def resources(request):

    resources = Resource.objects.all()

    return render(request,"resources.html",{"resources":resources})