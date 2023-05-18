from django.shortcuts import render
from django.views import View
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Form
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

@login_required
class HomePageView(TemplateView):
    template_name = 'home.html'


class HomePageView(LoginRequiredMixin, TemplateView):
    template_name = 'login.html'
    login_url = '/accounts/login/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


class HomePageView(View):
    def get(self, request):
        return render(request, 'home.html')

class FormView(View):
    def get(self, request):
        return render(request, 'form.html')

    def post(self, request):
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        form = Form(name=name, email=email, message=message)
        form.save()
        return HttpResponseRedirect(reverse('home'))
    
class MessagesView(View):
    def get(self, request):
        messages = Form.objects.all()
        return render(request, 'messages.html', {'messages': messages})


def messages_view(request):
    forms = Form.objects.all()
    return render(request, 'messages.html', {'forms': forms})
