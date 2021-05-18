from django.contrib import admin
from propertylistings.models import Propertydetails


class PropertyAdmin(admin.ModelAdmin):
    list_display = ("city", "description", "address", "bedrooms", "bathrooms")


admin.site.register(Propertydetails, PropertyAdmin)