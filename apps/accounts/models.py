from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from rest_framework_simplejwt.tokens import RefreshToken
from django.utils.safestring import mark_safe
from config import settings


class AccountManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if username is None:
            raise TypeError('Phone did not come')
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        if not username:
            raise TypeError('Password did not come')
        user = self.create_user(username, password, **extra_fields)
        user.is_superuser = True
        user.is_staff = True
        user.is_sponsor = True
        user.is_active = True
        user.save(using=self._db)
        return user


GENDER = (
    (0, "None"),
    (1, "Male"),
    (2, "Female"),
)


class Account(AbstractBaseUser, PermissionsMixin):
    class Meta:
        verbose_name = 'Account'
        verbose_name_plural = 'Accounts'
    username = models.CharField(max_length=50, unique=True, verbose_name='Username', db_index=True)
    phone = models.CharField(max_length=16, verbose_name='Phone Number', null=True)
    gender = models.IntegerField(choices=GENDER, default=0, verbose_name="Jinsi")
    full_name = models.CharField(max_length=50, verbose_name='Full name', null=True)
    image = models.ImageField(upload_to='accounts/', verbose_name='Account image', null=True, blank=True)
    is_superuser = models.BooleanField(default=False, verbose_name="Superuser")
    is_staff = models.BooleanField(default=False, verbose_name="Admin")
    is_physical_person = models.BooleanField(default=False, verbose_name="Jismoniy shaxs")
    is_legal_entity = models.BooleanField(default=False, verbose_name="Yuridik shaxs")
    is_sponsor = models.BooleanField(default=False, verbose_name="Sponsor")
    is_student = models.BooleanField(default=False, verbose_name="Student")
    is_active = models.BooleanField(default=True)
    date_login = models.DateTimeField(auto_now=True, verbose_name='Yangilangan sanasi')
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Yaratilgan sanasi')

    objects = AccountManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self):
        if self.full_name:
            return f'{self.full_name} ({self.username})'
        return f'{self.username}'

    def image_tag(self):
        if self.image:
            return mark_safe(f'<a href="{self.image.url}"><img src="{self.image.url}" style="height:40px;"/></a>')
        return 'no_image'

    @property
    def get_physical_person_count(self):
        user = Account.objects.filter(is_physical_person=True).count()
        return user

    @property
    def get_legal_entity_count(self):
        user = Account.objects.filter(is_legal_entity=True).count()
        return user

    def get_student_count(self):
        user = Account.objects.filter(is_student=True).count()
        return user

    @property
    def image_url(self):
        if self.image:
            if settings.DEBUG:
                return f'{settings.LOCAL_BASE_URL}{self.image.url}'
            return f'{settings.PROD_BASE_URL}{self.image.url}'
        else:
            return None

    @property
    def tokens(self):
        refresh = RefreshToken.for_user(self)
        data = {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }
        return data
