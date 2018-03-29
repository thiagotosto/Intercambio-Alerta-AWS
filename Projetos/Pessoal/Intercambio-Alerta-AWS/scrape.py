# -*- coding: utf-8 -*-

import scrapy
from scrapy.crawler import CrawlerProcess
from intercambio_spider import *
from scrapy.utils.project import get_project_settings
import json
from send_email import *
from template_parser import *
from parse_cadastros import *
from log_generator import *
import sys
import shutil
#import boto3

PATH = '/home/ttosto_estag/Thiago/Projetos/Pessoal/Intercambio-Alerta-AWS/'

def load_json(file):
	try:
		with open(file) as json_file:
			return json.load(json_file)
	except ValueError:
		raise
		#sys.exit(0)

#recebe duas listas e retorna o elemento diferente
def diff(lista1, lista2):
	for lo in lista1:
		teste = False
		for li in lista2:
			if lo['text'] == li['text']:
				teste = True
		if not teste:
			return lo['text'].encode('utf-8')

	return False

def recover():
	with open(PATH +'/result.json', 'w') as result:
		shutil.copyfile(PATH + '/result-bkp.json', PATH + '/result.json')



#carregando json com ultima atualização
try:
	last = load_json(PATH +'/result.json')
except:
	raise

with open(PATH +'/result.json', 'w') as result:
	result.write('')

settings = get_project_settings()
settings.overrides['FEED_FORMAT'] = 'json'
settings.overrides['FEED_URI'] = PATH + '/result.json'

process = CrawlerProcess(settings)


process.crawl(IntercambioSpider)
try:
	process.start() # the script will block here until the crawling is finished
except:
	print '\n\n\n\nPassei aqui\n\n\n\n\n'
	recover()
	log_generator('no_conection')


try:
	current = load_json(PATH +'/result.json')


	if current == last:
		log_generator('miss')


	new = diff(current, last)

	#se houver algo novo
	if new:
		#parseando contatos cadastrados
		cadastrados = parse_cadastros(PATH +'/cadastros/cadastrados.txt')

		#enviando para cada cadastrado
		for cadastro in cadastrados:
			send_email(cadastro['email'] ,{'subject':'alerta nova publicação', 'body': template_parser({'nome': cadastro['nome'], 'msg': new}, PATH +'/templates/alerta.txt')})

		#gerando log do hit
		log_generator('hit', "%s" % new)

		#atualizando bkp
		shutil.copyfile(PATH + '/result.json', PATH + '/result-bkp.json')

except ValueError:
	log_generator('no_conection')
	recover()

#def lambda_handler(event, context):
#    return 'Hello from Lambda'
