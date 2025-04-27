from pathlib import Path
import csv
# import chardet

from nominees import nomminees

CAMINHO_CSV = Path(__file__).parent / 'base/datasheet_oscars.csv'

# with CAMINHO_CSV.open('rb') as arquivo:
#     leitor = arquivo.read()
#     resultado = chardet.detect(leitor)
#     print(resultado)


# with CAMINHO_CSV.open('r', encoding='utf-8') as arquivo:
#     leitor = csv.reader(arquivo, delimiter='\t')
    
#     lista_nomminees = []

#     linhas = list(leitor)
#     for linha in linhas[1:4]:
#         linha_tratada = [item.strip().replace('\n', '').replace('\r', '') for item in linha]
#         lista_nomminees.append(nomminees(*linha_tratada))


# lista_nomminees[1].print_info()
# lista_nomminees[1].print_info_type()

with CAMINHO_CSV.open('r', encoding='utf-8') as arquivo:
    leitor = csv.DictReader(arquivo, delimiter='\t')

    linhas = list(leitor)
    lista_dados = []
    for linha in linhas:
        lista_dados.append(linha['Class'])

    for item in list(set(lista_dados)):
        print(item)


    



    
