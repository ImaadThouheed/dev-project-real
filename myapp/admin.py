from django.contrib import admin
from .models import Guard, GuardReal, BookingReal

# Register the Guard model in the admin interface
admin.site.register(Guard)

# Register the GuardReal model in the admin interface
admin.site.register(GuardReal)

admin.site.register(BookingReal)