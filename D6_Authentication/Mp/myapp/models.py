from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserMoreInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    SocialMediaLink=models.URLField(blank=True)
    Profile_Picture=models.ImageField(upload_to='P_pic',blank=True)

    def __str__(self):
        return self.user.username
