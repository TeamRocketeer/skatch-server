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

