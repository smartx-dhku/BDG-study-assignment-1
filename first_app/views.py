from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json

def index(request, name, age):
    data = {}
    msg = "hello, "+age+" years old "+name+"!"
    data["name"] = name
    data["age"] = age
    data["message"] = msg
    return JsonResponse(data, json_dumps_params={"indent": 2})