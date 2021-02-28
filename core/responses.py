from django.http import JsonResponse


def bad_request(request, message=None):
    response_data = {
        'code': 400,
        'message': message or 'Invalid request format or path.'
    }

    return JsonResponse(response_data, status=400)

def not_found(request, message=None):
    response_data = {
        'code': 404,
        'message': message or 'Object not found.'
    }

    return JsonResponse(response_data, status=404)
