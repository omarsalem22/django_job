
from tokenize import blank_re
from django.contrib.auth.models import User
from django.db import models
from PIL import Image
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User , on_delete=models.CASCADE)
    city=models.ForeignKey('City',related_name='user_city',on_delete=models.CASCADE,null=True,blank=True)
   
    phone_number=models.CharField(max_length=15)
    image=models.ImageField( upload_to='profile/',null=True)
    def __str__(self) :
        return f'{self.user.username} Profile'
    # def save(self ,*args,**kwargs):
    #     super(Profile,self).save(*args, **kwargs)  
    #     img=Image.open(self.image.path)
    #     if img.height > 300 or img.width > 300:
    #         outputsize=(300,300)
    #         img.thumbnail(outputsize)
    #         img.save(self.image.path)
@receiver(post_save,sender=User)
def Create_user_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)


class City(models.Model):
  name=  models.CharField( max_length=50)

  def __str__(self) :
        return f'{self.name} City  '