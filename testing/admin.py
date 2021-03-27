from django.contrib import admin
from testing.models import Person, Tracking_entry, Orders

# Register your models here.

admin.site.register(Person)
admin.site.register(Tracking_entry)
admin.site.register(Orders)
