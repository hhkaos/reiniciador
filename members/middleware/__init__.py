# myapp/middleware/__init__.py

from django.core.exceptions import SuspiciousOperation
from django.views.defaults import server_error


class SquashInvalidHostMiddleware(object):
    """
    Middleware class to squash errors due to suspicious Host: headers.
    """

    def process_request(self, request):
        """
        Check for denied Hosts.
        """

        try:
            # Attempt to obtain Host: from http header.  This may elicit a
            # SuspiciousOperation if Host: doesn't match ALLOWED_HOSTS.
            # Unceremoniously squash these errors to prevent log emails,
            # diverting straight to 500 page.

            request.get_host()
        except SuspiciousOperation:
            return server_error(request)
