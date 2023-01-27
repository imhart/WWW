from django.contrib import admin
from .models import *

class osobaAdmin(admin.ModelAdmin):
    list_display = ['imie', 'nazwisko']
    list_filter = ('data_dodania',)

# ten obiekt też trzeba zarejestrować w module admin
admin.site.register(Osoba, osobaAdmin)

class DruzynaAdmin(admin.ModelAdmin):
    list_display = ['nazwa', 'kraj']
    list_filter = ('kraj',)

# ten obiekt też trzeba zarejestrować w module admin
admin.site.register(Druzyna, DruzynaAdmin)


# Register your models here.
