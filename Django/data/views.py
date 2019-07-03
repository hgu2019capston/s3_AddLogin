from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.utils import json
from rest_framework import serializers
from rest_framework import viewsets

from data.models import Stones
from .serializers import OmokSerializer
from django.shortcuts import redirect, render


class Session1View(TemplateView):
    def get(self, request, **kwargs):
         if request.method == 'GET':
            return render(request, 'index.html', context=None)

    def post(self, request, **kwargs):
        return redirect(reverse('session2'))

class Session2View(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index1.html', context=None)
    
    def post(self, request, **kwargs):
        return redirect(reverse('session1'))


@api_view(["POST"])
def CalcTest(x1):
    try:
        x=json.loads(x1.body.decode('utf-8'))
        y=str(x*100)
        return JsonResponse("result:"+y,safe=False)
    except ValueError as e:
        return Response(e.args[0],status.HTTP_400_BAD_REQUEST)


class OmokViewSet(viewsets.ModelViewSet):
        queryset = Stones.objects.all()
        serializer_class = OmokSerializer


