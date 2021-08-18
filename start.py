import os
import pandas
import shutil

from authentication import get_token
from tipo import register_tipo
from unidade import register_unidade
from empreendimento import get_empreendimento_id
from bloco import register_bloco

token = get_token()

source_dir = f"{os.getcwd()}/__process__"
target_dir = f"{os.getcwd()}/__processing__"
finished_dir = f"{os.getcwd()}/__processed__"

file_names = os.listdir(source_dir)

print("             ___           _______           ___")
print("            /   \         |       \         /   \\")
print("           /  ^  \        |  .--.  |       /  ^  \\")
print("          /  /_\  \       |  |  |  |      /  /_\  \\")
print("         /  _____  \   __ |  '--'  | __  /  _____  \\   __")
print("        /__/     \__\ (__)|_______/ (__)/__/     \__\ (__)")
print("*" * 20, "Starting", "*" * 20)


def start_app():
    bloco_id = 0
    for file_name in file_names:
        print(file_name)
        print(f"Moving file: {file_name}")
        shutil.move(os.path.join(source_dir, file_name), target_dir)
        print("File moved")
        empreendimento_id = get_empreendimento_id(f"{target_dir}/{file_name}")

        print(f"Processing File: {file_name}")
        pandas.read_excel(f"{target_dir}/{file_name}", index_col=None, na_values=['NA'], usecols="G:R")

        if bloco_id == 0:
            bloco_id = register_bloco(token, f"{target_dir}/{file_name}")

        tipo_id = register_tipo(bloco_id, token, f"{target_dir}/{file_name}")
        register_unidade(empreendimento_id, bloco_id, tipo_id, token, f"{target_dir}/{file_name}")

        print("File processed!")

        print(f"Moving file {file_name} to '__processed__' folder!")
        shutil.move(os.path.join(target_dir, file_name), finished_dir)
        print("File moved")

        print("====================================================")
