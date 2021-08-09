import requests
from settings import BASE_URL
from excel_functions.excel import tipo_information


def register_tipo(empreendimento_id, bloco_id, token, filename):
    tipo = tipo_information(filename)
    response = requests.post(f"{BASE_URL}/interface/empreendimentos/{empreendimento_id}/blocos/{bloco_id}/tipos",
                             data=tipo, headers={'Authorization': token})
    tipo_id = response.json()["data"]["id"]
    return tipo_id
