from core.utils import get_appended_slashes_path

from quotes_v1.views import (
    languages,
    random,
    get_quote_by_id,
)


urlpatterns = get_appended_slashes_path([
    {'path': 'languages', 'view': languages},
    {'path': 'random', 'view': random},
    {'path': 'quote/<quote_id>', 'view': get_quote_by_id},
])
