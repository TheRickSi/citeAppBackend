from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.mail import send_mail
from django.contrib.auth.models import UserManager
from cites.models import Cite
# Create your models here.

class Member(AbstractBaseUser,PermissionsMixin):
    password = models.CharField(max_length=100)
    name = models.CharField(max_length=70)
    date_joined = models.DateField(auto_now=True)
    username_validator = UnicodeUsernameValidator
    username = models.CharField(
        ('username'),
        max_length=150,
        unique=True,
        help_text=('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
        error_messages={
            'unique': ("A user with that username already exists."),
        },
        primary_key=True,
    )
    email = models.EmailField(('email address'), blank=True)
    is_staff = models.BooleanField(
        ('staff status'),
        default=False,
        help_text=('Designates whether the user can log into this admin site.'),
    )
    favcite = models.ForeignKey(Cite,related_name='users',on_delete=models.CASCADE,null= True)
    objects = UserManager()
    USERNAME_FIELD = 'username'
    class Meta:
        verbose_name_plural = "Members"

    def __str__(self):
        return f"{self.username}"

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)
        
    def save(self, *args, **kwargs):
        super(Member, self).save(*args, **kwargs)

    