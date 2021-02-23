from django.db import models
from django.contrib.auth.models import AbstractUser

from django.utils.translation import ugettext_lazy as _

from django_countries.fields import CountryField

class OIAUserProfile(models.Model):
    """
    Class implements user's profile, contains basic information such as age and country
    """

    user = models.OneToOneField('OIAUser', on_delete=models.CASCADE, related_name='profile', verbose_name='profile')

    country = CountryField(default=None, null=True, verbose_name="country")
    age = models.IntegerField(default=None, null=True, verbose_name='age')

    AT_STUDENT = 'student'
    AT_TEACHER = 'teacher'
    AT_CHOICES = (
        (AT_STUDENT, _('Student')),
        (AT_TEACHER, _('Teacher'))
    )
    account_type = models.CharField(default=AT_STUDENT, choices=AT_CHOICES, max_length=16)

class OIAUser(AbstractUser):
    """
    Extend the AbstractUser class with special method for getting
    user's profile.
    """

    def get_profile(self):
        """
        Safe method to get user's profile. Creates it if it doesn't exist.
        """

        profile = self.profile
        if profile is None:
            profile = OIAUserProfile(user=self)
            profile.save()

        return profile
