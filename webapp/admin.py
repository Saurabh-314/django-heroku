from django.contrib import admin
from django.db.models import fields
from .models import Registration

# admin.site.register(Registration)


class RegistrationAdmin(admin.ModelAdmin):
    
    list_display = ["name","price","brand","typ","desc","img"]
    search_fields=["name","brand"]
    list_filter = ["name","price","typ","brand"]

admin.site.register(Registration,RegistrationAdmin)