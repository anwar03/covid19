from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, UserManager
from django.core.mail import send_mail
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from base.constants import ENGLISH, PREFERRED_LANGUAGE, TIMEZONE_CHOICES


class UserManagerEx(UserManager):

    def _create_user(self, username, email, password, **extra_fields):
        if not username:
            raise ValueError('The given username must be set')
        username = self.model.normalize_username(username)
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email=None, password=None, **extra_fields):
        return super(UserManagerEx, self).create_user(username, email, password, **extra_fields)

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        return super(UserManagerEx, self).create_superuser(username, email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    username = models.EmailField(verbose_name=_('username'), max_length=100, unique=True)
    first_name = models.CharField(verbose_name=_('first name'), max_length=100, null=True, blank=True)
    last_name = models.CharField(verbose_name=_('last name'), max_length=100, null=True, blank=True)
    image = models.ImageField(verbose_name=_('image'), upload_to='user/', null=True, blank=True)
    contact = models.ForeignKey('contact.Contact', verbose_name=_('contact'), related_name='users',
                                on_delete=models.SET_NULL, null=True, blank=True)
    is_staff = models.BooleanField(verbose_name=_('staff status'), default=False)
    is_active = models.BooleanField(verbose_name=_('active'), default=True)
    date_joined = models.DateTimeField(verbose_name=_('date joined'), default=timezone.now)
    language = models.CharField(verbose_name=_('language'), max_length=3, choices=PREFERRED_LANGUAGE, default=ENGLISH)
    timezone = models.CharField(verbose_name=_('timezone'), max_length=100, choices=TIMEZONE_CHOICES,
                                default='Asia/Dhaka')

    objects = UserManagerEx()

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'contact__email'

    def get_full_name(self):
        full_name = (self.first_name if self.first_name else '') + ' ' + (self.last_name if self.last_name else '')
        return full_name.strip()

    def get_short_name(self):
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        if self.contact and self.contact.email:
            send_mail(subject, message, from_email, [self.contact.email], **kwargs)
