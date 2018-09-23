import json

from django.utils.deprecation import MiddlewareMixin


class JsonMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.method == 'POST' and request.body:
            content_type = request.META.get('CONTENT_TYPE', '')
            if 'application/json' in content_type:
                request.JSON = json.loads(request.body)

    def process_response(self, request, response):
        return response