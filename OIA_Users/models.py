from django.db import models
from django.contrib.auth.models import AbstractUser


class OIAUserProfile(models.Model):
    """
    Class implements user's profile, contains basic information such as age and country
    """

    user = models.OneToOneField('OIAUser', on_delete=models.CASCADE, related_name='profile', verbose_name='profile')

    """
        TODO
            Change to IntegerChoices to simplify declaring it as unspecified
    """
    age = models.IntegerField(default=-1, verbose_name='age')
    """
        TODO
            Change to TextChoices to simply declaring it as unspecified
    """
    country = models.CharField(max_length=64, verbose_name="country")


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
