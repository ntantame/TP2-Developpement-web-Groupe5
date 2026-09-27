from django.core.exceptions import MiddlewareNotUsed

# exercice 19: creation du midlleware affichant la methode et le chemin
# choix d'ecriture: classe
class MiddlewareMethodPath:
    # contructeur
    def __init__(self, get_response):
        self.get_response = get_response
    # methode call
    def __call__(self, request):
        # exo21: ajout du print
        print("method-path initiale")
        print(request.method, request.path)
        response = self.get_response(request)
        print("method-path finale")
        return response

# exercice 20: creation du middleware qui calcule le temps pris par la vue
import time
class MiddlewareTempsTraitement:
    def __init__(self, get_response):
        self.get_response = get_response
    def __call__(self, request):
        # exo21
        print("temps traitement initiale")
        heure_debut=time.time()
        response = self.get_response(request)
        heure_fin=time.time()
        temps=(heure_fin-heure_debut)*1000
        print(f"Temps totale de reponse: {temps} ms")
        print("temps traitement finale")
        return response

# exercice 22: Middleware pour cour-circuiter
# importation de la reponse http
from django.http import HttpResponse
from django.conf import settings
# creation de la classe
class MiddlewareAutorisation:
    def __init__(self, get_response):
        self.get_response = get_response
        if not hasattr(settings, 'AUTORISATION_ACTIVEE'):
            raise MiddlewareNotUsed
    def __call__(self, request):
        if request.path=="/bibliotheque/livres/":
            autorisation=request.headers.get("X-Client-Autorise")
            if not autorisation:
                return HttpResponse("Access Denied", status=403)

        response = self.get_response(request)
        return response


# exercice 25 : ajout de la classe de verification jeton
class MiddlewareVerification:
    def __init__(self, get_response):
        self.get_response = get_response
    def __call__(self, request):
        # verification sur la route livre par genre:
        if request.path.startswith("/bibliotheque/livres/genre/"):
            jeton=request.headers.get("X-Client-Jeton")
            if not jeton:
                return HttpResponse("Access Denied", status=403)
        return self.get_response(request)