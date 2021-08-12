from django.urls import path
from .views import *


app_name = "hotel_manager"

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('rooms/', Rooms.as_view(), name="rooms"),
    path("room-create/", RoomCreate.as_view(), name="room-create"),
    path("room-update/<int:pk>/", RoomUpdate.as_view(), name="room-update"),
    path("room-delete/<int:pk>/",room_delete, name="room-delete"),


    path("posts/", BlogPosts.as_view(), name="posts"),
    path("post-create/", PostCreate.as_view(), name="post-create"),
    path("post-update/<int:pk>/",  PostUpdate.as_view(), name="post-update"),
    path("post-delete/<int:pk>/",post_delete, name="post-delete"),

    path("restaurant/", Restaurant.as_view(), name="restaurant"),
    path('restaurant-create/', RestaurantCreate.as_view(), name="restaurant-create"),
    path("restaurant-update/<int:pk>/", RestaurantUpdate.as_view(), name="restaurant-update"),
    path('restaurant-delete/<int:pk>/', restaurant_delete, name="restaurant-delete"),

    path("guests/", Guests.as_view(),name="guests"),

    path('room-category/', RoomCategory.as_view(), name="room-category"),
    path('room-category-create', RoomCategoryCreate.as_view(), name="room-category-create"),


    path('reservation-list/', Reservation.as_view(), name="reservation-list"),

    path('testimonials/', Testimonials.as_view(), name="testimonials"),
    path('testimonials-create/', TestimonialsCreate.as_view(), name="testimonials-create"),
    path('testimonials-update/<int:pk>/', TestimonialsUpdate.as_view(), name="testimonials-update"),
    path('testimonials-delete/<int:pk>/', testimonials_delete, name="testimonials-delete"),

    path('instagram-update/<int:pk>/', InstagramUpdateView.as_view(), name="instagram-update"),
    path('instagram-delete/<int:pk>/', instagram_delete, name="instagram-delete"),
]