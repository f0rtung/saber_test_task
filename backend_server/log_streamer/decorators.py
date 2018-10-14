from functools import wraps

from .responses import ErrorResponse


def check_post_method(func):
    @wraps(func)
    def func_wrapper(request, *args, **kwargs):
        if request.method == 'POST':
            return func(request, *args, **kwargs)
        else:
            response = ErrorResponse("Invalid method ({}) !".format(request.method))
            return response.create_http_response()
    return func_wrapper
