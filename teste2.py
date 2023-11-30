import re

texto = "teste(abc)"
padrao = r"\((.*?)\)"

match = re.search(padrao, texto)

if match:
    valor_dentro_parenteses = match.group(0)
    print(valor_dentro_parenteses)
else:
    print("Nenhuma correspondência encontrada.")



#código para pegar entre parenteses
#usar no código principal