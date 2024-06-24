from django.urls import path, include
from . import views

app_name = 'trassir'
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),\
    path("<int:nvr_id>/get_health/", views.get_health, name="get_health"),

]
