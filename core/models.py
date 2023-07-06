from django.db import models
from django.contrib.auth.models import AbstractUser
# Keeping all user related information in one model removes the need for additional or more complex database queries to retrieve related models.
# On the other hand, it may be more suitable to store app-specific user information in a model that has a relation with your custom user model

# Create your models here.
class User(AbstractUser):
    is_admin=models.BooleanField('Is admin',default=False)
    is_customer=models.BooleanField('Is customer',default=False)
    is_driver=models.BooleanField('Is driver',default=False)

