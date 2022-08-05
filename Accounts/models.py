from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)
from django.db.models.base import Model

# Create your models here.
class UserProfileManager(BaseUserManager):
    def create_user(self,name, email,username, password=None):
        if not email:
            raise ValueError("User must have email!")

        email = self.normalize_email(email)
        user = self.model(name=name,email=email,username=username)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self,name, email,username, password):
        user = self.create_user(name, email,username, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=255,default="",null=False)
    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=50,default="",null=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name","username"]
    
    
    def __str__(self):
        return self.email


# Image upload function

def upload_profile_image(instance, filename):
    return "uploads/{user}/{filename}".format(user=instance.user, filename=filename)

class profileInfo(models.Model):
    user = models.OneToOneField(UserProfile,on_delete=models.CASCADE,primary_key=True)
    image = models.ImageField(upload_to = upload_profile_image, null = True, blank = True)
    dateOfBirth = models.DateField()
    sex = models.CharField(max_length=10,default="",null=False)
    height = models.IntegerField(blank=False,null=False,default=0)
    weight = models.IntegerField(blank=False,null=False,default=0)
    religion = models.CharField(max_length=50,default="",null = False)
    profession = models.CharField(max_length=200,default="", null=False)
    workplace = models.CharField(max_length=100,default="",null=False)

    marital_status = models.CharField(max_length=50,default="",null=False)
    present_address_district = models.CharField(max_length=100,default="",null=False)
    present_address_division = models.CharField(max_length=100,default="",null=False)
    permanent_address_district = models.CharField(max_length=100,default="",null=False)
    permanent_address_division = models.CharField(max_length=100,default="",null=False)
    skin_tone = models.CharField(max_length=100,default="",null=False)
    blood_group = models.CharField(max_length=100,default="",null=False)
    yearly_income = models.CharField(max_length=100,default="",null=False)
    educational_qualification = models.CharField(max_length=300,default="",null=False)
    coins = models.IntegerField(blank=False,null=False,default=0)
    bio = models.TextField(blank=True)


    def __str__(self):
        return  f'{self.user.username} profile'


class matching(models.Model):
    who = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    toWhom = models.IntegerField(blank=False, null=False)
    name = models.CharField(max_length=200,default="",null=False)

    

