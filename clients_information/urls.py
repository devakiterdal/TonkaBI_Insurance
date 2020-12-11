from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.clients_form, name="clients_form"),
    path('<int:id>/', views.clients_form, name="clients_form_edit"),
    path('delete/<int:id>/', views.clients_delete, name="clients_form_delete"),
    path('clients_summary', views.clients_summary, name="clients_summary"),
    path('getpdf/<int:id>', views.getpdf, name="getpdf"),
    
]
