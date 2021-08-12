import re
from django import contrib
from django.db.models.query_utils import RegisterLookupMixin
from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect, reverse
from .forms import ContactUsForm, ProfileForm
from django.core.mail import send_mail
from .models import *
from django.core.paginator import Paginator, EmptyPage,\
								  PageNotAnInteger

from django.contrib.auth.decorators import login_required
from taggit.models import Tag
from blog_post.models import *

from .decorators import unauthenticated_user
# Login&Signup Section
from .forms import UserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Translation settinf in view 
from django.conf import settings
from datetime import datetime
from django.utils.translation import activate
from .filters import RoomSearchForm, ReservationSearchForm


from django.contrib.auth.models import Group


def main(request):
	blogs = Blog.objects.order_by("-date_created")[:4]
	rooms = Room.objects.filter(status='Available').order_by("-date_created")[:6]
	testimonials = Testimonials.objects.all()
	happy_guests = Guest.objects.all().count()
	num_rooms = Room.objects.all().count()

	try:
		latest_user = User.objects.all().last()
		# print("latest user",latest_user)
		Guest.objects.create(user=latest_user, first_name=latest_user.username)
	except:
		pass

	if request.method == 'POST':

		username = request.POST['username']
		password = request.POST['password']

		user = authenticate(request, username=username, password=password)
		print("user",user)
		if user is not None:
			login(request, user)
			return redirect('home')

	current_lang = request.POST.get('lang')
	if current_lang == settings.LANGUAGES[0][0]:
		reverse('home')
		activate('en')
	elif current_lang == settings.LANGUAGES[0][1]:
		reverse('home')
		activate('uz')


	amenities = HotelAmenities.objects.all()
	instagram_images = Instagram.objects.all()
	room_facilities = RoomFacilities.objects.all()

	context = {'blogs': blogs, 'rooms':rooms, 'testimonials':testimonials, 'happy_guests':happy_guests,
	'num_rooms':num_rooms, 'amenities':amenities, 'instagram_images':instagram_images, 'room_facilities':room_facilities}
	return render(request, 'main.html', context)



def main2(request):
	return render(request, 'main2.html')


def contact(request):
	if request.method == 'POST':
		messager_name = request.POST['name']
		messager_email = request.POST['email']
		subject = request.POST['subject']
		message = request.POST['message']

		if request.user.is_authenticated:
			pass
		else:
			return redirect('user_login')

		# Sending an email
		send_mail(
			messager_name,
			message,
			[messager_email],
			['zubaycoder0022@gmail.com'],
			fail_silently=False,
		)
		return render(request, 'user/contact.html')
	return render(request, 'user/contact.html')

# @login_required(login_url="user_signup")

def restaurant(request):
	foods = Food.objects.all()
	context = {'foods': foods}
	return render(request, 'user/restaurant.html', context)



def about(request):
	testimonials = Testimonials.objects.all()
	happy_guests = Guest.objects.all().count()
	num_rooms = Room.objects.all().count()
	amenities = HotelAmenities.objects.all()
	instagram_images = Instagram.objects.all()
	room_facilities = RoomFacilities.objects.all()
	context = {'testimonials':testimonials, 'happy_guests':happy_guests, 'num_rooms':num_rooms,
	'amenities':amenities,'instagram_images':instagram_images, 'room_facilities':room_facilities}
	return render(request, 'user/about.html', context)


# Booking process starts 

@unauthenticated_user
def booking(request, pk):
	room = Room.objects.get(id=pk)
	context = {'room': room}
	return render(request, 'user/booking.html', context)


from django.views import View
import stripe
# from django.conf import settings
from django.http import JsonResponse
from django.views.generic import TemplateView

stripe.api_key = settings.STRIPE_SECRET_KEY


class SuccessView(TemplateView):
	template_name = 'user/success.html'



checkout_session_id = ""
class CreateCheckoutSessionView(View):
		def post(self, request, *args, **kwargs):
			global checkout_session_id
			YOUR_DOMAIN = "http://127.0.0.1:8000"
			checkout_session = stripe.checkout.Session.create(
					payment_method_types=['card'],
					line_items=[
							{
							'price_data': {
								'currency': 'usd',
								'unit_amount': request.session['totalroomprice']*100,
								'product_data': {
									# 'name': room.category.name + ' room' + " | "+ str(STAY_PERIOD) + " nights",

									'name': 'Your reserved rooms' + " | " + " night",
									'images': ['https://cf.bstatic.com/xdata/images/hotel/max1024x768/249726706.jpg?k=addd1393ada03988da7a1ca1976979e95366e6f2837649124a561c0d8214572f&o=&hp=1'],
								},
							},
							'quantity': 1,
						},
					],
					mode='payment',
					success_url=YOUR_DOMAIN + '/user/',
					cancel_url=YOUR_DOMAIN + '/',
				)

			checkout_session_id = checkout_session.id

			return JsonResponse({
				'id': checkout_session.id
			})


def cancel_booking(request, pk):
	reserved_rooms = Reservation.objects.filter(guest=Guest.objects.get(user=request.user))
	try:
		single_room_id = Reservation.objects.get(room_id=pk)
		single_room_id.delete()
	except:
		pass

	room = Room.objects.get(id=pk)
	room.status = "Available"
	room.save()

	return redirect(request.META.get('HTTP_REFERER'))

# Room Section 
def rooms(request):
	rooms = Room.objects.filter(status='Available')

	room_filter = RoomSearchForm(request.GET, queryset=rooms)
	rooms = room_filter.qs

	facilities = RoomFacilities.objects.all()

	context = {'rooms': rooms, 'room_filter': room_filter,'facilities':facilities}
	return render(request, 'user/rooms.html', context)




def room_single(request, pk):
	room = Room.objects.get(id=pk)
	available_rooms = Room.objects.filter(status='Available')
	room_facilities = room.facility.all()
	print(room_facilities)
	blogs = Blog.objects.order_by("-date_created")[:3]
	context = {'room': room, "available_rooms": available_rooms, "blogs": blogs, "room_facilities":room_facilities}

	return render(request, 'user/rooms-single.html', context)

# from django.urls import resolve # getting the current url name
# from urllib.parse import urlparse


def user_profile(request):
	# current_url = resolve(request.path_info).url_name # getting the current url name
	# print(current_url)
	# url_path =   request.META.get('HTTP_REFERER') #getting the previous url path
	try:
		result = stripe.checkout.Session.retrieve(
		checkout_session_id)
		reserved_rooms = Reservation.objects.filter(guest=Guest.objects.get(user=request.user),
													status="Payment process...")
		for reserved_room in reserved_rooms:
			reserved_room.status = "Paid"
			reserved_room.save()
		messages.info(request, "You have successfully paid!")
		print(result)
		paid_room_price = result["amount_total"] / 100
		print(paid_room_price)
		customer_email = result["customer_details"]["email"]
		finance_info = Finance.objects.all()
		all_emails = []
		for finance in finance_info:
			all_emails.append(finance.email)

		if customer_email in all_emails:
			user_finance_info = Finance.objects.get(email=customer_email)
			print(user_finance_info)
			print(user_finance_info.room_price)
			user_finance_info.room_price += int(paid_room_price)
			print(user_finance_info.room_price)
			user_finance_info.save()
		else:
			Finance.objects.create(customer=Guest.objects.get(user=request.user),room_price=paid_room_price, email=customer_email)


	except:
		pass

	request.session['num_night'] = 0
	reserved_room_price = 0
	if request.method == 'POST':
		check_in = request.POST.get('checkin')
		check_out = request.POST.get('checkout')
		room = request.POST.get('room')
		email = request.POST.get('email')
		passport = request.POST.get('passport')
		phone = request.POST.get('phone')
		adults = request.POST.get('adults')
		children = request.POST.get('children')
		room_number = request.POST.get('room_number')
		room_price = request.POST.get('price')
		# reserved_room_price += int(room_price)
		# print("price",reserved_room_price)
		# next = request.POST.get('next')
		next = request.GET.get('next', '/')
		date_format = "%Y-%m-%d"
		checkin_date = datetime.strptime(str(check_in), date_format)
		checkout_date = datetime.strptime(str(check_out), date_format)
		day_str = datetime.today().strftime('%Y-%m-%d')
		current_day = datetime.strptime(str(day_str), date_format)
		if checkin_date < current_day or checkin_date > checkout_date:
			messages.warning(request, "Please enter valid check_in_out dates!")
			return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))
			# return redirect(next)
		else:
			delta = checkout_date-checkin_date
			request.session['num_night'] += delta.days
		# room1 = Room.objects.get(category__name=room)
		room1 = Room.objects.get(room_number = room_number)

		# print("room-",room1)

		Reservation.objects.create(guest=Guest.objects.get(user=request.user), room=room1, check_in=check_in, check_out=check_out,
		adults=adults, children=children, email=email,passport=passport, phone_number=phone)


		room1.status = "Not-available"
		room1.save()

	reserved_rooms = Reservation.objects.filter(guest=Guest.objects.get(user=request.user)).order_by("-reservation_date")
	rooms_with_no_payment  = Reservation.objects.filter(guest=Guest.objects.get(user=request.user), status="Payment process...").order_by("-reservation_date")


	print("payment process rooms:",reserved_rooms)
	# print(reserved_rooms)
	guest_reservation_id = 0

	night = []
	for re in rooms_with_no_payment:
		guest_reservation_id = re.guest.user.id
		night = (re.check_out-re.check_in).days

		reserved_room_price += int(re.room.price) * int(night)
	print("outside",night)
	# print(reserved_room_price)
	total_room_price = reserved_room_price
	# request.totalroomprice = 9
	request.session['totalroomprice'] = total_room_price
	# print("ttotal_price", total_room_price)
	context = {
	'i':guest_reservation_id,
	'reserved_rooms': reserved_rooms,
	'num_night': night,
	'total_price':request.session['totalroomprice'],
	'STRIPE_PUBLIC_KEY': settings.STRIPE_PUBLIC_KEY}

	return render(request, 'user/user.html', context)




def profile_settings(request):
	guest = request.user.guest
	profile_form = ProfileForm(instance=guest)
	if request.method == 'POST':
		profile_form = ProfileForm(request.POST, request.FILES, instance=guest)
		if profile_form.is_valid():
			profile_form.save()
			return redirect('user_profile')
	context = {'profile_form': profile_form}
	return render(request, 'user/profile_settings.html', context)


def admin_profile(request):
	return render(request, 'user/admin_profile.html')



def user_signup(request):
	userform = UserForm()

	if request.method == 'POST':
		userform = UserForm(request.POST)
		if userform.is_valid():
			user = userform.save()
			name = userform.cleaned_data

			group = Group.objects.get(name="guest")
			user.groups.add(group)

			Guest.objects.create(user=user, first_name=name['username'])



			messages.success(request, 'Account has been successfully created!')
			return redirect('home')
	try:
		latest_user = User.objects.all().last()
		# print("latest user",latest_user)
		Guest.objects.create(user=latest_user, first_name=latest_user.username)
	except:
		pass
	latest_user = User.objects.all().last()
	print("latest user", latest_user)
	context = {'form': userform}
	return render(request, 'user/registration.html', context)


def user_login(request):
	if request.method == 'GET':
		request.session['login_from'] = request.META.get('HTTP_REFERER', '/')
	else:
		username = request.POST['username']
		password = request.POST['password']

		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return HttpResponseRedirect(request.session['login_from'])
	return render(request, 'user/login.html')


def userLogout(request):
	logout(request)
	return redirect('home')

