from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json
from pymongo import MongoClient

def index(request, name, age):
    data = {}
    msg = "hello, "+age+" years old "+name+"!"
    data["name"] = name
    data["age"] = age
    data["message"] = msg
    return JsonResponse(data, json_dumps_params={"indent": 2})

def advance(request):
    host = 'localhost'
    port = 27017
    client = MongoClient(host, port)
    db = "baedalgeek_test"
    col = "Users"

    data = client[db][col].find_one(None, sort=[('_id', -1)])
    del data['_id']

    msg = "hello, "+str(data['age'])+" years old "+data['name']+"!"
    data['message'] = msg

    return JsonResponse(data, json_dumps_params={"indent": 2})