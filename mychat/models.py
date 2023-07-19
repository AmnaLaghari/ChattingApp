from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    pic = models.ImageField(upload_to="img", blank=True, null=True)
    friend = models.ManyToManyField("Friends", related_name='my_friends')

    def __str__(self) -> str:
        return self.name
    
class Friends(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.profile.name