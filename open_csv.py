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
        print(linha)

    



    
