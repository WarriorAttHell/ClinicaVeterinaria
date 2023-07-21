from django.urls import path

from . import views

app_name = 'backoffice'
urlpatterns = [
    
    # Clinica
    path('clinica/listar_clinicas/', views.view_clinica, name='listar-clinicas'),
    path('clinica/detalhar_clinica/<int:pk>/', views.detail_clinica, name='detalhar-clinica'),
    path('clinica/add_clinica/', views.add_clinica, name='add-clinica'),
    path('clinica/alterar_clinica/<int:pk>/', views.update_clinica, name='update-clinica'),
    path('clinica/deletar_clinica/<int:pk>/', views.delete_clinica, name='delete-clinica'),
    
    # Tipo de Animal
    path('tipo_animal/listar_tipo_animais/', views.view_tipo_animal, name='listar-tipo_animais'),
    path('tipo_animal/detalhar_tipo_animal/<int:pk>/', views.detail_tipo_animal, name='detalhar-tipo_animal'),
    path('tipo_animal/add_tipo_animal/', views.add_tipo_animal, name='add-tipo_animal'),
    path('tipo_animal/alterar_tipo_animal/<int:pk>/', views.update_tipo_animal, name='update-tipo_animal'),
    path('tipo_animal/deletar_tipo_animal/<int:pk>/', views.delete_tipo_animal, name='delete-tipo_animal'),
    
    # Raça do Animal
    path('raca_animal/listar_raca_animais/', views.view_raca_animal, name='listar-raca_animais'),
    path('raca_animal/detalhar_raca_animal/<int:pk>/', views.detail_raca_animal, name='detalhar-raca_animal'),
    path('raca_animal/add_raca_animal/', views.add_raca_animal, name='add-raca_animal'),
    path('raca_animal/alterar_raca_animal/<int:pk>/', views.update_raca_animal, name='update-raca_animal'),
    path('raca_animal/deletar_raca_animal/<int:pk>/', views.delete_raca_animal, name='delete-raca_animal'),

    # Animal
    path('animal/listar_animais/', views.view_animal, name='listar-animais'),
    path('animal/detalhar_animal/<int:pk>/', views.detail_animal, name='detalhar-animal'),
    path('animal/add_animal/', views.add_animal, name='add-animal'),
    path('animal/alterar_animal/<int:pk>/', views.update_animal, name='update-animal'),
    path('animal/deletar_animal/<int:pk>/', views.delete_animal, name='delete-animal'),

    # Vacina
    path('vacina/listar_vacinas/', views.view_vacina, name='listar-vacinas'),
    path('vacina/detalhar_vacina/<int:pk>/', views.detail_vacina, name='detalhar-vacina'),
    path('vacina/add_vacina/', views.add_vacina, name='add-vacina'),
    path('vacina/alterar_vacina/<int:pk>/', views.update_vacina, name='update-vacina'),
    path('vacina/deletar_vacina/<int:pk>/', views.delete_vacina, name='delete-vacina'),

    # Forma de Pagamento
    path('forma_pagamento/listar_formas_pagamento/', views.view_forma_pagamento, name='listar-formas_pagamento'),
    path('forma_pagamento/detalhar_forma_pagamento/<int:pk>/', views.detail_forma_pagamento, name='detalhar-forma_pagamento'),
    path('forma_pagamento/add_forma_pagamento/', views.add_forma_pagamento, name='add-forma_pagamento'),
    path('forma_pagamento/alterar_forma_pagamento/<int:pk>/', views.update_forma_pagamento, name='update-forma_pagamento'),
    path('forma_pagamento/deletar_forma_pagamento/<int:pk>/', views.delete_forma_pagamento, name='delete-forma_pagamento'),

    # Atendimento
    path('atendimento/listar_atendimentos/'             , views.view_atendimento, name='listar-atendimentos'),
    path('atendimento/detalhar_atendimento/<int:pk>/'   , views.detail_atendimento, name='detalhar-atendimento'),
    path('atendimento/add_atendimento/'                 , views.add_atendimento, name='add-atendimento'),
    path('atendimento/alterar_atendimento/<int:pk>/'    , views.update_atendimento, name='update-atendimento'),
    path('atendimento/deletar_atendimento/<int:pk>/'    , views.delete_atendimento, name='delete-atendimento'),

    # Pagamento
    path('pagamento/listar_pagamentos/'             , views.view_pagamento, name='listar-pagamentos'),
    path('pagamento/detalhar_pagamento/<int:pk>/'   , views.detail_pagamento, name='detalhar-pagamentos'),
    path('pagamento/add_pagamento/'                 , views.add_pagamento, name='add-pagamentos'),
    path('pagamento/alterar_pagamento/<int:pk>/'    , views.update_pagamento, name='update-pagamentos'),
    path('pagamento/deletar_pagamento/<int:pk>/'    , views.delete_pagamento, name='delete-pagamentos'),



]