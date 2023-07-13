import json

from django.http import JsonResponse
from django.views import View


class APIHome(View):
    def get(self, request):
        data = {}
        body = request.body
        try:
            data = json.loads(body)
        except:
            pass
        print(data)
        print(request.headers)
        return JsonResponse(data)
