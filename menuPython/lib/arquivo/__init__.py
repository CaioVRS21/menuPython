from menuPython.lib.interface import *


def arquivoExiste(arquivo):
    try:
        a = open(arquivo, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criaArquivo(arquivo):
    try:
        a = open(arquivo, 'wt+')
        a.close()
    except:
        print('ERRO! Problemas na criação do arquivo')
    else:
        print(f'Arquivo {arquivo} criado com sucesso')


def lerArquivo(arquivo):
    try:
        a = open(arquivo, 'rt')
    except:
        print('ERRO na leitura do arquivo')
    else:
        cabecalho('Pessoas Cadastradas')
        print(a.readlines())