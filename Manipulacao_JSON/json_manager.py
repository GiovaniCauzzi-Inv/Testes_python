import requests
from os.path import dirname, realpath, isfile
from json import dump
import json



class JsonManager:
    def __init__(self):
        self.path = dirname(realpath(__file__)) +'/'

    def create_json(self,file,dataInput): #{"nome": "giovani", "code": "13820938"}
        path_data_json= self.path+ file

        if not isfile(path_data_json):
            with open(path_data_json,'w') as f:
                dump(dataInput,f, indent=2, separators=(',',': '))
            return True
        else:
            return False

serialNumber = 1000005319305
urlAPI="http://rast.inova.ind.br/api/effective/products/" #http://rast.inova.ind.br/api/effective/products/1000005319305
 
response = requests.get(urlAPI+str(serialNumber)) 
responseSTR=response.text

if __name__== '__main__':
    jmanager = JsonManager()
    jmanager.create_json('data/data.json',response.json()) 

Objeto=json.loads(responseSTR)
print(Objeto['Information']['Firmware'])

for items in Objeto['Information']:
    print(Objeto['Information'][items])


variavel=123456
teste={"Produto": "INV-30910","CodProduto": ""+str(variavel)+ "","Gravador": "Renesas E2 Lite","Img_Gravador": "Renesas E2 Lite.png","BsGravacao":"NA","SupGravacao":"NA","Rastreamento": "true","Tst_State": {"1":"SetupInicial","2":"ScamGravador","3":"StartRastreamento","4":"GravaFirmware"}}
print(type(teste))
print(teste['CodProduto'])