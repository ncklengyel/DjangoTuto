from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    description = models.CharField(max_length=100, default='')
    city = models.CharField(max_length=100, default='')
    website = models.URLField(default='')
    phone = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username

    def create_profile(sender, **kwargs):
        if kwargs['created']:
            user_profile = UserProfile.objects.create(user=kwargs['instance'])

    post_save.connect(create_profile, sender=User)


class PreposeResidentielProfile(models.Model):
    user = models.OneToOneField(User)
    prep_type = models.CharField(max_length=100, default='prep_residentiel')

    class Meta:
        permissions = (
            ('view_clients_affaire', 'view_clients_affaire'),
            ('view_clients_residentiel', 'view_clients_residentiel'),
        )

    def __str__(self):
        return self.user.username

    #source: https://simpleisbetterthancomplex.com/tutorial/2016/11/23/how-to-add-user-profile-to-django-admin.html
    #@receiver(post_save, sender=User)
    def create_or_update_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
        post_save.connect(create_profile, sender=User)


class PreposeAffaireProfile(models.Model):
    user = models.OneToOneField(User)
    prep_type = models.CharField(max_length=100, default='prep_affaire')

    def __str__(self):  # __unicode__ for Python 2
        return self.user.username

    #source: https://simpleisbetterthancomplex.com/tutorial/2016/11/23/how-to-add-user-profile-to-django-admin.html
    #@receiver(post_save, sender=User)
    def create_or_update_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
        post_save.connect(create_profile, sender=User)


class ClientResidentiel(models.Model):
    first_name = models.CharField(max_length=100, default='')
    last_name = models.CharField(max_length=100, default='')
    email = models.CharField(max_length=100, default='')


    def __str__(self):  # __unicode__ for Python 2
        return self.email

class ClientAffaire(models.Model):
    first_name = models.CharField(max_length=100, default='')
    last_name = models.CharField(max_length=100, default='')
    email = models.CharField(max_length=100, default='')

    def __str__(self):  # __unicode__ for Python 2
        return self.email
