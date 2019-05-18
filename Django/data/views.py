from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.utils import json
from rest_framework import serializers
from rest_framework import viewsets

from data.models import Stones
from .serializers import OmokSerializer

class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)


@api_view(["POST"])
def CalcTest(x1):
    try:
        x=json.loads(x1.body.decode('utf-8'))
        y=str(x*100)
        return JsonResponse("Result:"+y,safe=False)
    except ValueError as e:
        return Response(e.args[0],status.HTTP_400_BAD_REQUEST)


class OmokViewSet(viewsets.ModelViewSet):
    queryset = Stones.objects.all()
    serializer_class = OmokSerializer

