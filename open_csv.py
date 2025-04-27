from pathlib import Path
import csv
# import chardet

from nominees import nomminees

CAMINHO_CSV = Path(__file__).parent / 'base/datasheet_oscars.csv'

# with CAMINHO_CSV.open('rb') as arquivo:
#     leitor = arquivo.read()
#     resultado = chardet.detect(leitor)
#     print(resultado)


with CAMINHO_CSV.open('r', encoding='utf-8') as arquivo:
    leitor = csv.DictReader(arquivo, delimiter='\t')

    for linha in leitor:
        linha_tratada = limpar_linha(linha)
        print(linha_tratada)

    # for linha in leitor:
    #     linha_limpa = {k.strip(): v.strip() for k, v in linha.items()}
    #     print(linha_limpa)

    # objetos = []
    # for linha in leitor:
    #     item = nomminees(linha['Ceremony'], linha['Year'], linha['Class'], linha['Movie'], linha['Name'], linha['Nominees'], linha['Winner'], linha['Detail'], linha['Note'])
    #     objetos.append(item)

# for item in objetos:
#     if( 'T' in item.winner):
#         item.print_info()

    



    
