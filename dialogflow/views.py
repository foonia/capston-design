from django.shortcuts import render
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def fulfillment(request):
    print(request.JSON)

    return JsonResponse({})