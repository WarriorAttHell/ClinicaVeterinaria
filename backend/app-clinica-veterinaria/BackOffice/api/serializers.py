from rest_framework import serializers
from ..models import *

# Clinica
class ClinicaCadastroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clinica
        fields = [
            'id_clinica',
            'nome_clinica',
            'cnpj',
            'inscricao_estadual',
            'inscricao_municipal',
            'endereco',
            'bairro',
            'cep',
            'municipio',
            'uf',
            'status',
            'data_criacao',
            'data_ult_atualizacao',
            'usuario_criador',
            'usuario_ult_atualizacao'
        ]

class ClinicaListagemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clinica
        fields = [
            'id_clinica',
            'nome_clinica',
            'municipio',
            'uf',
            'status'
        ]

# Tipo de Animal
class TipoAnimalCadastroSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoAnimal
        fields = [
            'id_tipo_animal',
            'nome_tipo_animal',
            'status',
            'data_criacao',
            'data_ult_atualizacao',
            'usuario_criador',
            'usuario_ult_atualizacao'
        ]

class TipoAnimalListagemSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoAnimal
        fields = [
            'id_tipo_animal',
            'nome_tipo_animal',
            'status',
        ]
  
# Raca de Animal
class RacaAnimalCadastroSerializer(serializers.ModelSerializer):
    class Meta:
        model = RacaAnimal
        fields = [
            'id_raca',
            'nome_raca',
            'tipo_animal',
            'status',
            'data_criacao',
            'data_ult_atualizacao',
            'usuario_criador',
            'usuario_ult_atualizacao'
        ]

class RacaAnimalListagemSerializer(serializers.ModelSerializer):
    class Meta:
        model = RacaAnimal
        fields = [
            'nome_raca',
            'tipo_animal',
            'status'
        ]

# Animal
class VacinaAtendimentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacina
        fields = [
            'id_vacina'
        ]
   
class AnimalCadastroSerializer(serializers.ModelSerializer):
    vacina = VacinaAtendimentoSerializer
    class Meta:
        model = Animal
        fields = [
            'id_animal',
            'id_clinica',
            'nome_animal',
            'tipo_animal',
            'raca_animal',
            'data_nascimento',
            'porte',
            'cor',
            'id_responsavel',
            'status',
            'data_criacao',
            'data_ult_atualizacao',
            'usuario_criador',
            'usuario_ult_atualizacao'
        ]

class AnimalListagemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = [
            'id_clinica',
            'nome_animal',
            'tipo_animal',
            'raca_animal',
            'id_responsavel',
            'status'
        ]

# Vacina 
class VacinaAtendimentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacina
        fields = [
            'id_vacina'
        ]
        
class VacinaCadastroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacina
        fields = [
            'id_vacina',
            'id_clinica',
            'nome_vacina',
            'descricao',
            'status',
            'data_criacao',
            'data_ult_atualizacao',
            'usuario_criador',
            'usuario_ult_atualizacao'
        ]

class VacinaListagemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacina
        fields = [
            'id_clinica',
            'nome_vacina',
            'descricao',
            'status',
        ]

# Forma de Pagamento
class FormaPagamentoCadastroSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormaPagamento
        fields = [
            'id_forma_pagamento',
            'nome_forma_pagamento',
            # 'logo',
            'dados_integracao',
            'id_clinica',
            'status',
            'data_criacao',
            'data_ult_atualizacao',
            'usuario_criador',
            'usuario_ult_atualizacao'
        ]

class FormaPagamentoListagemSerializer(serializers.ModelSerializer):
    logo = serializers.ImageField(max_length=None, use_url=True)
    class Meta:
        model = FormaPagamento
        fields = [
            'nome_forma_pagamento',
            'logo',
            'dados_integracao',
            'id_clinica',
            'status',
        ]
    
# Atendimento
class AtendimentoCadastroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Atendimento
        fields = [
            'id_atendimento',
            'id_clinica',
            'id_cliente',
            'id_animal',
            'id_medico',
            'categoria_atendimento',
            'titulo_atendimento',
            'descricao_atendimento',
            'urgencia',
            'status_atendimento',
            'status_pagamento',
            'vacinas',
            'data_criacao',
            'data_inicio',
            'data_encerramento',
            'data_pagamento',
            'data_ult_atualizacao',
            'usuario_criador',
            'usuario_ult_atualizacao'
        ]

class AtendimentoListagemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Atendimento
        fields = [
            'id_clinica',
            'id_cliente',
            'id_animal',
            'id_medico',
            'categoria_atendimento',
            'titulo_atendimento',
            'urgencia',
            'status_atendimento',
            'status_pagamento',
            'data_inicio',
            'data_encerramento',
            'data_pagamento',
        ]

# Pagamento   
class PagamentoCadastroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pagamento
        fields = [
            'id_pagamento',
            'id_atendimento',
            'id_forma_pagamento',
            'data_pagamento',
            'valor_pagamento',
            'data_criacao',
            'data_ult_atualizacao',
            'usuario_criador',
            'usuario_ult_atualizacao'
        ]

class PagamentoListagemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pagamento
        fields = [
            'id_atendimento',
            'id_forma_pagamento',
            'data_pagamento',
            'valor_pagamento',
            'data_criacao'
        ]
 