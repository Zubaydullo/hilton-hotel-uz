from django import forms
from user.models import *
from blog_post.models import *


class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = "__all__"


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = "__all__"


class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = "__all__"

class RoomCategoryForm(forms.ModelForm):
    class Meta:
        model = RoomCategory
        fields = "__all__"


class TestimonialsForm(forms.ModelForm):
    class Meta:
        model = Testimonials
        fields = "__all__"


class InstagramUpdateForm(forms.ModelForm):
    class Meta:
        model = Instagram
        fields = "__all__"