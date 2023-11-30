import os

diretorios = os.listdir("D:/RECUPERAR TUDO/BATOCERA/Recovered/HD-Marcolino(D)/Arquivos Existentes/Batocera/ROMs")
roms = {
    
}


for pasta in diretorios: #aqui transforma o dicionario ROMS em um com nome = pasta e [] roms
    roms[pasta] = []
    for rom in os.listdir(f"D:/RECUPERAR TUDO/BATOCERA/Recovered/HD-Marcolino(D)/Arquivos Existentes/Batocera/ROMs/{pasta}"):
        roms[pasta].append(rom)
        if "(" in rom:
            print(rom)




    

