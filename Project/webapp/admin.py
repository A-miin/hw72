from django.contrib import admin
from webapp.models import Quote
# Register your models here.

class QuoteAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'text']
    fields = ['id', 'text', 'name', 'email','rate', 'is_moderated', 'created_at']
    readonly_fields = ['id','created_at']

admin.site.register(Quote, QuoteAdmin)