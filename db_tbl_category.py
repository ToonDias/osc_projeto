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
lista_all_category = []

for linha in linhas:
    lista_all_category.append(linha['Category'])

lista_unique_category = list(set(lista_all_category))

lista_category_tratada = []

for item in lista_unique_category:
    lista_category_tratada.append(str(item).strip().replace('\n', '').replace('\r', ''))

lista_final = sorted(list(filter(None,lista_category_tratada)))

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

for item in lista_final:
    try:
        cursor.execute("INSERT INTO tbl_category (description) VALUES (%s)",(item,))
        print("Descrição inserida com sucesso!")
    except psycopg2.errors.UniqueViolation:
        print("Essa descrição já existe!")

cursor.close()
connection.close()
print('Tudo certo por aqui... verifique o banco!')