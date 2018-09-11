from django.urls import path
from django.http.response import HttpResponse

urlpatterns = [
    path('', lambda request: HttpResponse('Hello World')),
]