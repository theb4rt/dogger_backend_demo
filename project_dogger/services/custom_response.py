from rest_framework.response import Response

from rest_framework import status as code_status


def response_ok(status=True, message='ok', data=None, type_response=True):
    if data is None:
        data = {}

    if type_response:
        return Response({
            "status": status,
            "data": data,
            "message": message
        }, status=code_status.HTTP_200_OK)

    return {
        "status": status,
        "data": data,
        "message": message
    }


def response_error(status=False, message='error', data=None, type_response=True):
    if data is None:
        data = {}

    if type_response:
        return Response({
            "status": status,
            "data": data,
            "message": message
        }, status=code_status.HTTP_500_INTERNAL_SERVER_ERROR)

    return {
        "status": status,
        "data": data,
        "message": message
    }
