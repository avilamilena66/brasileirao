"""glicmed URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from tasks import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('sair/', views.sair, name='sair'),
    path('userpage/', views.userpage, name='userpage'),
    path('admin/', views.admin, name='admin'),
    path('profile/', views.profile, name='profile'),
    path('editprofile/', views.editprofile, name='editprofile'),
    # Histórico
    path('historico/', views.historico, name='historico'),
    #Insulina
    path('insulina/', views.insulina, name='insulina'),
    path('insulina/list/', views.insulina_list, name='insulina_list'),
    path('insulina/editar/<int:insulina_id>/', views.editar_insulina, name='editar_insulina'),
    path('insulina/excluir/<int:insulina_id>/', views.excluir_insulina, name='excluir_insulina'),
    path('editar_insulina/<int:insulina_id>/', views.editar_insulina, name='editar_insulina'),
    #Glicose
    path('glicose/', views.glicose, name='glicose'),
    path('glicose/list/', views.glicose_list, name='glicose_list'),
    path('glicose/editar/<int:glicose_id>/', views.editar_glicose, name='editar_glicose'),
    path('glicose/excluir/<int:glicose_id>/', views.excluir_glicose, name='excluir_glicose'),
    path('editar_glicose/<int:glicose_id>/', views.editar_glicose, name='editar_glicose'),
    #Refeição
    path('meal/', views.meal, name='meal'),
    path('meal/list/', views.meal_list, name='meal_list'),
    path('meal/editar/<int:meal_id>/', views.editar_meal, name='editar_meal'),
    path('meal/excluir/<int:meal_id>/', views.excluir_meal, name='excluir_meal'),
    path('editar_meal/<int:meal_id>/', views.editar_meal, name='editar_meal'),
    # Atividade Física
    path('atividade_fisica/', views.atividade_fisica, name='atividade_fisica'),
    path('atividade_fisica/list/', views.atividade_fisica_list, name='atividade_fisica_list'),
    path('atividade_fisica/editar/<int:atividade_id>/', views.editar_atividade, name='editar_atividade'),
    path('atividade_fisica/excluir/<int:atividade_id>/', views.excluir_atividade, name='excluir_atividade'),
    path('editar_atividade/<int:atividade_id>/', views.editar_atividade, name='editar_atividade'),
]
