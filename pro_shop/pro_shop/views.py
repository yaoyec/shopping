import json

from django.http import JsonResponse
from django.shortcuts import render


def test_cross(request):
    return render(request, 'test_cors.html')


def test_cross_server(request):
    data = {'name': 'chenbao', 'age': 22}
    json_str = json.dumps(data)
    return JsonResponse(json_str, safe=False)
