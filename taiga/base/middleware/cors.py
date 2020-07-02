
from django import http
from django.conf import settings


CORS_ALLOWED_ORIGINS = "*"
CORS_ALLOWED_METHODS = ["POST", "GET", "OPTIONS", "PUT", "DELETE", "PATCH", "HEAD"]
CORS_ALLOWED_HEADERS = ["content-type", "x-requested-with",
                         "authorization", "accept-encoding",
                         "x-disable-pagination", "x-lazy-pagination",
                         "x-host", "x-session-id", "set-orders"]
CORS_ALLOWED_CREDENTIALS = True
CORS_EXPOSE_HEADERS = ["x-pagination-count", "x-paginated", "x-paginated-by",
                        "x-pagination-current", "x-pagination-next", "x-pagination-prev",
                        "x-site-host", "x-site-register"]

CORS_EXTRA_EXPOSE_HEADERS = getattr(settings, "APP_EXTRA_EXPOSE_HEADERS", [])


class CorsMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        self.process_request(request)
        response = self.get_response(request)
        self.process_response(request, response)

        return response

    def _populate_response(self, response):
        response["Access-Control-Allow-Origin"] = CORS_ALLOWED_ORIGINS
        response["Access-Control-Allow-Methods"] = ",".join(CORS_ALLOWED_METHODS)
        response["Access-Control-Allow-Headers"] = ",".join(CORS_ALLOWED_HEADERS)
        response["Access-Control-Expose-Headers"] = ",".join(CORS_EXPOSE_HEADERS + CORS_EXTRA_EXPOSE_HEADERS)
        response["Access-Control-Max-Age"] = "3600"

        if CORS_ALLOWED_CREDENTIALS:
            response["Access-Control-Allow-Credentials"] = "true"

    def process_request(self, request):
        if "HTTP_ACCESS_CONTROL_REQUEST_METHOD" in request.META:
            response = http.HttpResponse()
            self._populate_response(response)
            return response
        return None

    def process_response(self, request, response):
        self._populate_response(response)
        return response
