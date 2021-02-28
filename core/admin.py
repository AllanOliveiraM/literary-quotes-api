from django.contrib import admin
from django.contrib.auth.models import Group

from core.models import CoreUser


admin.site.unregister(Group)
admin.site.register(CoreUser)

admin.site.site_url = ''
admin.site.site_title = 'Literary Quotes API'
admin.site.site_header = 'Literary Quotes API'
