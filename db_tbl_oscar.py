import psycopg2
from dotenv import load_dotenv
import os

from pathlib import Path
import csv

load_dotenv()

db_user = os.getenv("DB_USER")
db_senha = os.getenv("DB_SENHA")
db_porta = os.getenv("DB_PORTA")
db_host = os.getenv("DB_HOST")
db_nome = 'db_oscar'

# csv
CAMINHO_CSV = Path(__file__).parent / 'base/datasheet_oscars.csv'

with CAMINHO_CSV.open('r', encoding='utf-8') as arquivo:
    leitor = csv.DictReader(arquivo, delimiter='\t')
    linhas = list(leitor)

# manipulação
lista_all_ceremony = []
lista_all_year = []

for linha in linhas:
    lista_all_ceremony.append(linha['Ceremony'])
    lista_all_year.append(linha['Year'])

lista_unique_ceremony = list(set(lista_all_ceremony))
lista_unique_year = list(set(lista_all_year))

lista_ceremony_str_tratada = []
lista_year_str_tratada = []

for item in lista_unique_ceremony:
    lista_ceremony_str_tratada.append(str(item).strip().replace('\n', '').replace('\r', ''))

for item in lista_unique_year:
    lista_year_str_tratada.append(str(item[:4]).strip().replace('\n', '').replace('\r', ''))

lista_str_ceremony_final = list(filter(None,lista_ceremony_str_tratada))
lista_str_year_final = list(filter(None,lista_year_str_tratada))

lista_ceremony_final = [int(item) for item in lista_str_ceremony_final]
lista_year_final = [int(item) for item in lista_year_str_tratada]

dados = list(zip(sorted(lista_ceremony_final), sorted(lista_year_final)))

# print(dados, len(dados))

# conexão com banco.
connection = psycopg2.connect(
    dbname = db_nome,
    user = db_user,
    password = db_senha,
    host = db_host,
    port = db_porta
)

connection.autocommit = True

cursor = connection.cursor()

try:
    cursor.executemany("INSERT INTO tbl_oscar (ceremony, year) VALUES (%s, %s)", dados)
    print("Todos os dados foram inseridos com sucesso!")
except psycopg2.errors.UniqueViolation:
    print("Algum registro já existe!")

cursor.close()
connection.close()
print('Tudo certo por aqui... verifique o banco!')