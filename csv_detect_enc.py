from pathlib import Path
import chardet

CAMINHO_CSV = Path(__file__).parent / 'base/datasheet_oscars.csv'

with CAMINHO_CSV.open('rb') as arquivo:
    leitor = arquivo.read()
    resultado = chardet.detect(leitor)
    print(resultado)