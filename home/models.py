# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Pet(models.Model):

    #__Pet_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    weight = models.CharField(max_length=255, null=True, blank=True)
    unit = models.CharField(max_length=255, null=True, blank=True)
    gender = models.IntegerField(null=True, blank=True)
    breed = models.IntegerField(null=True, blank=True)
    species = models.IntegerField(null=True, blank=True)

    #__Pet_FIELDS__END

    class Meta:
        verbose_name        = _("Pet")
        verbose_name_plural = _("Pet")



#__MODELS__END
