from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.utils.translation import gettext_lazy as _
from .managers import UserManager
from django.contrib.auth.models import PermissionsMixin

class Role(models.Model):
    name =  models.CharField(max_length=100)
    def __str__(self):   
        return self.name
    
class CustomUser(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    role  = models.ForeignKey(Role,on_delete=models.CASCADE,blank=True,null=True)
    is_active = models.BooleanField(_('active'), default=True)
    is_staff = models.BooleanField(_('staff'), default=False)
    is_superuser = models.BooleanField(_('superuser'), default=False)
    
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email
    
    def save(self, *args, **kwargs):       
        role,flag = Role.objects.get_or_create(name='Viewer')
        self.role = role      
        super(CustomUser, self).save(*args, **kwargs)


    