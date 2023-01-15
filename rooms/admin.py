from django.contrib import admin
from .models import Room, Amenity


# Register your models here.


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "price",
        "kind",
        "owner",
        "create_at",
        "update_at",
    )
    list_filter = (
        "country",
        "city",
        "price",
        "romms",
        "kind",
        "pet_friendly",
        "amenity",
        "create_at",
        "update_at",
    )
    search_fields = (
        "name",
        "address",
    )


@admin.register(Amenity)
class AmenityAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "description",
        "create_at",
        "update_at",
    )
    readonly_fields = (
        "create_at",
        "update_at",
    )
