from django.urls import path

from app.decorators import guest
from borrowers import views

app_name = 'borrowers'

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login')
]
