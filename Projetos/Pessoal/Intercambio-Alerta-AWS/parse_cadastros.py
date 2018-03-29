# -*- coding: utf-8 -*-

#função recebe um arquivo de cadastro e devolve uma lista de dicionarios com cada cadastro
def parse_cadastros(cadastrados):
    cadastros_list = []

    #separando as linhas
    cadastros_raw = cadastrados.split('\n')
    #tirando elemento nulo
    cadastros_raw.pop()

    for cadastro in cadastros_raw:
        print "CADASTRO: " + cadastro
        cadastros_list.append({'nome': cadastro.split(': ')[0], 'email': cadastro.split(': ')[1]})

    return cadastros_list
