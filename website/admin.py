from django.contrib import admin

# Register your models here.

from website.models import Contact


class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_filter = ('email',)
    list_display = ('name','email','subject', 'created_date')
    search_fields=['name','email']
admin.site.register(Contact,ContactAdmin)