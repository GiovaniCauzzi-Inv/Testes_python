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

#{"Op":"OPALT-202970-1","Code":"1000005319305","Filial":0,"Information":{"ERPName":"INV-13630","Firmware":"I:\\Documentos\\Softwares\\STM8\\STM8S003F3\\Inv-136\\136v60\\136v60_0.2.0.hex","Description":"ACIONADOR ELETRONICO INV-136 13630 ()","TestScript":"I:/Teste_Producao/INV-136M5/TF;INV-136.html","Stock":1,"ProductCode":"17114"},"ProductSteps":[{"Description":"CONFIRMAR OP-","Firmware":"","Script":"","Cod":1,"Sequence":50},{"Description":"SEPARAR MATERIAL-","Firmware":"","Script":"","Cod":2,"Sequence":100},{"Description":"DESPAINELIZAR-","Firmware":"","Script":"","Cod":13,"Sequence":150},{"Description":"GRAVAR FW-","Firmware":"","Script":"","Cod":14,"Sequence":200},{"Description":"MONTAR-","Firmware":"","Script":"","Cod":15,"Sequence":250},{"Description":"REVISAR-","Firmware":"","Script":"","Cod":8,"Sequence":300},{"Description":"ENCAIXOTAR-","Firmware":"","Script":"","Cod":17,"Sequence":350},{"Description":"TESTAR TESTE FINAL-","Firmware":"I:\\Documentos\\FirmwaresDeTeste\\INV-13600\\136at_v1_0.2.0.hex","Script":"I:\\Teste_Producao\\INV-136M5\\TF;INV-136.html","Cod":18,"Sequence":400},{"Description":"FINALIZAR ORDEM DE PRODUÇÃO-","Firmware":"","Script":"","Cod":9,"Sequence":450},{"Description":"TRANSPORTAR-EXPEDICAO","Firmware":"","Script":"","Cod":42,"Sequence":500}],"LabelType":"PRODUTO PRONTO","Children":null,"Status":"Tested"}