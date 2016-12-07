#!/usr/bin/python

import os
import shutil
i=1

newdir=('/home/mbenedicto/Downloads/CRIADOPELOPYTHON')

while os.path.exists(newdir): #Acrescenta "1" no nome do diretororio se existir.
	newdir+=str(i)
	i+=1

os.makedirs(newdir)

lis=[]

lis=os.listdir('/home/mbenedicto/Downloads')

for file in lis:
	print file
	if file=='__file__' #Se for o script da continue, __file__ igual a $0
		continue
	shutil.move(file,newdir)

