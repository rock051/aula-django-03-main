from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User

def login(request):
    return render(request, 'login.html')

def cadastro(request):
    return render(request, 'cadastro.html')

def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    else: #senão será via método "POST":
        usuario = request.POST.get('usuario')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        user = User.objects.filter(username=usuario).first()
        if user:
            return HttpResponse('Já existe um usuário com esse username')

        # se não existir usuário com esse nome cria e salva o mesmo.
        user = User.objects.create_user(username=usuario, email=email, password=senha)
        user.save()

        return HttpResponse('Usuário cadastrado com sucesso')
