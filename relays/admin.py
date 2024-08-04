from django.contrib import admin
from .models import Relay



class RelayAdmin(admin.ModelAdmin):
    list_display = ('relay_name', 'manufacturer')
    search_fields = ('relay_name', 'manufacturer')
    list_filter = ('manufacturer',)


# Register your models here.
admin.site.register(Relay,RelayAdmin)
