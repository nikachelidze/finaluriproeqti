from multiprocessing import context
from django.shortcuts import render,redirect
from django.http import HttpRequest, HttpResponse 
from django.views import View
from users.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from users.models import car

# Create your views here.

def home_viwe(request: HttpRequest) -> HttpResponse:
    return render(request, 'index.html')

def mtavari_viwe(request: HttpRequest) -> HttpResponse:
    return render(request, 'mtavari.html', context={
        'cars': car.objects.all()
    })

class Register(View):
    template_name = 'registration/registracia.html'

    def get(self, request):
        context = {
            'form': UserCreationForm()
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            # login(request, user)
            return redirect('home')
        context ={
            'form': form
        }
        return render(request, self.template_name, context)
