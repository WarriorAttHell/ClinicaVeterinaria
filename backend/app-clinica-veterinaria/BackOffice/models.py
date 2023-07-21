from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
import re


def validate_cep(value):
    if len(value) == 8:
        padrao = r'^\d{5}\d{3}$'
        if re.match(padrao, value):
            return True
        else:
            raise ValidationError(_("%(value)s is not an valid CEP"),params={"value": value},)
        
    if len(value) == 9:
        padrao = r'^\d{5}-\d{3}$'
        if re.match(padrao, value):
            return True
        else:
            raise ValidationError(_("%(value)s is not an valid CEP"),params={"value": value},)
    else:
        raise ValidationError(_("%(value)s is not an valid CEP"),params={"value": value},)


def validate_cnpj(cnpj):
    
    # Remove todos os algarismos não numéricos
    cnpj = re.sub(r'[^0-9]', '', cnpj)
    
    # Verifica o comprimento do numero informado
    if len(cnpj) != 14:
        raise ValidationError(_("%(value)s is not an valid CNPJ"),params={"value": cnpj},)
    
    # Armazena os dois ultimos DV do cnpj informado
    original_dv1, original_dv2 = (cnpj[-2], cnpj[-1])
    pesos_dv1 = [5,4,3,2,9,8,7,6,5,4,3,2]
    soma_dv1 = 0
    resto_dv1 = 0 
    cnpj12 = cnpj[:12]
    dv1 = 0
    
    pesos_dv2 = [6,5,4,3,2,9,8,7,6,5,4,3,2]
    soma_dv2 = 0
    resto_dv2 = 0
    dv2 = 0
        
    # Valida o primeiro DV
    for k, cnpj_digit in enumerate(cnpj12):
        soma_dv1 += int(cnpj_digit) * pesos_dv1[k]
    resto_dv1 = int(soma_dv1 % 11)
    dv1 = 0 if resto_dv1 < 2 else 11 - resto_dv1
    if str(dv1) != original_dv1:
        raise ValidationError(_("%(value)s is not an valid CNPJ"),params={"value": cnpj},)
        
    # Valida o segundo DV
    cnpj13 = str(cnpj[:12]) + str(dv1)
    for k, cnpj_digit in enumerate(cnpj13):
        soma_dv2 += int(cnpj_digit) * pesos_dv2[k]
    resto_dv2 = int(soma_dv2 % 11)
    dv2 = 0 if resto_dv2 < 2 else 11 - resto_dv2
    if str(dv2) != original_dv2:
        raise ValidationError(_("%(value)s is not an valid CNPJ"),params={"value": cnpj},)
    
    return True


class Clinica(models.Model):
    STATUS_CHOICE = (
        ('A', 'Ativo'),
        ('I', 'Inativo')
    )
    UF_CHOICES = (
        ('AC','Acre'),
        ('AL','Alagoas'),
        ('AM','Amazonas'),
        ('AP','Amapá'),
        ('BA','Bahia'),
        ('CE','Ceará'),
        ('DF','Distrito Federal'),
        ('ES','Espírito Santo'),
        ('GO','Goiás'),
        ('MA','Maranhão'),
        ('MG','Minas Gerais'),
        ('MS','Mato Grosso do Sul'),
        ('MT','Mato Grosso'),
        ('PA','Pará'),
        ('PB','Paraíba'),
        ('PE','Pernambuco'),
        ('PI','Piauí'),
        ('PR','Paraná'),
        ('RJ','Rio de Janeiro'),
        ('RN','Rio Grande do Norte'),
        ('RO','Rondônia'),
        ('RR','Roraima'),
        ('RS','Rio Grande do Sul'),
        ('SC','Santa Catarina'),
        ('SE','Sergipe'),
        ('SP','São Paulo'),
        ('TO','Tocantins'),
    )
    id_clinica = models.AutoField(primary_key=True)
    nome_clinica = models.CharField(max_length=250, verbose_name='Nome da Clínica')
    cnpj = models.CharField(max_length=20, verbose_name='CNPJ', validators=[validate_cnpj])
    inscricao_estadual = models.CharField(max_length=20, verbose_name='Inscrição Estadual')
    inscricao_municipal = models.CharField(max_length=20, verbose_name='Inscrição Municipal')
    endereco = models.CharField(max_length=512, verbose_name='Endereço')
    bairro = models.CharField(max_length=250, verbose_name='Bairro')
    cep = models.CharField(max_length=9, validators=[validate_cep], verbose_name='CEP')
    municipio = models.CharField(max_length=250, verbose_name='Município')
    uf = models.CharField(max_length=2, verbose_name='UF', choices=UF_CHOICES)
    status = models.CharField(max_length=1,
                              choices=STATUS_CHOICE,
                              default='A',
                              verbose_name='Status')
    data_criacao = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    data_ult_atualizacao = models.DateTimeField(auto_now=True, verbose_name="Última alteração em")
    usuario_criador = models.ForeignKey(User, 
                                        related_name='usuario_criador_clinica',
                                        on_delete=models.PROTECT, 
                                        null=False,
                                        verbose_name="Criado por")
    usuario_ult_atualizacao = models.ForeignKey(User, 
                                                related_name='usuario_alteracao_clinica',
                                                on_delete=models.PROTECT,
                                                null=False,
                                                verbose_name="Última alteração feita por")
    
    class Meta:
        ordering = ('id_clinica',)
        verbose_name_plural = 'Clínicas'

    def __str__(self):
        return self.nome_clinica
    
class TipoAnimal(models.Model):
    STATUS_CHOICE = (
        ('A', 'Ativo'),
        ('I', 'Inativo')
    )
    id_tipo_animal = models.AutoField(primary_key=True)
    nome_tipo_animal = models.CharField(max_length=250, verbose_name="Tipo de Animal")
    status = models.CharField(max_length=1,
                              choices=STATUS_CHOICE,
                              default='A',
                              verbose_name="Status")
    data_criacao = models.DateTimeField(auto_now_add=True, verbose_name="Criado em")
    data_ult_atualizacao = models.DateTimeField(auto_now=True, verbose_name="Última alteração em")
    usuario_criador = models.ForeignKey(User, 
                                        related_name='usuario_criador_tipo_animal',
                                        on_delete=models.PROTECT,
                                        null=False, 
                                        verbose_name="Criado por")
    usuario_ult_atualizacao = models.ForeignKey(User, 
                                                related_name='usuario_alteracao_tipo_animal',
                                                on_delete=models.PROTECT,
                                                null=False, 
                                                verbose_name="Última alteração feita por")
    class Meta:
        ordering = ('id_tipo_animal',)
        verbose_name_plural = 'Tipos de Animal'
        
    def __str__(self):
        return self.nome_tipo_animal
    
class RacaAnimal(models.Model):
    STATUS_CHOICE = (
        ('A', 'Ativo'),
        ('I', 'Inativo')
    )
    id_raca = models.AutoField(primary_key=True)
    nome_raca = models.CharField(max_length=250, verbose_name="Raça")
    tipo_animal = models.ForeignKey(TipoAnimal,
                                    related_name='tipo_animal_raca',
                                    on_delete=models.PROTECT,
                                    null=False,
                                    verbose_name="Tipo de Animal")
    status = models.CharField(max_length=1,
                              choices=STATUS_CHOICE,
                              default='A',
                              verbose_name='Status')
    data_criacao = models.DateTimeField(auto_now_add=True, verbose_name="Criado em")
    data_ult_atualizacao = models.DateTimeField(auto_now=True, verbose_name="Última alteração em")
    usuario_criador = models.ForeignKey(User, 
                                        related_name='usuario_criador_raca',
                                        on_delete=models.PROTECT,
                                        null=False, 
                                        verbose_name="Criado por")
    usuario_ult_atualizacao = models.ForeignKey(User, 
                                        related_name='usuario_alteracao_raca',
                                        on_delete=models.PROTECT,
                                        null=False, 
                                        verbose_name="Última alteração feita por")
    
    class Meta:
        ordering = ('id_raca',)
        verbose_name_plural = 'Raças de Animal'

    def __str__(self):
        return f"{self.nome_raca}"
    
class Animal(models.Model):
    STATUS_CHOICE = (
        ('A', 'Ativo'),
        ('I', 'Inativo')
    )
    PORTE_CHOICES = (
        ('P', 'Pequeno'),
        ('M', 'Médio'),
        ('G', 'Grande')        
    )
    id_animal = models.AutoField(primary_key=True)
    id_clinica = models.ForeignKey(Clinica,
                                   related_name='clinica_animal',
                                    on_delete=models.PROTECT,
                                    verbose_name="Clínica")
    nome_animal = models.CharField(max_length=250, verbose_name="Nome do animal")
    tipo_animal = models.ForeignKey(TipoAnimal, 
                                    related_name='tipo_animal',
                                    on_delete=models.PROTECT,
                                    default=1,
                                    verbose_name="Tipo de Animal")
    raca_animal = models.ForeignKey(RacaAnimal,
                                    related_name='raca_animal',
                                    on_delete=models.PROTECT,
                                    verbose_name="Raça")
    data_nascimento = models.DateField(verbose_name='Data de nascimento')
    porte = models.CharField(max_length=1,
                              choices=PORTE_CHOICES,
                              default='P',
                              verbose_name='Porte') 
    cor = models.CharField(max_length=50, verbose_name='Cor')
    id_responsavel = models.ForeignKey(User, 
                                       related_name='responsavel_animal',
                                       on_delete=models.PROTECT,
                                       verbose_name='Responsável')
    status = models.CharField(max_length=1,
                              choices=STATUS_CHOICE,
                              default='A',
                              verbose_name='Status')
    data_criacao = models.DateTimeField(auto_now_add=True, verbose_name="Criado em")
    data_ult_atualizacao = models.DateTimeField(auto_now=True, verbose_name="Última alteração em")
    usuario_criador = models.ForeignKey(User, 
                                        related_name='usuario_criador_animal',
                                        on_delete=models.PROTECT,
                                        null=False, 
                                        verbose_name="Criado por")
    usuario_ult_atualizacao = models.ForeignKey(User, 
                                                related_name='usuario_alteracao_animal',
                                                on_delete=models.PROTECT,
                                                null=False, 
                                                verbose_name="Última alteração feita por")
    class Meta:
        ordering = ('id_animal',)
        verbose_name_plural = 'Animais'

    def __str__(self):
        return self.nome_animal
    
class Vacina(models.Model):
    STATUS_CHOICE = (
        ('A', 'Ativo'),
        ('I', 'Inativo')
    )  
    id_vacina = models.AutoField(primary_key=True)
    id_clinica = models.ForeignKey(Clinica,
                                   related_name='clinica_vacina',
                                   on_delete=models.PROTECT,
                                   verbose_name='Clínica')
    nome_vacina = models.CharField(max_length=250, verbose_name='Vacina')
    descricao = models.TextField(verbose_name='Descrição')
    status = models.CharField(max_length=1,
                              choices=STATUS_CHOICE,
                              default='A',
                              verbose_name='Status')
    data_criacao = models.DateTimeField(auto_now_add=True, verbose_name="Criado em")
    data_ult_atualizacao = models.DateTimeField(auto_now=True, verbose_name="Última alteração em")
    usuario_criador = models.ForeignKey(User, 
                                        related_name='usuario_criador_atendimento_vacina',
                                        on_delete=models.PROTECT,
                                        null=False, 
                                        verbose_name="Criado por")
    usuario_ult_atualizacao = models.ForeignKey(User, 
                                                related_name='usuario_alteracao_atendimento_vacina',
                                                on_delete=models.PROTECT,
                                                null=False, 
                                                verbose_name="Última alteração feita por")
    class Meta:
        ordering = ('id_vacina',)
        verbose_name_plural = 'Vacinas'

    def __str__(self):
        return self.nome_vacina
    
class FormaPagamento(models.Model):
    STATUS_CHOICE = (
        ('A', 'Ativo'),
        ('I', 'Inativo')
    )
    id_forma_pagamento = models.AutoField(primary_key=True)
    nome_forma_pagamento = models.CharField(max_length=250, verbose_name="Forma de pagamento")
    logo = models.ImageField(verbose_name="Logo da forma de pagamento", null=True, blank=True)
    dados_integracao = models.TextField(verbose_name="Dados para integração")
    id_clinica = models.ForeignKey(Clinica,
                                   related_name='clinica_forma_pagamento',
                                   on_delete=models.PROTECT,
                                   verbose_name="Clínica")
    status = models.CharField(max_length=1,
                              choices=STATUS_CHOICE,
                              default='A',
                              verbose_name='Status')
    data_criacao = models.DateTimeField(auto_now_add=True, verbose_name="Criado em")
    data_ult_atualizacao = models.DateTimeField(auto_now=True, verbose_name="Última alteração em")
    usuario_criador = models.ForeignKey(User, 
                                        related_name='usuario_criador_forma_pagamento',
                                        on_delete=models.PROTECT,
                                        null=False, 
                                        verbose_name="Criado por")
    usuario_ult_atualizacao = models.ForeignKey(User, 
                                                related_name='usuario_alteracao_forma_pagamento',
                                                on_delete=models.PROTECT,
                                                null=False, 
                                                verbose_name="Última alteração feita por")
    
    class Meta:
        ordering = ('id_forma_pagamento',)
        verbose_name_plural = 'Formas de Pagamento'

    def __str__(self):
        return self.nome_forma_pagamento
    
class Atendimento(models.Model):
    CATEGORIA_CHOICES = (
        ('1', 'PetShop'),
        ('2', 'Atendimento Médico'),
        ('3', 'Intervenção Cirúrgica'),
    )
    URGENCIA_CHOICES = (
        ('1', 'Baixa'),
        ('2', 'Média'),
        ('3', 'Alta'),
        ('4', 'Urgente'),
    )
    STATUS_ATENDIMENTO_CHOICES = (
        ('1', 'Aguardando Atendimento'),
        ('2', 'Em Atendimento'),
        ('3', 'Em Espera'),
        ('4', 'Finalizado'),
    )
    STATUS_PAGAMENTO_CHOICES = (
        ('1', 'Aguardando Pagamento'),
        ('2', 'Pagamento Realizado'),
    )
    id_atendimento = models.AutoField(primary_key=True)
    id_clinica = models.ForeignKey(Clinica,
                                   related_name='clinica_atendimento',
                                   on_delete=models.PROTECT,
                                   verbose_name='Clínica')
    id_cliente = models.ForeignKey(User, 
                                  related_name='responsavel_animal_atendimento',
                                  on_delete=models.PROTECT,
                                  verbose_name='Cliente')
    id_animal = models.ForeignKey(Animal, 
                                  related_name='animal_atendimento',
                                  on_delete=models.PROTECT,
                                  verbose_name='Animal')
    id_medico = models.ForeignKey(User,
                                  related_name='medico_atendimento',
                                  on_delete=models.PROTECT,
                                  null=True,
                                  blank=True,
                                  verbose_name='Médico Veterinário')
    categoria_atendimento = models.CharField(max_length=5,
                                             choices=CATEGORIA_CHOICES,
                                             default='1',
                                             verbose_name='Categoria')
    titulo_atendimento = models.CharField(max_length=250, verbose_name='Titulo')
    descricao_atendimento = models.TextField(verbose_name='Descrição')
    urgencia = models.CharField(max_length=5,
                                choices=URGENCIA_CHOICES,
                                default='1',
                                verbose_name='Urgência')
    status_atendimento = models.CharField(max_length=5,
                                          choices=STATUS_ATENDIMENTO_CHOICES,
                                          default=1,
                                          verbose_name='Status do atendimento')
    status_pagamento = models.CharField(max_length=5,
                                        choices=STATUS_PAGAMENTO_CHOICES,
                                        default='1',
                                        verbose_name='Status do pagamento')
    vacinas = models.ManyToManyField(Vacina, 
                                     verbose_name='Vacina', 
                                     default=None,
                                     null=True,
                                     blank=True)
    data_criacao = models.DateTimeField(auto_now_add=True, verbose_name="Criado em")
    data_inicio = models.DateTimeField(default=datetime.utcfromtimestamp(0), verbose_name="Iniciado em")
    data_encerramento = models.DateTimeField(default=datetime.utcfromtimestamp(0), verbose_name="Encerrado em")
    data_pagamento = models.DateTimeField(default=datetime.utcfromtimestamp(0), verbose_name="Pagamento realizado em")
    data_ult_atualizacao = models.DateTimeField(auto_now=True, verbose_name="Última alteração em")
    usuario_criador = models.ForeignKey(User, 
                                        related_name='usuario_criador_atendimento',
                                        on_delete=models.PROTECT,
                                        null=False, 
                                        verbose_name="Criado por")
    usuario_ult_atualizacao = models.ForeignKey(User, 
                                                related_name='usuario_alteracao_atendimento',
                                                on_delete=models.PROTECT,
                                                null=False, 
                                                verbose_name="Última alteração feita por")
    
    class Meta:
        ordering = ('-data_criacao',)
        verbose_name_plural = 'Atendimentos'

    def __str__(self):
        return self.titulo_atendimento
    
class Pagamento(models.Model):
    id_pagamento = models.AutoField(primary_key=True)
    id_atendimento = models.ForeignKey(Atendimento,
                                       related_name='atendimento_pagamento',
                                       on_delete=models.PROTECT,
                                       verbose_name='Atendimento')
    id_forma_pagamento = models.ForeignKey(FormaPagamento,
                                           related_name='forma_pagamento',
                                           on_delete=models.PROTECT,
                                           verbose_name='Forma de pagamento')
    data_pagamento = models.DateTimeField(verbose_name='Data do pagamento')
    valor_pagamento = models.DecimalField(max_digits=8,decimal_places=2, verbose_name='Valor')
    data_criacao = models.DateTimeField(auto_now_add=True, verbose_name="Criado em")
    data_ult_atualizacao = models.DateTimeField(auto_now=True, verbose_name="Última alteração em")
    usuario_criador = models.ForeignKey(User, 
                                        related_name='usuario_criador_pagamento',
                                        on_delete=models.PROTECT,
                                        null=False, 
                                        verbose_name="Criado por")
    usuario_ult_atualizacao = models.ForeignKey(User, 
                                                related_name='usuario_alteracao_pagamento',
                                                on_delete=models.PROTECT,
                                                null=False, 
                                                verbose_name="Última alteração feita por")

    class Meta:
        ordering = ('id_pagamento',)
        verbose_name_plural = 'Pagamentos'
        
    def __str__(self):
        return f"Pagamento do atendimento {self.id_atendimento}"
     
