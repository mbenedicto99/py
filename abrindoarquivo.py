#!/usr/bin/python

import sys

try:
	File = open('myfile.txt')

except IOError as e:
		print ("ERRO! Arquivo nao pode ser aberto!\r\n" +
			"ERRO NUMERO: {0}\r\n". format(e.errno) +
			"ERRO TEXTO: {0}". format(e.strerror))

else:
	print ("Ok! Arquivo aberto.")
	File.close();
