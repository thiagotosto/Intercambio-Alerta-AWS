#!/home/ttosto_estag/Thiago/Projetos/Globosat/Scrapy/bin/python
# -*- coding: utf-8 -*-
import os
from log_generator import *
from template_parser  import *
from parse_cadastros import *
from send_email import *
from lib import *

#send_email('thiagotosto@gmail.com', {'subject': 'boas vindas!', 'body': template_parser({'nome': 'Amanda Cortez'}, 'templates/boas_vindas.txt')})

PATH = os.environ['PATH']

old_cadastrados = parse_cadastros(PATH + '/cadastros/.ultimos_cadastrados.txt')
new_cadastrados = parse_cadastros(PATH + '/cadastros/cadastrados.txt')

novos = diff(new_cadastrados,  old_cadastrados)

if novos != None:
    print novos
    for novo in novos:
        send_email(novo['email'] ,{'subject':'boas vindas!', 'body': template_parser({'nome': novo['nome']}, PATH +'/templates/boas_vindas.txt')})

        #atualizando o arquivo ultimos com os novos cadastrados
        with open(PATH + '/cadastros/.ultimos_cadastrados.txt', 'a') as f:
            f.write('%s: %s' % (novo['nome'], novo['email']))

	log_generator('new_user', None, novo['nome'])
