from django.urls import path, register_converter
from django.views.generic import DetailView

from . import views
from .converter import ISBNPersnnoliseConverter
from .views import ListeLivreView, ListeLivresView, DetailLivreView

register_converter(ISBNPersnnoliseConverter, 'isbn')

urlpatterns = [
   # exercice1: ajout du motif "livre/"
   # path("livre/", views.liste_livres),

    # exercice 2: ajout du motif "livre/<str:isbn>/"
    # path("livres/<str:isbn>", views.detail_livre),

    # exercice 5: nomage des motifs : changement de livre a ouvrage
    # path("ouvrages/", views.liste_livres, name="liste-livres"),
    # path("ouvrages/<str:isbn>/", views.detail_livre, name="detail-livre"),
    # exercice 6: personnalisation du isbn
    # path("livres/<isbn:isbn>/", views.detail_livre, name="detail-livre"),
    # exercice 9: ajout de la route ajouter
    path("livres/ajouter/", views.ajouter_livre, name="ajouter-livre"),
    # exercice 10: ajout de la route json
    path("livres/json/", views.livres_json, name="livres-json"),

    # exercice 12 : route pour CBV
    # path("livres/", ListeLivreView.as_view(), name="liste-livre"),

    # exerice 13: route pour ListeView
     path("livres/", ListeLivresView.as_view(), name="liste-livre"),

    # exercice 15 ajout du motif genre
    path("livres/genre/<str:nom>/", views.GenreLivreView.as_view(), name="livres-par-genre"),

    # exerice 17: ajout de la route DetailView
    path("livres/<isbn:isbn>/", DetailLivreView.as_view(), name="detail-livre"),

    # exercice 25:
    path("livre_genre/<str:nom>/", views.liste_livre_genre, name="livres-genre"),
]


"""
    exercice 3:
    La page /livres/nouveautes/ n'affichera jamais ce qu'on attend parce que le premier path 'livre/isbn/ est egalement une 
    chaine de caractere , du coup elle correspond a l'url demandee et vu qu'il est place en tete de liste et que l'ordre est 
    important il va s'arreter la et appeler la vue detail_livre, donc il ne va jamais examiner 'livre/nouveautes/'.
    pour la corriger il suffit d'inverser l'ordre c'est a dire placer 'livre/nouveautes/' en tete de liste pour que django 
    puisse appeler la vue nouveautes. donc:
    urlpatterns = [
            path("livres/nouveautes/", views.nouveautes, name="nouveautes"),
            path("livres/<str:isbn>/", views.detail_livre, name="detail-livre"),
        ]    
"""
