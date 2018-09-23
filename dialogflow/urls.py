from django.urls import path
from django.http.response import HttpResponse
from .views import fulfillment

urlpatterns = [
    path('', fulfillment),
]