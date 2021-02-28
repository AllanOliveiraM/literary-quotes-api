'''Quotes datastructure serializers.'''


def list_all_languages(model):
    languages_queryset = model.objects.all()

    available_languages = []

    for language_queryset in languages_queryset:
        available_languages.append({
            'language': language_queryset.language,
            'language_code': language_queryset.language_code,
        })

    return {
        'available_languages': available_languages
    }


def format_quote_data(queryset):
    return {
        'literary_quote': {
            'quote': queryset.quote,
            'book': queryset.book,
            'author': queryset.author,
            'language': queryset.language.language_code,
            'id': queryset.id,
        }
    }
