from django.urls import path

from app.decorators import guest
from borrowers import views

app_name = 'borrowers'

urlpatterns = [
    path('login/', guest(views.LoginView.as_view()), name='login')
]
