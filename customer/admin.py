from django.contrib import admin

from .models import Customer, License, Passport



admin.site.register(Customer)
admin.site.register(License)
admin.site.register(Passport)
