from django.contrib import admin

from .models import *

# admin.site.register(ListEmails)
# admin.site.register(Participants)
# admin.site.register(Aggregate)


@admin.register(Participants)
class ParticipantsAdmin(admin.ModelAdmin):
    list_display = ("Name",)


@admin.register(ListEmails)
class ListEmailsAdmin(admin.ModelAdmin):
    list_display = ("participant", "email")


@admin.register(Aggregate)
class AggregateAdmin(admin.ModelAdmin):
    list_display = ("all",)

# Register your models here.
