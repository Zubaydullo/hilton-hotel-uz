from django.shortcuts import redirect, render, reverse
from django.views.generic import CreateView, ListView, DeleteView, DeleteView
from django.views.generic.edit import UpdateView, FormView
from user.models import *
from blog_post.models import *
from .forms import *
from .models import *
from user.decorators import *
from django.contrib.auth.decorators import login_required

@login_required(login_url='user_login')
@admin_only
def dashboard(request):
	overall = 0
	total_price = Finance.objects.all()
	for price in total_price:
		overall += price.room_price
	finances = Finance.objects.all()
	instagram_images = Instagram.objects.all()
	hotel_amenities = HotelAmenities.objects.all()
	context = {'overall': overall, 'finances': finances, 'instagram_images':instagram_images, 'hotel_amenities':hotel_amenities}
	return render(request, 'hotel_manager/dashboard.html', context)


class Rooms(ListView):
	template_name = "hotel_manager/rooms.html"
	queryset = Room.objects.filter(status="Available")
	context_object_name = "rooms"


class RoomCreate(CreateView):
	template_name = "hotel_manager/manager_create_update.html"
	form_class = RoomForm

	def get_success_url(self):
		return reverse("hotel_manager:rooms")


class RoomUpdate(UpdateView):
	template_name = "hotel_manager/manager_create_update.html"
	queryset = Room.objects.all()
	form_class = RoomForm

	def get_success_url(self):
		return reverse("hotel_manager:rooms")


def room_delete(request, pk):
	room = Room.objects.get(id=pk)
	room.delete()
	return redirect("hotel_manager:rooms")


class BlogPosts(ListView):
	queryset = Blog.objects.all()
	template_name = "hotel_manager/blog-posts.html"
	context_object_name = "posts"


class PostCreate(CreateView):
	template_name = "hotel_manager/manager_create_update.html"
	form_class = BlogForm

	def get_success_url(self):
		return reverse("hotel_manager:posts")


class PostUpdate(UpdateView):
	template_name = "hotel_manager/manager_create_update.html"
	queryset = Blog.objects.all()
	form_class = BlogForm

	def get_success_url(self):
		return reverse("hotel_manager:posts")


def post_delete(request, pk):
	post = Blog.objects.get(id=pk)
	post.delete()
	return redirect("hotel_manager:posts")




class Restaurant(ListView):
	template_name = "hotel_manager/restaurant-foods.html"
	queryset = Food.objects.all()
	context_object_name = "foods"

class RestaurantCreate(CreateView):
	template_name = "hotel_manager/manager_create_update.html"
	form_class = RestaurantForm

	def get_success_url(self):
		return reverse("hotel_manager:restaurant")


class RestaurantUpdate(UpdateView):
	template_name = "hotel_manager/manager_create_update.html"
	queryset = Food.objects.all()
	form_class = RestaurantForm

	def get_success_url(self):
		return reverse("hotel_manager:restaurant")


def restaurant_delete(request, pk):
	post = Food.objects.get(id=pk)
	post.delete()
	return redirect("hotel_manager:restaurant")

class Guests(ListView):
	template_name = "hotel_manager/guests.html"
	queryset = Guest.objects.all()
	context_object_name = "guests"


class RoomCategory(ListView):
	template_name = "hotel_manager/room_category.html"
	queryset = RoomCategory.objects.all()
	context_object_name = "room_category"



class RoomCategoryCreate(CreateView):
	template_name = "hotel_manager/manager_create_update.html"
	form_class = RoomCategoryForm

	def get_success_url(self):
		return reverse("hotel_manager:room-category")



class Reservation(ListView):
	template_name = "hotel_manager/reservation.html"
	queryset = Reservation.objects.all()
	context_object_name = "reservations"

	def get_success_url(self):
		return reverse('hotel_manager:reservation-list')


class Testimonials(ListView):
	template_name = "hotel_manager/testimonials.html"
	queryset = Testimonials.objects.all()
	context_object_name = "testimonials"

	def get_success_url(self):
		return reverse('hotel_manager:testimonials')


class TestimonialsCreate(CreateView):
	template_name = "hotel_manager/manager_create_update.html"
	form_class = TestimonialsForm

	def get_success_url(self):
		return reverse("hotel_manager:testimonials")


# def testimonials_update(request, pk):
# 	testimonial = Testimonials.objects.get(id=pk)
# 	forma = TestimonialsUpdateForm
#
# 	if request.method == "POST":
# 		forma = TestimonialsUpdateForm(request.POST, instance=testimonial)
# 		if forma.is_valid():
# 			forma.save()
# 			return redirect("hotel_manager:testimonials")
# 	context = {'form': forma}
# 	return render(request, 'hotel_manager/manager_create_update.html', context)
class TestimonialsUpdate(UpdateView):
	template_name = "hotel_manager/manager_create_update.html"
	# queryset = Testimonials.objects.all()
	model = Testimonials
	form_class = TestimonialsForm

	def get_success_url(self):
		return reverse("hotel_manager:testimonials")


def testimonials_delete(request, pk):
	testimonial = Testimonials.objects.get(id=pk)
	testimonial.delete()
	return redirect('hotel_manager:testimonials')


class InstagramUpdateView(UpdateView):
	model = Instagram
	form_class = InstagramUpdateForm
	template_name = "hotel_manager/manager_create_update.html"

	def get_success_url(self):
		return reverse("hotel_manager:dashboard")


def instagram_delete(request, pk):
	image = Instagram.objects.get(id=pk)
	image.delete()
	return redirect("hotel_manager:dashboard")

