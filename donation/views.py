# donation/views/auth_views.py
from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from .models import Donation
from django.shortcuts import redirect
from .forms import DonationForm
from django.views.generic import ListView

class DonorRegisterView(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'donation/register.html'
    success_url = reverse_lazy('login')

class CustomLoginView(LoginView):
    template_name = 'donation/login.html'
    success_url = reverse_lazy('dashboard')

def dashboard(request):
    return render(request, 'donation/dashboard.html')

# class Donate(CreateView):
#     model = Donation
#     fields = ['food_item', 'quantity', 'expiry_date']
#     template_name = 'donation/donate.html'
#     success_url = reverse_lazy('dashboard')

def donate(request):
    if request.method=='POST':
        form=DonationForm(request.POST)
        if form.is_valid():
            donation = form.save(commit=False)
            donation.donor = request.user
            donation.save()
            return redirect('dashboard')
    else:
        form = DonationForm()
    return render(request, 'donation/donate.html', {'form': form})  

class DonorListView(ListView):
    model = Donation
    template_name = 'donation/donor_list.html'
