from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Post(models.Model):
	image = models.ImageField(upload_to='posts', null=True)
	title = models.CharField(max_length=250)
	description = models.TextField()
	uploaded_on = models.DateTimeField(default=timezone.now())
	user = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.title

class Profile(models.Model):
	bio = models.TextField(null=True, blank=True)
	image = models.ImageField(upload_to='profile', null=True)
	# post = models.ForeignKey(Post, on_delete=models.CASCADE)
	user = models.OneToOneField(User, on_delete=models.CASCADE)

	@receiver(post_save, sender=User)
	def create_user_profile(sender, instance, created, **kwargs):
		if created:
			Profile.objects.create(user=instance)

	@receiver(post_save, sender=User)
	def save_user_profile(sender, instance, **kwargs):
		instance.profile.save()