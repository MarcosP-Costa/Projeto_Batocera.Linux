import os

def separarArquivos(arquivos):
    #passo lista com os arquivos da pasta e retorna os nomes e as extensões
    nomes = []
    extensoes = []
    for i in arquivos:
        nome, extensao = os.path.splitext(i)
        if extensao != '':
            nomes.append(nome)
            extensoes.append(extensao.replace(".", ""))
    return nomes, extensoes

def criarPastas(extensoes):
    #função para criar os diretórios caso não tenha
    for i in extensoes:
        i = i.replace(".", "")
        if(os.path.exists(f"./org/{i}") != True):
            os.makedirs(f"./org/{i}")
            print(f"Diretório {i} criado com sucesso!")

def moverArquivos(arquivos, extensoes):
    extensoes = set(extensoes)
    for e in extensoes:
        for a in arquivos:
            if(os.path.isdir(f"./org/{a}")) != True:
                if(e in a):
                    os.rename(f"./org/{a}", f"./org/{e}/{a}")
                

    print("cabooo, cabo programa")


arquivos = os.listdir("./org")

nomes, extensoes = separarArquivos(arquivos)

criarPastas(extensoes)

moverArquivos(arquivos, extensoes)










