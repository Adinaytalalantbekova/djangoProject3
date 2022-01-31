from django.db import models
from django.contrib.auth.models import User



ADMIN = 1
DOCTOR = 2
SINGER = 3
ACTOR = 4
COMEDIAN = 5
DANCER = 6
USER_TYPE =(
    (ADMIN, 'ADMIN'),
    (DOCTOR, 'DOCTOR'),
    (SINGER, 'SINGER'),
    (ACTOR, 'ACTOR'),
    (COMEDIAN, 'COMEDIAN'),
    (DANCER, 'DANCER')
)
MALE = 1
FEMALE = 2
OTHER = 3
GENDER_TYPE = (
    (MALE, 'MALE'),
    (FEMALE, "FEMALE"),
    (OTHER, 'OTHER')
)



class NewUser(User):
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
    user_type =models.IntegerField(choices=USER_TYPE,
                                   verbose_name="Тип Пользователя",
                                   default=ADMIN)
    phone_number = models.CharField('phone_number', max_length=100)
    age = models.IntegerField()
    gender = models.IntegerField(choices=GENDER_TYPE, verbose_name="Гендер")


