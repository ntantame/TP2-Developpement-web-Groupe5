from django.urls import reverse
from .models import Livre
from django.http import HttpResponse, Http404, JsonResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from django.views.generic import ListView, DetailView


# exercice 5: contruction du lien de chaque livre avec la methode reverse
"""
def liste_livres(request):
    return  HttpResponse(
        reverse('liste-livres')
    )

def detail_livre(request, isbn):
    return HttpResponse(
        reverse('detail-livre', args=(isbn,))
    )
"""
# exercice 7: fonction qui renvoie la liste des livres
def liste_livres(request):
    livres = Livre.objects.all()
    html="<h1>Liste de livres</h1></ul>"
    for livre in livres:
        html+=f"<li> {livre.titre} </li>"
    html+="</ul>"
    return HttpResponse(html)

# exercice 8: gestion de l'absence d'un livre
def detail_livre(request, isbn):
    try:
        livre = Livre.objects.get(isbn=isbn)
    except Livre.DoesNotExist:
        raise Http404("Livre n'existe pas")
    return HttpResponse(
        f"<p>titre du livre {livre.isbn}: {livre.titre}</p>"
    )

# exercice 9: ajout du livre renvoyant un message selon la methode
@csrf_exempt
def ajouter_livre(request):
    if request.method == "GET":
        return HttpResponse("affichage du formulaire d'ajout")
    elif request.method == "POST":
        return HttpResponse("Traitement du formulaire d'ajout")

# exercice 10: vue liste.json
def livres_json(request):
    livres = Livre.objects.all()
    dataLivre=[]
    for livre in livres:
        dataLivre.append({
            "titre": livre.titre,
            "isbn": livre.isbn,
        })
    return JsonResponse(dataLivre, safe=False)

# exercice 12: reecriture de liste_livre
class ListeLivreView(View):
    def get(self, request):
        livres = Livre.objects.all()
        html="<h1>Liste de livres</h1></ul>"
        for livre in livres:
            html+=f"<li> {livre.titre} </li>"
        html+="</ul>"
        return HttpResponse(html)

# exercice 13: utilisation de ListeView
class ListeLivresView(ListView):
        model=Livre
        # exercice 14: personalisation d la vue generique
        context_object_name="livres"
        queryset=Livre.objects.order_by('titre')
        # exercice 22
        print("execution de la vue liste_livres")


# exercice 15 : vue pour le genre livre
class GenreLivreView(ListView):
    model=Livre
    context_object_name="livres"

    # redefiniton du get_queryset
    def get_queryset(self):
        nom_genre=self.kwargs["nom"]
        return  Livre.objects.filter(genre__nom=nom_genre)

    # exercice 16: redefinition du get_context_data
    def get_context_data(self, **kwargs):
        context = super(GenreLivreView, self).get_context_data(**kwargs)
        context["total_livres"]= self.get_queryset().count()
        return context

# exercice 17: reecriture de detail_livre avec DetailView
class DetailLivreView(DetailView):
    model = Livre
    slug_url_kwarg = "isbn"
    slug_field="isbn"
    template_name="bibliotheque/livre_detail.html"
    context_object_name="livre"

# exercice 25: lien vers la page avec reverse:
def liste_livre_genre(request,nom):

    url_genre = reverse("livres-par-genre",kwargs={"nom": nom})
    return HttpResponse(
        f'<a href="{url_genre}">Voir les livres de {nom}</a>'
    )


"""
reponse a l'exercice 17: Avec DetailView, la gestion du livre introuvable n'est plus de notre responsabilite, 
car Django renvoie automatiquement une erreur 404 si l'objet n'existe pas.
"""

"""
Pour le projet bibliothèque, je prefererais une vue fonction lorsque la logique est spécifique et nécessite beaucoup 
de personnalisation, par exemple pour ajouter un livre en distinguant le traitement d’une requete GET et d’une requete POST.
A l’inverse, je préférerais une vue generique lorsque l’operation est classique et que Django peut faire 
le travail automatiquement, par exemple pour afficher les details d’un livre avec DetailView, 
ce qui permet une mise en œuvre plus rapide et gère automatiquement le cas ou le livre est introuvable.

"""





"""
exercice11
 def ajouter_commentaire(request):
if request.POST:
    # traitement du commentaire
    return HttpResponse("Commentaire ajoute")
return HttpResponse("Formulaire vide")
Ici le formulaire HTML envoye sans aucun champ rempli ne declenchera jamais le traitement attendu parceque que apres
verification de la condition request.POST cela renverra faux du coup l'instruction a l'interieur de la condition ne sera
jamais execute, bien que le formulaire ait ete envoye. pour le corriger il suffit d'ecrire comme ceci:
if request.method == "POST"::
    # traitement du commentaire
    return HttpResponse("Commentaire ajoute")
return HttpResponse("Formulaire vide")
"""