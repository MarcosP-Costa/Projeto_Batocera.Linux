import os

arquivos = os.listdir("./org") #colocar aqui as roms que precisam ser renomeadas
siglas = ["(EUA)", "()"] #colocar aqui as siglas que precisam ser retiradas
roms = {"SNES": [0, 1], "PSX": [0, 1]}


def renomearROMs():
    for a in arquivos:
        for s in siglas:
            if s in a:
                new_a = a.strip().replace(f"{s}", "")
                os.rename(f"./org/{a}", f"./org/{new_a}")



