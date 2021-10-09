from django.contrib import admin

from .models import Dsuser

# Register your models here.
class DsuserAdmin(admin.ModelAdmin):
    list_display = [ 'id', 'email', 'registered_date' ]

admin.site.register(Dsuser, DsuserAdmin)