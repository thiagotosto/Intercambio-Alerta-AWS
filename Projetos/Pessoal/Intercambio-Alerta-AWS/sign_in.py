#!/home/ttosto_estag/Thiago/Projetos/Globosat/Scrapy/bin/python
# -*- coding: utf-8 -*-
import os

def sign_in(name, email):
	PATH = os.environ['PATH'] + '/cadastros'

	with open(PATH +'/cadastrados.txt', 'a') as cadastro:
		cadastro.write(name +  ": " + email);

if __name__ == "__main__":
	print "Nome: ",
	name = raw_input()
	print "e-mail: ",
	email = raw_input()

	sign_in(name, email)
