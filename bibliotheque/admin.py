from django.contrib import admin
from .models import  Auteur, Livre, Emprunt
from membres.models import Emprunteur
admin.site.register(Auteur)
admin.site.register(Livre)
admin.site.register(Emprunt)
admin.site.register(Emprunteur)

# Register your models here.
