from django.contrib import admin
from .models import Contact


class ContactFormAdmin(admin.ModelAdmin):
    readonly_fields = (
        'contact_name',
        'contact_email',
        'contact_message',
        'date',
    )

    fields = (
        'contact_email',
        'contact_name',
        'date',
        'contact_message',
    )

    list_display = (
        'contact_email',
        'date',
    )

    ordering = ('-date',)


admin.site.register(Contact, ContactFormAdmin)

