from django.contrib import admin

from countries.models import Country, UsState


class CountryAdmin(admin.ModelAdmin):
    list_display = ('printable_name', 'iso')

class UsStateAdmin(admin.ModelAdmin):
    list_display = ('abbrev', 'name')

admin.site.register(Country, CountryAdmin)
admin.site.register(UsState, UsStateAdmin)
