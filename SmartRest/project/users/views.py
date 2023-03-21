from django.shortcuts import render
from djangp.contrib.auth.forms import UserCreationForm



# Create your views here.
def register(request):
    form = UserCreationForm()
    return render(request, 'users/register.html', {'form' : form })


    



