from django.shortcuts import render
from .models import Commande
# Create your views here.


def home(request):
    context = {
        'commandes': Commande.objects.all()
    }
    return render(request, 'SmartRest/home.html')


def commande(request):
    return render(request, 'SmartRest/cmd.html')



def login(request):
    return render(request, 'SmartRest/login.html')


