from django.db import models
from utilisateurs.models import CustomUser

# Create your models here.
class VisaRequests(models.Model):

    code = models.CharField(max_length=30)
    creation_date = models.DateField(auto_now_add=True)
    reason = models.TextField()
    userConcerned = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='utilisateur')
    country = models.CharField(max_length=255)
    university = models.CharField(max_length=255)
    city = models.CharField(max_length=255)