from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from django.contrib.auth.models import User 
# Create your models here.


class preview(models.Model):
    title =  models.CharField(max_length=100)
    description =  models.CharField(max_length=500)
    Subject =  models.CharField(max_length=60,default="разное")
    text = models.TextField()
    image_id = models.IntegerField()
    date = models.DateTimeField(default=timezone.now) 
    time_read = models.IntegerField()
 
class Interesting(models.Model): 
    post_id = models.IntegerField(default=0)

class test(models.Model):
    title =  models.CharField(max_length=100)   
    image_id = models.IntegerField()    

class profile(models.Model):  
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    TARGET_CHOICES = (
        ('trening', 'Эктоморф, энергичный, худой, быстрый'),
        ('losing', 'Эндоморф, полный, широкий и медлительный'),
        ('maintenance', 'Мезоморф, достаточно мускулистый, средний')
    )
    GENDER_CHOICES = (
        ('male', 'Мужской'),
        ('female', 'Женский')
    )
    ACTIVITY_CHOICES = (
        ('minimal', 'Сидячий режим весь день'),
        ('low', 'Минимальная активность'),
        ('mid', 'Средняя активность'),
        ('high', 'Тяжелая работа и/или нагрузка'),
        ('very_high', 'Экстрим')
    )  
    target = models.CharField(
        max_length=50,
        choices=TARGET_CHOICES,
        verbose_name='Телосложение'
    )
    height = models.PositiveIntegerField(
        default=0,
        verbose_name='Рост'
    )
    weight = models.PositiveIntegerField(
        default=0,
        verbose_name='Вес'
    )
    steps = models.PositiveIntegerField(
        default=0,
        verbose_name='Шаги в день'
    )
    age = models.PositiveIntegerField(
        default=0,
        verbose_name='Возраст'
    )
    gender = models.CharField(
        max_length=50,
        choices=GENDER_CHOICES,
        verbose_name='Пол'
    )
    activity = models.CharField(
        max_length=50,
        choices=ACTIVITY_CHOICES,
        verbose_name='Активность'
    )
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs): 
        print("Saving profile")
        if instance.profile is not None:
            print("Save profile")
            instance.profile.save()
        else:  
            profile.objects.create(user=instance)
   
