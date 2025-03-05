from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import CadastroUsuarioForm, EntradaForm
from .models import Entrada
from django.contrib.auth.decorators import login_required

# Página inicial (login)
def pagina_inicial(request):
    return render(request, 'diario/pagina_inicial.html')

# Registro de usuário
def registro(request):
    if request.method == 'POST':
        form = CadastroUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('diario:entrada_diario')
    else:
        form = CadastroUsuarioForm()
    return render(request, 'diario/registro.html', {'form': form})

# Login de usuário
def login_usuario(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('diario:entrada_diario')
    else:
        form = AuthenticationForm()
    return render(request, 'diario/login.html', {'form': form})

# Criar uma nova entrada no diário
@login_required
def criar_entrada(request):
    if request.method == 'POST':
        form = EntradaForm(request.POST)
        if form.is_valid():
            nova_entrada = form.save(commit=False)
            nova_entrada.user = request.user  # Relaciona com o usuário logado
            nova_entrada.save()
            return redirect('diario:entrada_diario')
    else:
        form = EntradaForm()
    return render(request, 'diario/criar_entrada.html', {'form': form})

# Exibir as entradas do diário organizadas por data
@login_required
def exibir_entradas(request):
    entradas = Entrada.objects.filter(user=request.user).order_by('-data')
    return render(request, 'diario/exibir_entradas.html', {'entradas': entradas})

def editar_entrada(request, entrada_id):
    entrada = get_object_or_404(Entrada, id=entrada_id, user=request.user)
    
    if request.method == "POST":
        form = EntradaForm(request.POST, instance=entrada)
        if form.is_valid():
            form.save()
            return redirect("diario/exibir_entradas")
    else:
        form = EntradaForm(instance=entrada)

    return render(request, "diario/editar_entrada.html", {"form": form})

@login_required
# Excluir entrada
def excluir_entrada(request, entrada_id):
    entrada = get_object_or_404(Entrada, id=entrada_id, user=request.user)
    
    if request.method == "POST":
        entrada.delete()
        return redirect("diario/exibir_entradas")
    
    return render(request, "diario/excluir_entrada.html", {"entrada": entrada})
