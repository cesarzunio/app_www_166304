from django.contrib import admin
from .models import Osoba, Stanowisko


class OsobaAdmin(admin.ModelAdmin):
    # readonly_fields = ['data_dodania']
    list_filter = ['data_dodania', 'stanowisko']
    list_display = ['nazwisko', 'plec', 'get_stanowisko']

    @admin.display(description='Stanowisko')
    def get_stanowisko(self, obj):
        return f'{obj.stanowisko.nazwa} ({obj.stanowisko.id})'


admin.site.register(Osoba, OsobaAdmin)
admin.site.register(Stanowisko)
