from django.shortcuts import render
from rest_framework import viewsets
from .models import Pessoa
from .serializers import PessoaSerializer
from .models import Pessoa

class PessoaViewSet(viewsets.ModelViewSet):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer



def lista_pessoas(request):
    pessoas = Pessoa.objects.all()
    return render(request, 'pessoas/lista.html', {'pessoas': pessoas})