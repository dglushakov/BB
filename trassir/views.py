from django.shortcuts import render
from django.views import generic

from .models import NVR


# Create your views here.

class IndexView(generic.ListView):
    model = NVR


class DetailView(generic.DetailView):
    model = NVR
