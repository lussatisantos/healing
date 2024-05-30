from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User

# Create your views here.
def cadastro(request):
    if request.method == 'GET':
        return render(request, 'cadastro.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')

        if senha != confirmar_senha:
            return redirect('/usuarios/cadastro')

        if len(senha) < 6:
            return redirect('/usuarios/cadastro')

        user = User.objects.create_user(
            username=username, 
            email=email, 
            password=senha
        )

        return render(request, 'cadastro.html', {'nome': nome, 'email': email, 'senha': senha})