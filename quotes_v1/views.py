from random import choice

from django.views.decorators.http import require_http_methods

from django.http import JsonResponse

from quotes_v1.models import Languages, Quotes
from quotes_v1.serializers import (
    list_all_languages,
    format_random_quote_data,
)

from core.responses import not_found


@require_http_methods(['GET', ])
def languages(request):
    return JsonResponse(list_all_languages(Languages))


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

    return JsonResponse(format_random_quote_data(random_quote))
