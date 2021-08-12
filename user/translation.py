from modeltranslation.translator import translator, register, TranslationOptions
from .models import *


class RoomTranslationOptions(TranslationOptions):
    fields = ('explanation',)

translator.register(Room, RoomTranslationOptions)

# @register(Room)
# class RoomTranslationOptions(TranslationOptions):
#     fields = ('explanation',)


class RoomCategoryTranslationOptions(TranslationOptions):
    fields = ('name',)

translator.register(RoomCategory, RoomCategoryTranslationOptions)


class FoodTranslationOptions(TranslationOptions):
    fields = ('food_name', 'description',)

translator.register(Food, FoodTranslationOptions)


class RoomViewTranslationOptions(TranslationOptions):
    fields = ('description',)

translator.register(RoomView, RoomViewTranslationOptions)

class RoomFacilitiesPropertyTranslationOptions(TranslationOptions):
    fields = ('facility_name',)

translator.register(RoomFacilities, RoomFacilitiesPropertyTranslationOptions)


class ReservationTranslationOptions(TranslationOptions):
    fields = ('status',)

translator.register(Reservation, ReservationTranslationOptions)


class TestimonialsTranslationOptions(TranslationOptions):
    fields = ('comment',)

translator.register(Testimonials, TestimonialsTranslationOptions)


class HotelAmenitiesTranslationOptions(TranslationOptions):
    fields = ('heading',) 

translator.register(HotelAmenities, HotelAmenitiesTranslationOptions)


