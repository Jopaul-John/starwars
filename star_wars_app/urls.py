from django.urls import path

from star_wars_app import views

urlpatterns = [
    path('shipname', views.ShipName.as_view()),
]