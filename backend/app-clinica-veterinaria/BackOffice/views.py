from django.shortcuts import redirect, render, get_object_or_404
from .models import (Clinica, TipoAnimal, RacaAnimal,
                     Animal, Vacina, FormaPagamento, Atendimento,
                     Pagamento)


ROTA_ADMIN = 'appdamin'

def index(request):
    """Se o usuario estiver logado, retorna o contexto necessário para renderizar o menu lateral"""
    return render(request, 'base.html', {})

## LISTAGEM
def listar_clinicas(request):
    pass

def listar_tipos_animais(request):
    pass

def listar_racas_animais(request):
    pass

def listar_animais(request):
    pass

def listar_vacinas(request):
    pass

def listar_formas_pagamento(request):
    pass

def listar_pagamentos(request):
    pass

def listar_atendimentos(request):
    pass


## CADASTRO
def cadastrar_clinica(request):
    pass

def cadastrar_tipo_animal(request):
    pass

def cadastrar_raca_animal(request):
    pass

def cadastrar_animal(request):
    pass

def cadastrar_vacina(request):
    pass

def cadastrar_forma_pagamento(request):
    pass

def cadastrar_pagamento(request):
    pass

def cadastrar_atendimento(request):
    pass

