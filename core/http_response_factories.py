from django.http import JsonResponse


def create_json_response_from_data_object(data={}, message='OK.', status=200):
    response_data = data
    data['status'] = status
    data['message'] = message

    return JsonResponse(response_data, status=status)
