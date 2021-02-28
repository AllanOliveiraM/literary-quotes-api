from core.http_response_factories import create_json_response_from_data_object


def bad_request(request, message=None):
    response_status = 400
    response_message = message or 'Invalid request format or path.'

    return create_json_response_from_data_object(
        message=response_message,
        status=response_status
    )


def not_found(request, message=None):
    response_status = 404
    response_message = message or 'Object not found.'

    return create_json_response_from_data_object(
        message=response_message,
        status=response_status
    )
