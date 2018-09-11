from django.shortcuts import render
from django.http.response import JsonResponse


def fulfillment(request):
    print(request.body)

    return JsonResponse({})