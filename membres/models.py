from django.db import models

class Emprunteur(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField()

    class Meta:
        db_table = 'bibliotheque_emptrunteur'
    def __str__(self):
        return self.nom
# Create your models here.
