from template_parser  import *
from parse_cadastros import *
from send_email import *
import os 
#send_email('thiagotosto@gmail.com', {'subject': 'boas vindas!', 'body': template_parser({'nome': 'Amanda Cortez'}, 'templates/boas_vindas.txt')})

PATH = os.environ['PATH']

old_cadastrados = parse_cadastros(PATH + '/cadastros/ultimos_cadastrados.txt')
new_cadastrados = parse_cadastros(PATH + '/cadastros/cadastrados.txt')

send_email(cadastro['email'] ,{'subject':'boas vindas!', 'body': template_parser({'nome': cadastro['nome'], 'msg': new}, PATH +'/templates/boas_vindas.txt')})
