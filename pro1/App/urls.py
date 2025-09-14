from django.urls import path
from . import views


urlpatterns=[
  path("show/",views.show),
  path('lili/',views.lili),
  path('greet/',views.greet)
]
