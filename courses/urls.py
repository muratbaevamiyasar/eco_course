from django.urls import path
from . import views

urlpatterns = [

path('', views.home),
path('maruza/', views.lectures),
path('amaliyot/', views.practice),
path('resurslar/', views.resources),

]

