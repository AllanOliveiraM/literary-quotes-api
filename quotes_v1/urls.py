from core.utils import get_appended_slashes_path

from quotes_v1.views import (
    languages,
    random
)


urlpatterns = get_appended_slashes_path([
    {'path': 'languages', 'view': languages},
    {'path': 'random', 'view': random},
])
