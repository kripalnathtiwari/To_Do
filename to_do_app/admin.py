from django.contrib import admin

# Register your models here.
from.models import To_do_task, Deleted_task, compleated_task, ListItem
admin.site.register(To_do_task)
admin.site.register(Deleted_task)
admin.site.register(compleated_task)
admin.site.register(ListItem)