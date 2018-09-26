import json

from django.http.response import HttpResponse, JsonResponse
from django.utils.deprecation import MiddlewareMixin


class JsonMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.method == 'POST' and request.body:
            content_type = request.META.get('CONTENT_TYPE', '')
            if 'application/json' in content_type:
                request.JSON = json.loads(request.body)

    def process_response(self, request, response):
        if isinstance(response, str):
            if response and response[0] in ('[', '{', '"'):
                return HttpResponse(response, content_type='application/json')
            return HttpResponse(response)
        elif isinstance(response, (list, tuple, set, dict,)):
            return JsonResponse(response, safe=False)
        return response