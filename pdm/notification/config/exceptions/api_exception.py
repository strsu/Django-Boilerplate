import traceback

from config.exceptions.custom_exceptions import CustomException
from rest_framework.response import Response
from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):
    print(traceback.format_exc())

    response = exception_handler(exc, context)

    if response is not None:
        status_code = response.status_code
        msg = str(exc)

        if hasattr(exc, "detail"):
            msg = exc.detail

        if isinstance(exc, CustomException):
            msg = exc.detail.get("message")
            status_code = int(exc.detail.get("code"))

        response.status_code = status_code
        response.data = {"message": msg}

        return response
    else:
        msg = {"message": str(exc)}
        return Response(msg, status=500)
