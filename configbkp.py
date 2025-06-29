import os
from datetime import datetime

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'chave-secreta-segura'

    PYTHONANYWHERE_PROJECT_PATH = '/home/Ascentia/Administrativo_IBAN'

    DATA_FOLDER_PATH = os.path.join(PYTHONANYWHERE_PROJECT_PATH, 'data')

    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(DATA_FOLDER_PATH, 'iban.db')

    VERSAO_APP = 'Beta'

    ANO_ATUAL = datetime.now().year

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    CAMPUS = {
        'Central':        '#0d6efd',  # primary
        'Concesso Elias': '#6c757d',  # secondary
        'Capão':          '#198754',  # success
        'Cidade Nova':    '#dc3545',  # danger
        'Perdigão':       '#ffc107',  # warning
        'Pitangui':       '#0dcaf0',  # info
    #   'Outro':          '#6f42c1',    # purple
    }

    # STATUS: nome → cor
    STATUS = {
        'Membro':       '#0d6efd',  # primary
        'Líder':        '#198754',  # success
        'Supervisor':   '#ffc107',  # warning
        'Não-Membro':   '#dc3545',  # danger
        'Inativo':      '#6c757d',  # secondary
    }

    TIPOS = ['Dízimo', 'Oferta'] #'Oferta Missionária'

    FORMAS = ['via Pix', 'em Espécie']

    JORNADA_CADASTRO_MEMBRO = {
        'class': 'bg-secondary', 'icon': 'bi-person-add',
        'label': 'Cadastro', 'categoria': 'Admissão'
    }

    JORNADA_CADASTRO_CTM = {
        'class': 'bg-secondary', 'icon': 'bi-person-fill-add',
        'label': 'Ingresso no CTM', 'categoria': 'Admissão'
    }

    JORNADA = {
        'Cadastro': JORNADA_CADASTRO_MEMBRO,

        'Status_Mudanca': {
            'class': 'bg-warning', 'icon': 'bi-person-check',
            'label': 'Mudança de Status', 'categoria': 'Atualizações'
        },

        'Campus_Mudanca': {
            'class': 'bg-warning', 'icon': 'bi-building',
            'label': 'Mudança de Campus', 'categoria': 'Atualizações'
        },

        'Desligamento': {
            'class': 'bg-danger', 'icon': 'bi-person-x',
            'label': 'Desligamento', 'categoria': 'Saída'
        },

        'Data_Recepcao_Mudanca': {
            'class': 'bg-warning', 'icon': 'bi-calendar-event',
            'label': 'Data Recepção Alterada', 'categoria': 'Atualizações'
        },

        # ----------- CTM -----------
        'Cadastro_Nao_Membro_CTM': JORNADA_CADASTRO_CTM,

        'Presenca': {
            'class': 'bg-success', 'icon': 'bi-check-circle',
            'label': 'Presença no CTM', 'categoria': 'Frequência'
        },

        # ----------- TESOURARIA -----------
        'Contribuicao': {
            'class': 'bg-primary', 'icon': 'bi-currency-dollar',
            'label': 'Contribuição', 'categoria': 'Financeiro'
        },

        'Edicao_Contribuicao': {
            'class': 'bg-primary', 'icon': 'bi-pencil-square',
            'label': 'Edição Contribuição', 'categoria': 'Financeiro'
        },
    }
