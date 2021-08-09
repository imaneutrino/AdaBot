import requests
from settings import BASE_URL
from excel_functions.excel import bloco_information

def register_bloco(empreendimento_id, token, filename):
    bloco = bloco_information(filename)
    response = requests.post(f"{BASE_URL}/interface/empreendimentos/{empreendimento_id}/blocos",
                             data=bloco,
                             headers={'Authorization': token})
    bloco_id = response.json()["data"]["id"]
    return bloco_id
