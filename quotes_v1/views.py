from random import choice

from django.views.decorators.http import require_http_methods

from core.responses import (
    not_found,
    bad_request,
)
from core.http_response_factories import create_json_response_from_data_object

from quotes_v1.models import Languages, Quotes
from quotes_v1.serializers import (
    list_all_languages,
    format_quote_data,
)


@require_http_methods(['GET', ])
def languages(request):
    return create_json_response_from_data_object(
        data=list_all_languages(Languages),
    )


@require_http_methods(['GET', ])
def get_quote_by_id(request, quote_id):
    if not str(quote_id).isnumeric():
        return bad_request(request, f"{quote_id} is an invalid ID number.")

    matched_quote = Quotes.objects.filter(id=quote_id)

    if not matched_quote:
        return not_found(request, f'Quote {quote_id} not found.')

    return create_json_response_from_data_object(
        format_quote_data(matched_quote.first()),
    )


@require_http_methods(['GET', ])
def random(request):
    language = request.GET.get('language')

    if language is not None:
        language_queryset = Languages.objects.filter(
            language_code=language
        ).first()

        if not language_queryset:
            return not_found(request, 'Language not found.')

        quotes_items = Quotes.objects.all().filter(language=language_queryset)
    else:
        quotes_items = Quotes.objects.all()

    if not quotes_items:
        return not_found(request, 'No quotes found')

    random_quote = choice(list(quotes_items))

    return create_json_response_from_data_object(
        format_quote_data(random_quote),
    )
