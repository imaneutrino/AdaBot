import requests
from settings import BASE_URL
from excel_functions.excel import tipo_information
from empreendimento import get_empreendimento_id


def register_tipo(bloco_id, token, filename):
    tipo = tipo_information(filename)
    empreendimento_id = get_empreendimento_id(filename)
    response = requests.post(f"{BASE_URL}/interface/empreendimentos/{empreendimento_id}/blocos/{bloco_id}/tipos",
                             data=tipo, headers={'Authorization': token})
    tipo_id = response.json()["data"]["id"]
    return tipo_id
