from django.http import HttpResponse
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate, get_user_model
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from .forms import UserUpdateForm
from django.contrib.auth.models import Group
from django.shortcuts import render, get_object_or_404, redirect
from .models import Insulina
from .forms import InsulinaForm
from .models import Glicose
from .forms import GlicoseForm
from .models import Meal
from .forms import MealForm
from .models import AtividadeFisica
from .forms import AtividadeFisicaForm

#Métodos 

def home(request):
    return render(request, 'home.html')

def signup(request):

    if request.method == 'GET':

        return render(request, 'signup.html', {
            'form': UserCreationForm
        })

    else:
        if request.POST['password1'] == request.POST['password2']:

            try:

                user = User.objects.create_user(
                    first_name = request.POST['first_name'], username=request.POST['username'], password=request.POST['password1'])
                user.save()
                # Adicione o usuário ao grupo 'usuario' (ou ao grupo que você desejar)
                grupo_usuario = Group.objects.get(name='costumer')
                user.groups.add(grupo_usuario)
                login(request, user)

                return redirect('userpage')

            except:
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    "error": 'Usuário já existe'

                })

        return render(request, 'signup.html', {
            'form': UserCreationForm,
            "error": 'senhas são diferentes'

        })

def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(username=request.POST['username'], password=request.POST['password'])

        if user is None:
            return render(request, 'signin.html', {
                'form': AuthenticationForm,
                'error': 'Usuário ou senha está incorreto'
            })
        else:
            login(request, user)

            # Verificar o grupo do usuário
            if user.groups.filter(name='costumer').exists():
                return redirect('userpage')
            elif user.groups.filter(name='admin').exists():
                return redirect('admin')
            else:
                # Redirecionar para uma página padrão se não estiver em nenhum grupo específico
                return redirect('home')
            
@login_required
def sair(request):
    logout(request)
    return redirect('home')

@login_required
def admin(request):
    return render(request, 'admin.html')

@login_required
def userpage(request):
    if request.method == 'POST':
        if "profile" in request.POST:
            return redirect('profile')
        if "insulina" in request.POST:
            return redirect('insulina')
        if "glicose" in request.POST:
            return redirect('glicose')
        if "meal" in request.POST:
            return redirect('meal')
        if "historico" in request.POST:
            return redirect('historico')

    return render(request, 'userpage.html')

@login_required
def profile(request):
    if request.method == 'POST':
        if "update" in request.POST:
            return redirect('editprofile')
        if "delete" in request.POST:
            user_pk = request.user.pk
            logout(request)
            User = get_user_model()
            User.objects.filter(pk=user_pk).delete()
            return redirect('home')
        if "return" in request.POST:
            return redirect('userpage')
    else:
        return render(request, 'profile.html')

@login_required
def editprofile(request):
    if request.method == 'POST':
        if "return" in request.POST:
            return redirect('profile')
        if "confirm" in request.POST:
            if request.POST['password1'] == request.POST['password2']:
                try:
                    user = request.user
                    if request.POST['username'] != '':
                        user.username = request.POST['username']
                    if request.POST['first_name'] != '':
                        user.first_name = request.POST['first_name']
                    if request.POST['password1'] != '':
                        user.set_password(request.POST['password1'])
                    logout(request)
                    user.save()
                    login(request, user)
                    return redirect('profile')

                except:
                    return render(request, 'editprofile.html', {
                        'form': UserUpdateForm,
                        "error": 'Usuário já existe'

                    })

        return render(request, 'editprofile.html', {
            'form': UserUpdateForm,
            "error": 'senhas são diferentes'

        })

    else:
        return render(request, 'editprofile.html', {
            'form': UserUpdateForm
        })
    
@login_required
def insulina(request):
    
    if request.method == 'POST':
        form = InsulinaForm(request.POST)
        if form.is_valid():
            insulina_instance = form.save(commit=False)
            insulina_instance.user = request.user
            insulina_instance.save()
            return redirect('insulina_list')
    else:
        form = InsulinaForm()

    return render(request, 'insulina.html', {'form': form})

@login_required
def insulina_list(request):
    insulina_list = Insulina.objects.filter(user=request.user)
    return render(request, 'insulina_list.html', {'insulina_list': insulina_list})

@login_required
def editar_insulina(request, insulina_id):
    insulina = get_object_or_404(Insulina, pk=insulina_id)
    
    if request.method == 'POST':
        form = InsulinaForm(request.POST, instance=insulina)
        if form.is_valid():
            form.save()
            return redirect('insulina_list')
    else:
        form = InsulinaForm(instance=insulina)

    return render(request, 'editar_insulina.html', {'form': form})

@login_required
def excluir_insulina(request, insulina_id):
    insulina = get_object_or_404(Insulina, pk=insulina_id)
    insulina.delete()
    return redirect('insulina_list')

@login_required
def glicose(request):

    if request.method == 'POST':
        if "cancel" in request.POST:
            return redirect('userpage')
        
        form = GlicoseForm(request.POST)

        if form.is_valid():
            
            glicose_instance = form.save(commit=False)
            glicose_instance.user = request.user
            glicose_instance.save()
            return redirect('glicose_list')
        print(form.errors.as_data())
    else:
        form = GlicoseForm()

    return render(request, 'glicose.html', {'form': form})

@login_required
def glicose_list(request):
    glicose_list = Glicose.objects.filter(user=request.user)
    return render(request, 'glicose_list.html', {'glicose_list': glicose_list})

@login_required
def editar_glicose(request, glicose_id):
    glicose = get_object_or_404(Glicose, pk=glicose_id)
    
    if request.method == 'POST':
        form = GlicoseForm(request.POST, instance=glicose)
        if form.is_valid():
            form.save()
            return redirect('glicose_list')
    else:
        form = GlicoseForm(instance=glicose)

    return render(request, 'editar_glicose.html', {'form': form})

@login_required
def excluir_glicose(request, glicose_id):
    glicose = get_object_or_404(Glicose, pk=glicose_id)
    glicose.delete()
    return redirect('glicose_list')

@login_required
def meal(request):

    if request.method == 'POST':
        if "cancel" in request.POST:
            return redirect('userpage')
        
        form = MealForm(request.POST)

        if form.is_valid():
            
            meal_instance = form.save(commit=False)
            meal_instance.user = request.user
            meal_instance.save()
            return redirect('meal_list')
        print(form.errors.as_data())
    else:
        form = MealForm()

    return render(request, 'meal.html', {'form': form})

@login_required
def meal_list(request):
    meal_list = Meal.objects.filter(user=request.user)
    return render(request, 'meal_list.html', {'meal_list': meal_list})

@login_required
def editar_meal(request, meal_id):
    meal = get_object_or_404(Meal, pk=meal_id)
    
    if request.method == 'POST':
        form = MealForm(request.POST, instance=meal)
        if form.is_valid():
            form.save()
            return redirect('meal_list')
    else:
        form = MealForm(instance=meal)

    return render(request, 'editar_meal.html', {'form': form})

@login_required
def excluir_meal(request, meal_id):
    meal = get_object_or_404(Meal, pk=meal_id)
    meal.delete()
    return redirect('meal_list')

@login_required
def historico(request):
    if request.method == 'POST':
        if "insulina_list" in request.POST:
            return redirect('insulina_list')
        if "glicose_list" in request.POST:
            return redirect('glicose_list')
        if "meal_list" in request.POST:
            return redirect('meal_list')
        if "atividade_fisica_list" in request.POST:
            return redirect('atividade_fisica_list')
    return render(request, 'historico.html')

@login_required
def atividade_fisica(request):
    if request.method == 'POST':
        form = AtividadeFisicaForm(request.POST)
        if form.is_valid():
            atividade_instance = form.save(commit=False)
            atividade_instance.user = request.user
            atividade_instance.save()
            return redirect('atividade_fisica_list')
    else:
        form = AtividadeFisicaForm()

    return render(request, 'atividade_fisica.html', {'form': form})

def atividade_fisica_list(request):
    atividade_list = AtividadeFisica.objects.filter(user=request.user)
    return render(request, 'atividade_fisica_list.html', {'atividade_fisica_list': atividade_list})

def editar_atividade(request, atividade_id):
    atividade = get_object_or_404(AtividadeFisica, pk=atividade_id)
    
    if request.method == 'POST':
        form = AtividadeFisicaForm(request.POST, instance=atividade)
        if form.is_valid():
            form.save()
            return redirect('atividade_fisica_list')
    else:
        form = AtividadeFisicaForm(instance=atividade)

    return render(request, 'editar_atividade.html', {'form': form})

def excluir_atividade(request, atividade_id):
    atividade = get_object_or_404(AtividadeFisica, pk=atividade_id)
    atividade.delete()
    return redirect('lista_atividades')