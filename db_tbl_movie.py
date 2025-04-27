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
lista_all_movie = []

for linha in linhas:
    lista_all_movie.append(linha['Movie'])

lista_unique_movie = list(set(lista_all_movie))

lista_movie_tratada = []

for item in lista_unique_movie:
    lista_movie_tratada.append(item.strip().replace('\n', '').replace('\r', ''))

lista_final = sorted(list(filter(None,lista_movie_tratada)))

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
        cursor.execute("INSERT INTO tbl_movie (title) VALUES (%s)",(item,))
        print("Titulo inserido com sucesso!")
    except psycopg2.errors.UniqueViolation:
        print("Esse Titulo já existe!")

cursor.close()
connection.close()
print('Tudo certo por aqui... verifique o banco!')