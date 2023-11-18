from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('services/',views.services,name='services_without_section'),
    path('services/<str:seccion>/',views.services,name='services_with_section'),
    path('drop_file/',views.drop,name='drop_files'),
    path('drop_file/<str:actividad>/',views.drop,name='drop_files_info'),
    path('mostrar_grafico/',views.show_grafico,name='show_grafico')
]