# -*- coding: utf-8 -*-
from random import *
import random
import numpy as np
import sys

class Population():
	"""docstring for ClassName"""
	def __init__(self):			
		tipo = input ("Digite o tipo da matriz 1:INT 2:REAL 3:BIN 4:INT_PERM \n")


		populacao = 10        # a nossa dimensao
		dimensao = 10
		matriz = []  # esta sera a nossa matriz



		for i in range(populacao):
		    linha = []  # certificar que começamos com uma linha vazia
		    for j in range(dimensao):
		        if(tipo==1):
		            num = randint(-5,10)
		            linha.extend([num])

		        if(tipo==2):
		            num = uniform(-10,10)
		            linha.extend([num])

		        if(tipo==3):
		            num = randint(0,1)
		            linha.extend([num])

		result = random.sample(range(-5,10), 10)

		for i in range(10):
			matriz.append(np.random.permutation(result))        
		         

		    

		for i in range(10):
			print matriz[i]



Population()