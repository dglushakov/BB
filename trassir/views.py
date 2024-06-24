import datetime

from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import NVR, Health
import json


# Create your views here.

class IndexView(generic.ListView):
    model = NVR


class DetailView(generic.DetailView):
    model = NVR


def get_health(request, nvr_id):
    health = Health(server=NVR.objects.get(pk=nvr_id))
    health.health = json.dumps(NVR.objects.get(pk=nvr_id).get_health())
    health.collected_at = datetime.datetime.now()
    health.save()

    return HttpResponseRedirect(reverse("trassir:index"))
