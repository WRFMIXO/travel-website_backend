from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class CustomUser(AbstractUser):

    SEX_CHOICES = [
        ("H", "Homme"),
        ("F", "Femme"),
        ("A", "Autre"),
    ]

    ID_TYPES_CHOICES = [
        ("CNI", "Carte Nationale d'Identité"),
        ("PASSPORT", "Passeport"),
        ("VISA", "Carte de visa"),
    ]

    # Champs supplémentaires
    contact = models.CharField(max_length=30, null=True, blank=True)
    address = models.TextField()
    birth_date = models.DateField(null=True, blank=True)
    old = models.IntegerField(default=0)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES)
    birth_place = models.CharField(max_length=200)
    is_connected = models.BooleanField(default=False)
    id_type = models.CharField(max_length=200, blank=True, null=True, choices=ID_TYPES_CHOICES, default='CNI')
    id_number = models.CharField(max_length=200, null=True, blank=True)
    photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)  # Champ pour la photo de profil
    pass