from django.urls import path


def get_appended_slashes_path(urlpatterns):
    formatted_urlpatterns = []

    for urlpattern in urlpatterns:
        formatted_urlpatterns.append(path(urlpattern['path'], urlpattern['view']))
        formatted_urlpatterns.append(path(urlpattern['path']+'/', urlpattern['view']))

    return formatted_urlpatterns
