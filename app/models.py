from django.db import models
from django.contrib.auth.models import User

def upload_image_game(instance, filename):
    return f"{instance.id}-{filename}"


# Create your models here.
class Game(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100, blank=True, null = True)
    developer = models.ForeignKey(User, on_delete=models.CASCADE)
    GENRES = (
            ('1' , 'Plataforma'),
            ('2' , 'Top-Down'),
            ('3' , 'Corrida'),
            ('4' , 'RPG'),
            ('5' , 'Outro'),
        )
    genre = models.CharField(max_length=20,  choices = GENRES)
    description = models.TextField(blank=True, null = True)
    image = models.ImageField(upload_to=upload_image_game, blank=True, null=True) 
    link = models.URLField(max_length=100)


