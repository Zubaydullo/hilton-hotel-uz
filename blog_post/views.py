from django.shortcuts import get_object_or_404, render, redirect, reverse
from .forms import BlogCommentForm
from django.core.mail import send_mail
from .models import *
from django.core.paginator import Paginator, EmptyPage,\
								  PageNotAnInteger

from django.contrib.auth.decorators import login_required
from taggit.models import Tag
from user.models import Guest
from user.decorators import *


def blog_list(request):
	blogs = Blog.objects.all()
	paginator = Paginator(blogs, 4) # 3 posts in each page
	page = request.GET.get('page')
	try:
		blogs = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer deliver the first page
		blogs = paginator.page(1)
	except EmptyPage:
		# If page is out of range deliver last page of results
		blogs = paginator.page(paginator.num_pages)
	context = {'blogs': blogs}
	return render(request, 'blog_post/blog_list.html', context)


@unauthenticated_user
def blog_single(request, pk):
	blogs = Blog.objects.order_by("-date_created")[:3]
	blog = Blog.objects.get(id=pk)
	comments = blog.comments.filter(active=True)

	new_comment = None	
	tags =Tag.objects.all()

	if request.method == 'POST':
		blog_comment_form = BlogCommentForm(data=request.POST)
		if request.user.is_authenticated:
			if blog_comment_form.is_valid():
				new_comment = blog_comment_form.save(commit=False)
				new_comment.post = blog
				new_comment.guest = Guest.objects.get(user=request.user) 
				new_comment.save()
		else:
			return redirect('user_login')
	else:
		blog_comment_form = BlogCommentForm()


	context = {'blog_comment_form': blog_comment_form,
	'blog': blog, 'blogs': blogs, 'comments': comments, 'tags':tags}
	return render(request, 'blog_post/blog_single.html', context)



def posts_with_tag(request, tag_slug=None):
	blogs = Blog.objects.all()
	tag = None

	if tag_slug:
		tag = get_object_or_404(Tag, slug=tag_slug)
		blogs = blogs.filter(tags__in = [tag])
	paginator = Paginator(blogs, 4) # 3 posts in each page
	page = request.GET.get('page')
	try:
		blogs = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer deliver the first page
		blogs = paginator.page(1)
	except EmptyPage:
		# If page is out of range deliver last page of results
		blogs = paginator.page(paginator.num_pages)
	context = {'tag':tag, 'blogs':blogs}

	return render(request, 'blog_post/posts_with_tags.html', context)
