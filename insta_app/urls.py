from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='home'),
	path('signup/', views.signup, name='signup'),
	path('signin/', views.signin, name='signin'),
	path('profile/', views.user_profile, name='profile'),
	path('posts/', views.post_view, name='posts'),
	path('<int:pk>', views.post_detail, name='post_detail'),
]