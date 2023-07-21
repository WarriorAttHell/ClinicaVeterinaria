from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework import serializers
from rest_framework import status
from rest_framework.response import Response
from django.db.models import ProtectedError
from ..models import *
from .serializers import *
from django.utils import timezone


def preenche_campos_cadastro(request):
    request.data.update({
            'data_criacao': timezone.now(), 
            'data_ult_atualizacao': timezone.now(),
    })       
    if request.user.is_authenticated:
        request.data.update({
            'usuario_criador': request.user.id,
            'usuario_ult_atualizacao': request.user.id
        })
    else:
        request.data.update({
            'usuario_criador': 1,
            'usuario_ult_atualizacao': 1
        })
    return request   

def preenche_campos_alteracao(request, objeto_atual):
    request.data.update({
        'data_criacao': objeto_atual.data_criacao, 
        'data_ult_atualizacao': timezone.now(),
        'usuario_criador': objeto_atual.usuario_criador.id,
    })
    if request.user.is_authenticated:
        request.data.update({
            'usuario_ult_atualizacao': request.user.id
        })
    else:
        request.data.update({
            'usuario_ult_atualizacao': 1
        })
    return request   

# Clinica (LISTAR | DETALHAR | CADASTRAR | ALTERAR | DELETAR)
@api_view(['GET'])
def view_clinica(request):
    clinica = Clinica.objects.all() # SELECT *
 
    # if there is something in items else raise error
    if clinica:
        serializer = ClinicaListagemSerializer(clinica, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
   
@api_view(['GET'])
def detail_clinica(request, pk):
    # checking for the parameters from the URL
    clinica = Clinica.objects.filter(id_clinica=pk)
     
    # if there is something in items else raise error
    if clinica:
        serializer = ClinicaCadastroSerializer(clinica, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def add_clinica(request):
    # Valida se ja existe o clinica
    if Clinica.objects.filter(**request.data).exists():
        raise serializers.ValidationError('Esta clínica já existe.')

    request = preenche_campos_cadastro(request)
    clinica = ClinicaCadastroSerializer(data=request.data)
    
    if clinica.is_valid():
        clinica.save()
        return Response(clinica.data)
    else:
        print(clinica.errors)
        return Response(data=clinica.errors, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def update_clinica(request, pk):
    clinica = Clinica.objects.get(id_clinica=pk)
    request = preenche_campos_alteracao(request, clinica)
    data = ClinicaCadastroSerializer(instance=clinica, data=request.data)
 
    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(data=data.errors, status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def delete_clinica(request, pk):
    clinica = get_object_or_404(Clinica, id_clinica=pk)
    try:
        clinica.delete()
    except ProtectedError as err:
        cadastros = dict()
        for i in err.protected_objects:
            objeto = i.__str__()
            
            modelo = str(type(i)).replace('>','').replace('<','').replace("'","").split('.')[-1]
            # <class 'BackOffice.models.Animal'>
            
            if modelo in cadastros.keys():
                cadastros[modelo].append(objeto)
            else:
                cadastros[modelo] = [objeto,]
                
        data = {
            "message": f"Clinica ID {clinica.id_clinica}, '{clinica.nome_clinica}', não pode ser removida, pois está sendo referenciada em outros cadastros.",
            "cadastros": cadastros
        } 
        return Response(data=data, status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_202_ACCEPTED)

# Tipo de Animal (LISTAR | DETALHAR | CADASTRAR | ALTERAR | DELETAR)
@api_view(['GET'])
def view_tipo_animal(request):
    tipo_animal = TipoAnimal.objects.all()
 
    # if there is something in items else raise error
    if tipo_animal:
        serializer = TipoAnimalListagemSerializer(tipo_animal, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
   
@api_view(['GET'])
def detail_tipo_animal(request, pk):
    tipo_animal = TipoAnimal.objects.filter(id_tipo_animal=pk)

    # if there is something in items else raise error
    if tipo_animal:
        serializer = TipoAnimalCadastroSerializer(tipo_animal, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def add_tipo_animal(request):
    # Valida se ja existe o tipo_animal
    if TipoAnimal.objects.filter(**request.data).exists():
        raise serializers.ValidationError('Este tipo de animal já existe.')

    request = preenche_campos_cadastro(request)
    tipo_animal = TipoAnimalCadastroSerializer(data=request.data)
    
    if tipo_animal.is_valid():
        tipo_animal.save()
        return Response(tipo_animal.data)
    else:
        print(tipo_animal.errors)
        return Response(data=tipo_animal.errors, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def update_tipo_animal(request, pk):
    tipo_animal = TipoAnimal.objects.get(id_tipo_animal=pk)
    request = preenche_campos_alteracao(request, tipo_animal)
    data = TipoAnimalCadastroSerializer(instance=tipo_animal, data=request.data)
 
    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(data=data.errors, status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def delete_tipo_animal(request, pk):
    tipo_animal = get_object_or_404(TipoAnimal, id_tipo_animal=pk)
    try:
        tipo_animal.delete()
    except ProtectedError as err:
        cadastros = dict()
        for i in err.protected_objects:
            objeto = i.__str__()
            
            modelo = str(type(i)).replace('>','').replace('<','').replace("'","").split('.')[-1]
            # <class 'BackOffice.models.Animal'>
            
            if modelo in cadastros.keys():
                cadastros[modelo].append(objeto)
            else:
                cadastros[modelo] = [objeto,]
                
        data = {
            "message": f"Tipo Animal ID {tipo_animal.id_tipo_animal}, '{tipo_animal.nome_tipo_animal}', não pode ser removida, pois está sendo referenciada em outros cadastros.",
            "cadastros": cadastros
        } 
        return Response(data=data, status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_202_ACCEPTED)

# Raca de Animal (LISTAR | DETALHAR | CADASTRAR | ALTERAR | DELETAR)
@api_view(['GET'])
def view_raca_animal(request):
    raca_animal = RacaAnimal.objects.all()
 
    # if there is something in items else raise error
    if raca_animal:
        serializer = RacaAnimalListagemSerializer(raca_animal, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
   
@api_view(['GET'])
def detail_raca_animal(request, pk):
    raca_animal = RacaAnimal.objects.filter(id_raca=pk)

    # if there is something in items else raise error
    if raca_animal:
        serializer = RacaAnimalCadastroSerializer(raca_animal, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def add_raca_animal(request):
    # Valida se ja existe o raca_animal
    if RacaAnimal.objects.filter(**request.data).exists():
        raise serializers.ValidationError('Esta raça de animal já existe.')

    request = preenche_campos_cadastro(request)
    raca_animal = RacaAnimalCadastroSerializer(data=request.data)
    
    if raca_animal.is_valid():
        raca_animal.save()
        return Response(raca_animal.data)
    else:
        print(raca_animal.errors)
        return Response(data=raca_animal.errors, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def update_raca_animal(request, pk):
    raca_animal = RacaAnimal.objects.get(id_raca=pk)
    request = preenche_campos_alteracao(request, raca_animal)
    data = RacaAnimalCadastroSerializer(instance=raca_animal, data=request.data)
 
    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(data=data.errors, status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def delete_raca_animal(request, pk):
    raca_animal = get_object_or_404(RacaAnimal, id_raca=pk)
    try:
        raca_animal.delete()
    except ProtectedError as err:
        cadastros = dict()
        for i in err.protected_objects:
            objeto = i.__str__()
            
            modelo = str(type(i)).replace('>','').replace('<','').replace("'","").split('.')[-1]
            # <class 'BackOffice.models.Animal'>
            
            if modelo in cadastros.keys():
                cadastros[modelo].append(objeto)
            else:
                cadastros[modelo] = [objeto,]
                
        data = {
            "message": f"Raça Animal ID {raca_animal.id_raca}, '{raca_animal.nome_raca_animal}', não pode ser removida, pois está sendo referenciada em outros cadastros.",
            "cadastros": cadastros
        } 
        return Response(data=data, status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_202_ACCEPTED)

# Animal (LISTAR | DETALHAR | CADASTRAR | ALTERAR | DELETAR)
@api_view(['GET'])
def view_animal(request):
    animal = Animal.objects.all()
 
    # if there is something in items else raise error
    if animal:
        serializer = AnimalListagemSerializer(animal, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
   
@api_view(['GET'])
def detail_animal(request, pk):
    animal = Animal.objects.filter(id_animal=pk)

    # if there is something in items else raise error
    if animal:
        serializer = AnimalCadastroSerializer(animal, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def add_animal(request):
    # Valida se ja existe o animal
    if Animal.objects.filter(**request.data).exists():
        raise serializers.ValidationError('Este animal já existe.')

    request = preenche_campos_cadastro(request)
    animal = AnimalCadastroSerializer(data=request.data)
    
    if animal.is_valid():
        animal.save()
        return Response(animal.data)
    else:
        print(animal.errors)
        return Response(data=animal.errors, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def update_animal(request, pk):
    animal = Animal.objects.get(id_animal=pk)
    request = preenche_campos_alteracao(request, animal)
    data = AnimalCadastroSerializer(instance=animal, data=request.data)
 
    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(data=data.errors, status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def delete_animal(request, pk):
    animal = get_object_or_404(Animal, id_animal=pk)
    try:
        animal.delete()
    except ProtectedError as err:
        cadastros = dict()
        for i in err.protected_objects:
            objeto = i.__str__()
            
            modelo = str(type(i)).replace('>','').replace('<','').replace("'","").split('.')[-1]
            # <class 'BackOffice.models.Animal'>
            
            if modelo in cadastros.keys():
                cadastros[modelo].append(objeto)
            else:
                cadastros[modelo] = [objeto,]
                
        data = {
            "message": f"Animal ID {animal.id_animal}, '{animal.nome_animal}', não pode ser removida, pois está sendo referenciada em outros cadastros.",
            "cadastros": cadastros
        } 
        return Response(data=data, status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_202_ACCEPTED)

# Vacina (LISTAR | DETALHAR | CADASTRAR | ALTERAR | DELETAR)
@api_view(['GET'])
def view_vacina(request):
    vacina = Vacina.objects.all()
 
    # if there is something in items else raise error
    if vacina:
        serializer = VacinaListagemSerializer(vacina, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
   
@api_view(['GET'])
def detail_vacina(request, pk):
    vacina = Vacina.objects.filter(id_vacina=pk)

    # if there is something in items else raise error
    if vacina:
        serializer = VacinaCadastroSerializer(vacina, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def add_vacina(request):
    # Valida se ja existe o vacina
    if Vacina.objects.filter(**request.data).exists():
        raise serializers.ValidationError('Esta vacína já existe.')

    request = preenche_campos_cadastro(request)
    vacina = VacinaCadastroSerializer(data=request.data)
    
    if vacina.is_valid():
        vacina.save()
        return Response(vacina.data)
    else:
        print(vacina.errors)
        return Response(data=vacina.errors, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def update_vacina(request, pk):
    vacina = Vacina.objects.get(id_vacina=pk)
    request = preenche_campos_alteracao(request, vacina)
    data = VacinaCadastroSerializer(instance=vacina, data=request.data)
 
    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(data=data.errors, status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def delete_vacina(request, pk):
    vacina = get_object_or_404(Vacina, id_vacina=pk)
    try:
        vacina.delete()
    except ProtectedError as err:
        cadastros = dict()
        for i in err.protected_objects:
            objeto = i.__str__()
            
            modelo = str(type(i)).replace('>','').replace('<','').replace("'","").split('.')[-1]
            # <class 'BackOffice.models.Vacina'>
            
            if modelo in cadastros.keys():
                cadastros[modelo].append(objeto)
            else:
                cadastros[modelo] = [objeto,]
                
        data = {
            "message": f"Vacina ID {vacina.id_vacina}, '{vacina.nome_vacina}', não pode ser removida, pois está sendo referenciada em outros cadastros.",
            "cadastros": cadastros
        } 
        return Response(data=data, status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_202_ACCEPTED)

# Forma de Pagamento (LISTAR | DETALHAR | CADASTRAR | ALTERAR | DELETAR)
@api_view(['GET'])
def view_forma_pagamento(request):
    forma_pagamento = FormaPagamento.objects.all()
 
    # if there is something in items else raise error
    if forma_pagamento:
        serializer = FormaPagamentoListagemSerializer(forma_pagamento, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
   
@api_view(['GET'])
def detail_forma_pagamento(request, pk):
    forma_pagamento = FormaPagamento.objects.filter(id_forma_pagamento=pk)

    # if there is something in items else raise error
    if forma_pagamento:
        serializer = FormaPagamentoCadastroSerializer(forma_pagamento, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def add_forma_pagamento(request):
    # Valida se ja existe o forma_pagamento
    if FormaPagamento.objects.filter(**request.data).exists():
        raise serializers.ValidationError('Esta forma de pagamento já existe.')

    request = preenche_campos_cadastro(request)
    forma_pagamento = FormaPagamentoCadastroSerializer(data=request.data)
    
    if forma_pagamento.is_valid():
        forma_pagamento.save()
        return Response(forma_pagamento.data)
    else:
        print(forma_pagamento.errors)
        return Response(data=forma_pagamento.errors, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def update_forma_pagamento(request, pk):
    forma_pagamento = FormaPagamento.objects.get(id_forma_pagamento=pk)
    request = preenche_campos_alteracao(request, forma_pagamento)
    data = FormaPagamentoCadastroSerializer(instance=forma_pagamento, data=request.data)
 
    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(data=data.errors, status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def delete_forma_pagamento(request, pk):
    forma_pagamento = get_object_or_404(FormaPagamento, id_forma_pagamento=pk)
    try:
        forma_pagamento.delete()
    except ProtectedError as err:
        cadastros = dict()
        for i in err.protected_objects:
            objeto = i.__str__()
            
            modelo = str(type(i)).replace('>','').replace('<','').replace("'","").split('.')[-1]
            # <class 'BackOffice.models.FormaPagamento'>
            
            if modelo in cadastros.keys():
                cadastros[modelo].append(objeto)
            else:
                cadastros[modelo] = [objeto,]
                
        data = {
            "message": f"Forma de Pagamento ID {forma_pagamento.id_forma_pagamento}, '{forma_pagamento.nome_forma_pagamento}', não pode ser removida, pois está sendo referenciada em outros cadastros.",
            "cadastros": cadastros
        } 
        return Response(data=data, status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_202_ACCEPTED)

# Atendimento (LISTAR | DETALHAR | CADASTRAR | ALTERAR | DELETAR)
@api_view(['GET'])
def view_atendimento(request):
    atendimento = Atendimento.objects.all()
 
    # if there is something in items else raise error
    if atendimento:
        serializer = AtendimentoListagemSerializer(atendimento, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
   
@api_view(['GET'])
def detail_atendimento(request, pk):
    atendimento = Atendimento.objects.filter(id_atendimento=pk)

    # if there is something in items else raise error
    if atendimento:
        serializer = AtendimentoCadastroSerializer(atendimento, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def add_atendimento(request):
    # Valida se ja existe o atendimento
  
    # if Atendimento.objects.filter(**request.data).exists():
    #     raise serializers.ValidationError('Este atendimento já existe.')

    request = preenche_campos_cadastro(request)
    atendimento = AtendimentoCadastroSerializer(data=request.data)
    
    if atendimento.is_valid():
        atendimento.save()
        return Response(atendimento.data)
    else:
        print(atendimento.errors)
        return Response(data=atendimento.errors, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def update_atendimento(request, pk):
    atendimento = Atendimento.objects.get(id_atendimento=pk)
    request = preenche_campos_alteracao(request, atendimento)
    data = AtendimentoCadastroSerializer(instance=atendimento, data=request.data)
 
    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(data=data.errors, status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def delete_atendimento(request, pk):
    atendimento = get_object_or_404(Atendimento, id_atendimento=pk)
    try:
        atendimento.delete()
    except ProtectedError as err:
        cadastros = dict()
        for i in err.protected_objects:
            objeto = i.__str__()
            
            modelo = str(type(i)).replace('>','').replace('<','').replace("'","").split('.')[-1]
            # <class 'BackOffice.models.Atendimento'>
            
            if modelo in cadastros.keys():
                cadastros[modelo].append(objeto)
            else:
                cadastros[modelo] = [objeto,]
                
        data = {
            "message": f"Atendimento ID {atendimento.id_atendimento}, '{atendimento.nome_atendimento}', não pode ser removida, pois está sendo referenciada em outros cadastros.",
            "cadastros": cadastros
        } 
        return Response(data=data, status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_202_ACCEPTED)

# Pagamento (LISTAR | DETALHAR | CADASTRAR | ALTERAR | DELETAR)
@api_view(['GET'])
def view_pagamento(request):
    pagamento = Pagamento.objects.all()
 
    # if there is something in items else raise error
    if pagamento:
        serializer = PagamentoListagemSerializer(pagamento, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
   
@api_view(['GET'])
def detail_pagamento(request, pk):
    pagamento = Pagamento.objects.filter(id_pagamento=pk)

    # if there is something in items else raise error
    if pagamento:
        serializer = PagamentoCadastroSerializer(pagamento, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def add_pagamento(request):
    # Valida se ja existe o pagamento
    if Pagamento.objects.filter(**request.data).exists():
        raise serializers.ValidationError('Este pagamento já existe.')

    request = preenche_campos_cadastro(request)
    pagamento = PagamentoCadastroSerializer(data=request.data)
    
    if pagamento.is_valid():
        pagamento.save()
        return Response(pagamento.data)
    else:
        print(pagamento.errors)
        return Response(data=pagamento.errors, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def update_pagamento(request, pk):
    pagamento = Pagamento.objects.get(id_pagamento=pk)
    request = preenche_campos_alteracao(request, pagamento)
    data = PagamentoCadastroSerializer(instance=pagamento, data=request.data)
 
    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(data=data.errors, status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def delete_pagamento(request, pk):
    pagamento = get_object_or_404(Pagamento, id_pagamento=pk)
    try:
        pagamento.delete()
    except ProtectedError as err:
        cadastros = dict()
        for i in err.protected_objects:
            objeto = i.__str__()
            
            modelo = str(type(i)).replace('>','').replace('<','').replace("'","").split('.')[-1]
            # <class 'BackOffice.models.Pagamento'>
            
            if modelo in cadastros.keys():
                cadastros[modelo].append(objeto)
            else:
                cadastros[modelo] = [objeto,]
                
        data = {
            "message": f"Pagamento ID {pagamento.id_pagamento} não pode ser removida, pois está sendo referenciada em outros cadastros.",
            "cadastros": cadastros
        } 
        return Response(data=data, status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_202_ACCEPTED)


