from django.contrib import admin
from .models import Entry

class EntryAdmin(admin.ModelAdmin):
    list_display = ('word', 'definition', 'status')
    list_filter = ('status',)
    search_fields = ('word', 'definition')


admin.site.register(Entry, EntryAdmin)