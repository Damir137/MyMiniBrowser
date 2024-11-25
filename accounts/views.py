from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm
from django.http import JsonResponse
from django.shortcuts import render

class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('login')
   

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

class ProtectedView(LoginRequiredMixin, TemplateView):
    template_name = 'protected.html'


def home(request):
    return render(request, 'index.html')

def allgames(request):
    return render(request, 'allgames.html')

def tictaktoe(request):
    return render(request, 'game.html')

def flappybird(request):
    return render(request, 'flappybird.html')

def pong(request):
    return render(request, 'pong.html')

def snake(request):
    return render(request, 'snake.html')

def typing(request):
    return render(request, 'typing.html')

def rpc(request):
    return render(request, 'rpc.html')

def timer(request):
    return render(request, 'timer.html')

def note(request):
    return render(request, 'notes.html')

def calc(request):
    return render(request, 'calculator.html')

 
def ponk(request):
    return JsonResponse({"message": "ponk"})





