from django.contrib import admin
from .models import *

from modeltranslation.admin import TranslationAdmin, TranslationTabularInline


# admin.site.register(Room)
# admin.site.register(RoomCategory)
# admin.site.register(RoomView)
# admin.site.register(Food)
admin.site.register(Guest)
# admin.site.register(Reservation)
# admin.site.register(FacilityProperty)
admin.site.register(Finance)
# admin.site.register(Testimonials)
# admin.site.register(Amenities)
admin.site.register(Instagram)


class RoomAdmin(TranslationAdmin):
    model = Room

admin.site.register(Room, RoomAdmin)

class RoomCategoryAdmin(TranslationAdmin):
    model = RoomCategory

admin.site.register(RoomCategory, RoomCategoryAdmin)

class FoodAdmin(TranslationAdmin):
    model = Food

admin.site.register(Food, FoodAdmin)


class RoomViewAdmin(TranslationAdmin):
    model = RoomView

admin.site.register(RoomView, RoomViewAdmin)


class RoomFacilitiesAdmin(TranslationAdmin):
    model = RoomFacilities

admin.site.register(RoomFacilities, RoomFacilitiesAdmin)


class ReservationAdmin(TranslationAdmin):
    model = Reservation

admin.site.register(Reservation, ReservationAdmin)


class TestimonialsAdmin(TranslationAdmin):
    model = Testimonials

admin.site.register(Testimonials, TestimonialsAdmin)


# class AmenitiesAdmin(TranslationAdmin):
#     model = Amenities

# admin.site.register(Amenities, AmenitiesAdmin)