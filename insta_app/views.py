from django.shortcuts import render
from .models import Post, Profile
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
	return render(request, 'insta_app/index.html', {})

def signup(request):
	return render(request, 'insta_app/signup.html', {})

def signin(request):
	return render(request, 'insta_app/signin.html', {})

@login_required(login_url='/insta_app/signin/')
def user_profile(request):
	user = request.user
	posts = Post.objects.filter(user=request.user).order_by('-uploaded_on')
	context = {
		'user': user,
		'posts': posts,
	}
	return render(request, 'insta_app/profile.html', context)

def post_view(request):
	posts = Post.objects.all().order_by('-uploaded_on')
	context = {
		'posts': posts,
	}
	return render(request, 'insta_app/posts.html', context)

def post_detail(request, pk):
	post = Post.objects.get(pk=pk)
	context = {
		'post': post,
	}
	return render(request, 'insta_app/post_detail.html', context)