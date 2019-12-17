# -*- coding: utf-8 -*-

from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profiles', unique=True, )

    class Meta:
        verbose_name = "profile"
        verbose_name_plural = "profiles"

    def __str__(self):
        return f'{self.user}'


class Variant(models.Model):
    number_of_variants = models.IntegerField()

    class Meta:
        verbose_name = "variant"
        verbose_name_plural = "variants"


class Test(models.Model):
    theme_of_test = models.CharField(max_length=30)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='tests', )
    variant = models.ForeignKey(to=Variant, on_delete=models.CASCADE, related_name='tests', null=True)

    class Meta:
        verbose_name = "test"
        verbose_name_plural = "tests"

    def __str__(self):
        return f'{self.theme_of_test}'


class Tag(models.Model):
    name_tag = models.CharField(max_length=30)
    

    class Meta:
        verbose_name = "tag"
        verbose_name_plural = "tags"

    def __str__(self):
        return f'{self.name_tag}'


class Task(models.Model):
    question = models.CharField(max_length=200)
    answer = models.CharField(max_length=200)
    img = models.ImageField(blank=True, null=True)
    variant = models.ForeignKey(to=Variant, on_delete=models.CASCADE, related_name='tasks', null=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='tasks', default=1)
    tag = models.ManyToManyField(to=Tag, related_name='tasks')

    class Meta:
        verbose_name = "task"
        verbose_name_plural = "tasks"

    def __str__(self):
        return f'{self.question}'


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


post_save.connect(create_user_profile, sender=settings.AUTH_USER_MODEL)
