from django.contrib import admin

from .models import DSUser

# Register your models here.
class DSUserAdmin(admin.ModelAdmin):
    list_display = [ 'name', 'email', 'registered_date' ]

admin.site.register(DSUser, DSUserAdmin)