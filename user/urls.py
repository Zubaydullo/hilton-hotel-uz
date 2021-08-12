from django.urls import path
from .views import *



urlpatterns = [
	path('', main, name='home'),
	path('main2/', main2, name='main2'),
	path('contact/', contact, name='contact'),
	path('about/', about, name='about'),


	path('user/', user_profile, name='user_profile'),
	path('profile_settings/', profile_settings, name='profile_settings'),
	path('rooms/', rooms, name='rooms'),
	path('room-single/<str:pk>/', room_single, name='room-single'),

	path('booking/<str:pk>/', booking, name='booking'),
	path('cancel_booking/<str:pk>/', cancel_booking, name='cancel_booking'),
	
	# stripe 
	path('success/', SuccessView.as_view(), name='success'),
    path('create-checkout-session/<pk>/', CreateCheckoutSessionView.as_view(), name='create-checkout-session'),
	# stripe 

	path('restaurant/', restaurant, name='restaurant'),

	path('signup/', user_signup, name='user_signup'),
	path('login/', user_login, name='user_login'),
	path('logout/', userLogout, name='logout'),

]
