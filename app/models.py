from django.db import models

# Create your models here.
class Game(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100, blank=True, null = True)
    GENRES = (
            ('1' , 'Plataforma'),
            ('2' , 'Top-Down'),
            ('3' , 'Corrida'),
            ('4' , 'RPG'),
            ('5' , 'Outro'),
        )
    genre = models.CharField(max_length=20,  choices = GENRES)
    description = models.TextField()
    image = models.ImageField() 
