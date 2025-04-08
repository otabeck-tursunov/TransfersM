from django.contrib import admin
from .models import *

admin.site.site_header = 'Transfer Administration'
admin.site.site_title = 'Transfer Administration'
admin.site.index_title = 'Transfer Administration'

admin.site.register(Season)
admin.site.register(Country)
admin.site.register(Club)
admin.site.register(Player)
admin.site.register(Transfer)

