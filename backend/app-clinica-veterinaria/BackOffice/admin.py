from django import forms
from django.contrib import admin
from django.db.models.query import QuerySet #
from django.http.request import HttpRequest #
from .models import (Clinica, TipoAnimal, RacaAnimal,
                     Animal, Vacina, FormaPagamento, Atendimento,
                     Pagamento)

# Register your models here.
@admin.register(Clinica)
class ClinicaAdmin(admin.ModelAdmin):
    list_display = ('nome_clinica','cnpj', 'inscricao_estadual', 'inscricao_municipal','endereco',
                    'bairro','cep', 'municipio','uf', 'status')
    list_filter = ('status', 'nome_clinica', 'municipio', 'uf', 'data_criacao')
    search_fields = ('nome_clinica', )
    date_hierarchy = 'data_criacao'
    ordering = ('-id_clinica',)
    readonly_fields = ('data_criacao', 'data_ult_atualizacao'
                    #    ,'usuario_criador', 'usuario_ult_atualizacao'
                    )
    
    # def save_form(self, request, form, change):
    #     obj = super(ClinicaAdmin, self).save_form(request, form, change)
    #     if not change:
    #         obj.usuario_criador = request.user
    #         obj.usuario_ult_atualizacao = request.user
    #     else:
    #         obj.usuario_ult_atualizacao = request.user
    #     return obj
    
@admin.register(TipoAnimal)
class TipoAnimalAdmin(admin.ModelAdmin):
    list_display = ('nome_tipo_animal','status')
    list_filter = ('nome_tipo_animal','status')
    search_fields = ('nome_tipo_animal', )
    date_hierarchy = 'data_criacao'
    ordering = ('-id_tipo_animal',)
    readonly_fields = ('data_criacao', 'data_ult_atualizacao'
                    #    ,'usuario_criador', 'usuario_ult_atualizacao'
                       )
    
    # def save_form(self, request, form, change):
    #     obj = super(TipoAnimalAdmin, self).save_form(request, form, change)
    #     if not change:
    #         obj.usuario_criador = request.user
    #         obj.usuario_ult_atualizacao = request.user
    #     else:
    #         obj.usuario_ult_atualizacao = request.user
    #     return obj

@admin.register(RacaAnimal)
class RacaAnimalAdmin(admin.ModelAdmin):
    list_display = ('nome_raca','tipo_animal','status')
    list_filter = ('nome_raca','tipo_animal','status')
    search_fields = ('nome_raca', )
    date_hierarchy = 'data_criacao'
    ordering = ('-id_raca',)
    readonly_fields = ('data_criacao', 'data_ult_atualizacao'
                    #    ,'usuario_criador', 'usuario_ult_atualizacao'
                       )
    

    
    # def save_form(self, request, form, change):
    #     obj = super(RacaAnimalAdmin, self).save_form(request, form, change)
    #     if not change:
    #         obj.usuario_criador = request.user
    #         obj.usuario_ult_atualizacao = request.user
    #     else:
    #         obj.usuario_ult_atualizacao = request.user
    #     return obj
    
@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):

    list_display = ('id_clinica', 'nome_animal', 'tipo_animal', 'data_nascimento',
                    'porte', 'cor', 'id_responsavel', 'status')
    list_filter = ('id_clinica', 'nome_animal', 'tipo_animal', 'porte', 'cor', 
                   'id_responsavel','status')
    search_fields = ('nome_animal', )
    date_hierarchy = 'data_criacao'
    raw_id_fields = ('raca_animal',)
    ordering = ('-id_animal',)
    readonly_fields = ('data_criacao', 'data_ult_atualizacao'
                    #    ,'usuario_criador', 'usuario_ult_atualizacao'
                       )
    
    # def formfield_for_foreignkey(self, db_field, request: HttpRequest, **kwargs):
        
    #     print(f'DB_FIELD: {db_field}')
    #     print(f'Request: {request.GET}')
    #     print(f'kwargs: {kwargs}')
    #     print('---------------------\n')
    #     if db_field.name == 'raca_animal':
    #         tipo_animal_selected = request.GET.get('tipo_animal')
    #         print(tipo_animal_selected)
    #         kwargs["queryset"] = RacaAnimal.objects.filter(tipo_animal=request.GET.get('tipo_animal'))
    #     return super().formfield_for_foreignkey(db_field, request, **kwargs)
    # def save_form(self, request, form, change):
    #     obj = super(AnimalAdmin, self).save_form(request, form, change)
    #     if not change:
    #         obj.usuario_criador = request.user
    #         obj.usuario_ult_atualizacao = request.user
    #     else:
    #         obj.usuario_ult_atualizacao = request.user
    #     return obj

@admin.register(Vacina)
class VacinaAdmin(admin.ModelAdmin):
    list_display = ('id_clinica', 'nome_vacina', 'descricao', 'status')
    list_filter = ('id_clinica', 'nome_vacina', 'descricao', 'status')
    search_fields = ('nome_vacina', 'descricao')
    date_hierarchy = 'data_criacao'
    ordering = ('-id_vacina',)
    readonly_fields = ('data_criacao', 'data_ult_atualizacao'
                    #    ,'usuario_criador', 'usuario_ult_atualizacao'
                       )
    
    # def save_form(self, request, form, change):
    #     obj = super(VacinaAdmin, self).save_form(request, form, change)
    #     if not change:
    #         obj.usuario_criador = request.user
    #         obj.usuario_ult_atualizacao = request.user
    #     else:
    #         obj.usuario_ult_atualizacao = request.user
    #     return obj

@admin.register(FormaPagamento)
class FormaPagamentoAdmin(admin.ModelAdmin):
    list_display = ('id_clinica', 'nome_forma_pagamento', 'status')
    list_filter = ('id_clinica', 'nome_forma_pagamento', 'status')
    search_fields = ('nome_forma_pagamento', )
    date_hierarchy = 'data_criacao'
    ordering = ('-id_forma_pagamento',)
    readonly_fields = ('data_criacao', 'data_ult_atualizacao'
                    #    ,'usuario_criador', 'usuario_ult_atualizacao'
                       )
    
    # def save_form(self, request, form, change):
    #     obj = super(FormaPagamentoAdmin, self).save_form(request, form, change)
    #     if not change:
    #         obj.usuario_criador = request.user
    #         obj.usuario_ult_atualizacao = request.user
    #     else:
    #         obj.usuario_ult_atualizacao = request.user
    #     return obj

@admin.register(Atendimento)
class AtendimentoAdmin(admin.ModelAdmin):
    list_display = ('titulo_atendimento', 'id_cliente', 'id_animal', 'id_medico', 
                    'categoria_atendimento', 'urgencia', 'status_atendimento')
    list_filter = ('id_clinica', 'titulo_atendimento', 'id_cliente', 'id_animal', 'id_medico', 
                    'categoria_atendimento', 'urgencia', 'status_atendimento','status_pagamento')
    search_fields = ('titulo_atendimento', )
    date_hierarchy = 'data_criacao'
    ordering = ('-id_atendimento',)
    readonly_fields = ('data_criacao', 'data_ult_atualizacao'
                    #    ,'usuario_criador', 'usuario_ult_atualizacao'
                       )
    
    # def save_form(self, request, form, change):
    #     obj = super(AtendimentoAdmin, self).save_form(request, form, change)
    #     if not change:
    #         obj.usuario_criador = request.user
    #         obj.usuario_ult_atualizacao = request.user
    #     else:
    #         obj.usuario_ult_atualizacao = request.user
    #     return obj

@admin.register(Pagamento)
class PagamentoAdmin(admin.ModelAdmin):
    list_display = ('id_atendimento', 'id_forma_pagamento', 'data_pagamento', 'valor_pagamento')
    list_filter = ('id_atendimento', 'id_forma_pagamento', 'data_pagamento')
    search_fields = ('id_pagamento', )
    date_hierarchy = 'data_criacao'
    ordering = ('-id_pagamento',)
    readonly_fields = ('data_criacao', 'data_ult_atualizacao'
                    #    ,'usuario_criador', 'usuario_ult_atualizacao'
                       )
    
    # def save_form(self, request, form, change):
    #     obj = super(PagamentoAdmin, self).save_form(request, form, change)
    #     if not change:
    #         obj.usuario_criador = request.user
    #         obj.usuario_ult_atualizacao = request.user
    #     else:
    #         obj.usuario_ult_atualizacao = request.user
    #     return obj
