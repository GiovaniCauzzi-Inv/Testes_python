import csv
import requests
from os.path import dirname, realpath, isfile
from json import dump
import json



with open('produtos.csv') as arquivo:
    leituraArquivo=csv.reader(arquivo,delimiter=',')
    contadorLinha=0
    for linha in leituraArquivo:
        if contadorLinha == 0:
            print(f'Column names are {", ".join(linha)}')
            contadorLinha += 1
        else:
            print(f'\tCódigo: {linha[0]} Descrição: {linha[1]} Firmware: {linha[2]}.')
            contadorLinha += 1
    print(f'Processed {contadorLinha} lines.')

