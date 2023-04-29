from django.contrib import admin

from .models import *


class BookingPierAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'pier', 'time_booking_start', 'time_booking_finish', 'wish', 'pier_status', 'time_create', 'is_published')
    list_display_links = ('id', )  # possibility of editing
    search_fields = ('user', 'pier', 'time_booking_start', 'time_booking_finish')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create', 'time_booking_start', 'time_booking_finish', 'user')
    # prepopulated_fields = {"slug": ("title",)}


class PierAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    # prepopulated_fields = {"slug": ("name",)}


# admin.site.register(BookingPier, BookingPierAdmin)
# admin.site.register(Pier, PierAdmin)

admin.site.register(BookingPier, BookingPierAdmin)
admin.site.register(Pier, PierAdmin)
