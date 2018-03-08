# -*- coding: utf-8 -*-
from random import *
import sys

tipo = input ("Digite o tipo da matriz 1:INT 2:REAL 3:BIN \n")


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


    matriz.append(linha)

for i in range(populacao):
    for j in range(dimensao):
        print(matriz[i][j], end="")
