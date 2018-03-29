#!bin/python
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
import boto3
import os
import io
from s3_boto_connection import *

#coletando variaveis de ambiente
PATH = os.environ['PATH']
BUCKET = os.environ['BUCKET']
PATH_COMPLETE = '%s/%s' % (BUCKET, PATH)
s3 = boto3.client('s3')

def load_json(file_):
	try:
		return json.loads(file_)
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


def scrape(event, context):
	print "Bucket: ", BUCKET
	result_object = read_s3_object(s3, BUCKET, PATH + '/result.json')

	print "RESULT CONTENT: ", result_object
	print

	#carregando json com ultima atualização
	try:
		last = load_json(result_object)
	except:
		raise

	#with open(result_object['Body'], 'w') as result:
	#	result.write('')

	settings = get_project_settings()
	settings.overrides['FEED_FORMAT'] = 'json'
	settings.overrides['FEED_URI'] = 's3://%s/%s/result.json' % (BUCKET, PATH)

	process = CrawlerProcess(settings)

	process.crawl(IntercambioSpider)

	try:
		process.start() # the script will block here until the crawling is finished
	except:
		print "proccess failed!"
		raise

		#recover()
		#log_generator('no_conection')


	try:
		current = load_json(read_s3_object(s3, BUCKET, PATH + '/result.json'))


		if current == last:
			log_generator('miss')


		new = diff(current, last)

		#se houver algo novo
		if new:
			#parseando contatos cadastrados
			cadastrados = parse_cadastros(read_s3_object(s3, BUCKET, PATH + '/cadastros/cadastrados.txt'))


	except:
		print  "DEU MERDA!"
		raise

	'''
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
	'''
	#def lambda_handler(event, context):
	#    return 'Hello from Lambda'
