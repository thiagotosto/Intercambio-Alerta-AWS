from send_email import *
from template_parser import *
from parse_cadastros import *

PATH = os.environ['PATH']

cadastrados = parse_cadastros(PATH + '/cadastros/cadastrados.txt')

'''
for cadastro in cadastrados:
    send_email(cadastro['email'] ,{'subject':'boas vindas', 'body': template_parser(cadastro['nome'], 'templates/boas_vindas.txt')})
'''

send_email(cadastrados[len(cadastrados)-1]['email'], {'subject':'boas vindas!', 'body': template_parser({'nome': cadastrados[len(cadastrados)-1]['nome']}, PATH + '/templates/boas_vindas.txt')})
