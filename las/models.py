from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
# Create your models here.

# class User(AbstractBaseUser, PermissionsMixin):
#   first_name = models.CharField(_('first name'), max_length=30, blank=True)
#   last_name = models.CharField(_('last name'), max_length=30, blank=True)
#   username = models.CharField(_('last name'), max_length=30, blank=True)
#   is_active = models.BooleanField(_('active'), default=True)
#   avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)

#   objects = UserManager()

#   USERNAME_FIELD = 'email'
#   REQUIRED_FIELDS = []

#   class Meta:
#     verbose_name = _('user')
#     verbose_name_plural = _('users')