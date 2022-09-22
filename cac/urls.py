from django.urls import path
from cac import views

urlpatterns = [
    path('hola_mundo',views.hola_mundo),
]