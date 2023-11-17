from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('services/',views.services,name='services_without_section'),
    path('services/<str:seccion>/',views.services,name='services_with_section')
]