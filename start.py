import os
import pandas
import shutil

from authentication import get_token
from empreendimento import get_empreendimento_id
from bloco import register_bloco
from tipo import register_tipo
from unidade import register_unidade

token = get_token()

source_dir = f"{os.getcwd()}/Documents/Ada/__process__"
target_dir = f"{os.getcwd()}/Documents/Ada/__processing__"
finished_dir = f"{os.getcwd()}/Documents/Ada/__processed__"

file_names = os.listdir(source_dir)

print("             ___           _______           ___")
print("            /   \         |       \         /   \\")
print("           /  ^  \        |  .--.  |       /  ^  \\")
print("          /  /_\  \       |  |  |  |      /  /_\  \\")
print("         /  _____  \   __ |  '--'  | __  /  _____  \\  __")
print("        /__/     \__\ (__)|_______/ (__)/__/     \__\ (__)")
print("*" * 20, "Starting", "*" * 20)


def start_app():
    for file_name in file_names:
        print(f"Moving file: {file_name}")
        shutil.move(os.path.join(source_dir, file_name), target_dir)
        print("File moved")

        print(f"Processing File: {file_name}")
        file = pandas.read_excel(f"{target_dir}/{file_name}", index_col=None, na_values=['NA'], usecols="G:Q")

        empreendimento_id = get_empreendimento_id(f"{target_dir}/{file_name}")
        bloco_id = register_bloco(empreendimento_id, token, f"{target_dir}/{file_name}")
        tipo_id = register_tipo(empreendimento_id, bloco_id, token, f"{target_dir}/{file_name}")
        register_unidade(empreendimento_id, bloco_id, tipo_id, token, f"{target_dir}/{file_name}")
        print(register_unidade)

        print("File processed!")

        print(f"Moving file {file_name} to '__processed__' folder!")
        shutil.move(os.path.join(target_dir, file_name), finished_dir)
        print("File moved")

        print("====================================================")
