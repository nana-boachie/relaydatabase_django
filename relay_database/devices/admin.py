from django.contrib import admin
from .models import Relay

# Register your models here.
class RelayAdmin(admin.ModelAdmin):
    list_display = ('name','area')
    list_filter = ('name','area')
     
admin.site.register(Relay,RelayAdmin)