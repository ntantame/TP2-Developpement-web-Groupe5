from django.db import models
from membres.models import Emprunteur

# creation de la classe Auteur
class Auteur(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    date_naissance= models.DateField()
    def __str__(self):
        return self.nom

# exo7: creation de la classe FicheAuteur
class FicheAuteur(models.Model):
    auteur=models.OneToOneField(Auteur,on_delete=models.CASCADE)
    biographie = models.TextField()
    site_web=models.URLField(blank=True, null=True)
    # La FicheAuteur permet de separer les informations complementaires
    # de l'auteur des informations principales. Elle peut être cree
    # uniquement lorsque ces informations sont nécessaires.

    def __str__(self):
        return f"Fiche de {self.auteur}"

# exo5: creation de la classe genre
class Genre(models.Model):
    nom = models.CharField(max_length=100)
    class Meta:
        verbose_name_plural = "Genres"
    def __str__(self):
        return self.nom

# exo6: creation de la classe Emprunteur




# creation de la classe Livre
class Livre(models.Model):
    titre = models.CharField(max_length=100)
    isbn = models.CharField(max_length=100, primary_key=True)
    nbre_page=models.PositiveIntegerField()
    # exercice 2: option commune
    # car le resume est optionnel et donc ce n'est pas oblige d'etre renseigne
    resume=models.TextField( blank=True, null=True)
    # elle peut être laissee vide lors de la création si elle est inconnue.
    langue=models.CharField(max_length=100,
                            choices=[('fr','Francais'), ('en','English'),('esp','Spanish')],blank=True,null=True)
    # la date peut rester inconnu donc oblige d'etre renseigne
    date_publication=models.DateField(blank=True, null=True)

    #exo4: ajout d'une cle etrangere
    auteur=models.ForeignKey(Auteur, on_delete=models.CASCADE,blank=True,null=True)
    genre=models.ManyToManyField(Genre)
    emprunteurs=models.ManyToManyField(Emprunteur, through='Emprunt')

    #exo9: ajout de __str__
    def __str__(self):
        return self.titre
    @property
    def est_disponible(self):
        return not self.emprunt_set.filter(
            date_retour_effective__isnull=True).exists()

    # exo10: ajout de la methode save():
    def save(self, *args, **kwargs):
        self.titre=self.titre.title()
        super().save(*args,**kwargs)


    #exo8: ajout de la classe Meta
    class Meta:
        ordering=['titre']

# creation de Emprunt
class Emprunt(models.Model):
    emprunteur=models.ForeignKey(Emprunteur, on_delete=models.CASCADE)
    livre=models.ForeignKey(Livre, on_delete=models.CASCADE)
    date_emprunt=models.DateField()
    date_retour_prevue=models.DateField()
    date_retour_effective=models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.emprunteur}-{self.livre}"

# Create your models here.
