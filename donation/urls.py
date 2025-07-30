from django.urls import path
from .views import DonorRegisterView, CustomLoginView,dashboard,donate,DonorListView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('register/', DonorRegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('dashboard/', dashboard, name='dashboard'),
    path('donate/', donate, name='donate'),
    path('donor_list/', DonorListView.as_view(), name='donor_list'),
]
