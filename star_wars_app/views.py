from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
import json
from star_wars_app import altagram

class ShipName(APIView):

    def get(self, request):
        shipNames = altagram.getShipNames()
        shipNamesSerialized = json.dumps(shipNames)
        return Response({"data": shipNamesSerialized})