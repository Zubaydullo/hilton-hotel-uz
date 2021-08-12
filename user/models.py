from re import S, T
from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model
from django.db.models.expressions import F


class Food(models.Model):
	food_name = models.CharField(max_length=100, null=True)
	price = models.FloatField(default=None, null=True)
	description = models.TextField()
	food_image = models.ImageField(upload_to='images/restaurant/menu', blank=True)

	def __str__(self):
		return self.food_name


class RoomCategory(models.Model):
	name = models.CharField(max_length=100, null=True)

	def __str__(self):
		return self.name


class RoomView(models.Model):
	description = models.CharField(max_length=100, null=True)

	def __str__(self):
		return self.description


class RoomFacilities(models.Model):
	facility_name = models.CharField(max_length=100, null=True)

	def __str__(self):
		return self.facility_name


class Room(models.Model):
	AVAILABILITY = (
		('Available', 'Available'),
		('Not-available', 'Not-available')
	)

	image_1 = models.ImageField(upload_to='images/room_images', blank=True)
	image_2 = models.ImageField(upload_to='images/room_images', blank=True)
	image_3 = models.ImageField(upload_to='images/room_images', blank=True)
	room_size = models.IntegerField()
	room_number = models.IntegerField(unique=True)
	price = models.IntegerField(default=0)
	adults = models.IntegerField()
	children = models.IntegerField()
	bed = models.IntegerField()
	date_created = models.DateTimeField(auto_now_add=True)
	status = models.CharField(max_length=100, choices=AVAILABILITY, default='Not-Available')
	category = models.ForeignKey(RoomCategory, on_delete=models.CASCADE, null=True, related_name='room_category')
	facility = models.ManyToManyField(RoomFacilities)
	view = models.ForeignKey(RoomView, on_delete=models.CASCADE, null=True, related_name='room_view')
	explanation = models.TextField()

	def __str__(self):
		return str(self.room_number) + ' room'


class Guest(models.Model):
	user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
	first_name = models.CharField(max_length=100, null=True, blank=True)
	last_name = models.CharField(max_length=155, null=True, blank=True)
	email = models.EmailField(blank=True)
	phone = models.CharField(max_length=30, blank=True)
	age = models.PositiveIntegerField(null=True, blank=True)
	address = models.CharField(max_length=255, blank=True)
	city = models.CharField(max_length=100, blank=True)
	country = models.CharField(max_length=100, blank=True)
	profile_pic = models.ImageField(upload_to='images/users_images', default='images/user.png', blank=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)

	def __str__(self):
		return self.user.username


class Reservation(models.Model):
	STATUS = (
		('Payment process...', 'Payment process...'),
		('Paid', 'Paid'),
	)
	guest = models.ForeignKey(Guest, on_delete=models.CASCADE, null=True, blank=True)
	room = models.ForeignKey(Room, on_delete=models.CASCADE, null=True, blank=True)
	reservation_date = models.DateTimeField(auto_now_add=True)
	check_in = models.DateField(null=True, blank=True)
	check_out = models.DateField(null=True, blank=True)
	adults = models.PositiveIntegerField()
	children = models.PositiveIntegerField()
	email = models.EmailField(blank=False)
	passport = models.CharField(max_length=25, null=True, blank=False)
	phone_number = models.CharField(max_length=50, blank=False)
	status = models.CharField(max_length=100, choices=STATUS, default="Payment process...")

	def __str__(self):
		return self.guest.user.username + " | " + str(self.room.room_number) + " room"


class Finance(models.Model):
	customer = models.OneToOneField(Guest, on_delete=models.CASCADE, null=True, blank=True)
	email = models.EmailField()
	room_price = models.FloatField(default=0)
	received_date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.customer.user.username + " | $ " + str(self.room_price)


class Testimonials(models.Model):
	name = models.CharField(max_length=50)
	image = models.ImageField(upload_to='images/testimonials', default='images/user.png', blank=True)
	comment = models.TextField()

	def __str__(self):
		return self.name


class HotelAmenities(models.Model):
	icon_class = models.CharField(max_length=100)
	heading = models.CharField(max_length=200)

	def __str__(self):
		return self.heading


class Instagram(models.Model):
	image = models.ImageField(upload_to='images/instagram', blank=False)
