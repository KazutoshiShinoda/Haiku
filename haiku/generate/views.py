# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from generate.models import Generation
from generate.serializers import GenerateSerializer


@csrf_exempt
def generation_list(request):
    if request.method == 'GET':
        g = Generation.objects.all()
        s = GenerateSerializer(g, many=True)
        return JsonResponse(s.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        s = GenerateSerializer(data=data)
        if s.is_valid():
            s.save()
            return JsonResponse(s.data, status=201)
        return JsonResponse(s.errors, status=400)
