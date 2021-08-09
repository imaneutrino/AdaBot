import pandas
import ast
import requests
from settings import BASE_URL
from config.unityKeyNames import key_name
from helpers.convertUnityStringToInteger import get_unity_category_through_key, get_unity_status_through_key


def register_unidade(empreendimento_id, bloco_id, tipo_id, token, filename):
    file = pandas.read_excel(filename, index_col=None, na_values=['NA'], usecols="G:Q")
    unities = file.to_dict("records")

    final_dict = []

    for x in unities:
        x["cub"] = 0
        x["Status"] = get_unity_status_through_key(x["Status"])
        x["Categoria.1"] = get_unity_category_through_key(x["Categoria.1"])
        x["Conditions"] = list(ast.literal_eval(x["Conditions"]))
        final_dict.append(dict(zip(key_name, list(x.values()))))
    for unity in final_dict:
        response = requests.post(f"{BASE_URL}/interface/empreendimentos/{empreendimento_id}/blocos/{bloco_id}/tipos/{tipo_id}/unidades",
                                 json=unity,
                                 headers={'Authorization': token})
    print(response.status_code)
