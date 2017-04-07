import time
from django.conf import settings
from django.shortcuts import redirect


class SleepMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def Sleep(self, request, view_func, view_args, view_kwargs):
        time.sleep(5)
