from django.db import models
from django.contrib.auth.models import AbstractBaseUser

from user.managers import UserManager


class User(AbstractBaseUser):

    # User 모델의 필수 field
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    # 헬퍼 클래스 사용
    objects = UserManager()

    # 필수로 작성해야하는 field
    REQUIRED_FIELDS = ['username', 'password']

#
#
# class Profile(models.Model):
#         # related fields =====
#     user = models.OneToOneField('account.User', on_delete=models.CASCADE, related_name='profile')
#     # favorite_exercises = models.ManyToManyField('fitnessdiving.CourseCategory', related_name='profiles')
#
#     # required fields =====
#     phone = models.CharField(max_length=20, null=True)
#     name = models.CharField(max_length=10, null=True)
#     nickname = models.CharField(max_length=10, null=True)
#     # option fields =====
#     age_range = models.IntegerField(choices=AGE_RANGE, blank=True, null=True)
#     gender = models.IntegerField(choices=GENDER, blank=True, null=True, help_text='1: 여성 , 2: 남성')
#     avatar = models.ImageField(upload_to=profile_avatar_path, default='', blank=True, null=True)
#     one_line_intro = models.CharField(max_length=100, default='', blank=True, null=True)
#     birthday = models.DateField(blank=True, null=True)
