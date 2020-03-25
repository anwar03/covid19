from django.contrib import admin
from .models import Contact, Address, Country

admin.site.register(Contact)
admin.site.register(Address)
admin.site.register(Country)