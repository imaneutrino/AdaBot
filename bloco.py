import requests
from settings import BASE_URL
from excel_functions.excel import bloco_information
from empreendimento import get_empreendimento_id


def register_bloco(token, filename):
    bloco = bloco_information(filename)
    empreendimento_id = get_empreendimento_id(filename)
    response = requests.post(f"{BASE_URL}/interface/empreendimentos/{empreendimento_id}/blocos",
                             data=bloco,
                             headers={'Authorization': token})
    bloco_id = response.json()["data"]["id"]
    return bloco_id
