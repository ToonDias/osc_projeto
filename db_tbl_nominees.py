import psycopg2
from dotenv import load_dotenv
import os
from pathlib import Path
import csv
from nominees import nomminees

load_dotenv()

db_user = os.getenv("DB_USER")
db_senha = os.getenv("DB_SENHA")
db_porta = os.getenv("DB_PORTA")
db_host = os.getenv("DB_HOST")
db_nome = 'db_oscar'

# csv
CAMINHO_CSV = Path(__file__).parent / 'base/datasheet_oscars.csv'

linhas_validas = []
linhas_invalidas_obg = []
linhas_invalidas_nsc = []

with CAMINHO_CSV.open('r', encoding='utf-8') as arquivo:
    leitor = csv.DictReader(arquivo, delimiter='\t')
    linhas = list(leitor)

    for linha in linhas:
        linha_ceremony = linha['Ceremony'].strip().replace('\n', '').replace('\r', '')
        linha_year = linha['Year'][:4].strip().replace('\n', '').replace('\r', '')
        linha_class = linha['Class'].strip().replace('\n', '').replace('\r', '')
        linha_category = linha['Category'].strip().replace('\n', '').replace('\r', '')
        linha_movie = linha['Movie'].strip().replace('\n', '').replace('\r', '')
        linha_name = linha['Name'].strip().replace('\n', '').replace('\r', '')
        linha_nominees = linha['Nominees'].strip().replace('\n', '').replace('\r', '')
        linha_wineer = bool(linha['Winner'].strip().replace('\n', '').replace('\r', ''))
        linha_detail = linha['Detail'].strip().replace('\n', '').replace('\r', '')
        linha_note = linha['Note'].strip().replace('\n', '').replace('\r', '')

        # linha_ceremony = linha['Ceremony']
        # linha_year = linha['Year'][:4]
        # linha_class = linha['Class']
        # linha_category = linha['Category']
        # linha_movie = linha['Movie']
        # linha_name = linha['Name']
        # linha_nominees = linha['Nominees']
        # linha_wineer = bool(linha['Winner'])
        # linha_detail = linha['Detail']
        # linha_note = linha['Note']


        if not linha_ceremony and not linha_year or not linha_class or not linha_category  or not linha_movie:
            linhas_invalidas_obg.append(linha)
            continue
        elif not linha_name or not linha_nominees:
            linhas_invalidas_nsc.append(linha)
            continue
        else:
            linhas_validas.append(linha)

print(f'Total de linhas validas: {len(linhas_validas)}')
print(f'Total de linhas invalidas por ausencia de dado obrigatorio: {len(linhas_invalidas_obg)}')
print(f'Total de linhas invalidas por ausencia de dado necessario: {len(linhas_invalidas_nsc)}')

# consultando banco para coletar os IDs
connection = psycopg2.connect(
    dbname = db_nome,
    user = db_user,
    password = db_senha,
    host = db_host,
    port = db_porta
)
connection.autocommit = True

cursor = connection.cursor()

cursor.execute("SELECT * FROM tbl_class")
all_class = cursor.fetchall()

cursor.execute("SELECT * FROM tbl_category")
all_category = cursor.fetchall()

cursor.execute("SELECT * FROM tbl_movie")
all_movie = cursor.fetchall()

cursor.execute("SELECT * FROM tbl_oscar")
all_oscar = cursor.fetchall()

# print(all_oscar)
# print(all_class)
# print(all_category)
# print(all_movie)

lista_nominees = []

for linha in linhas_validas:
    
    linha_ceremony = linha['Ceremony'].strip().replace('\n', '').replace('\r', '')
    linha_year = linha['Year'][:4].strip().replace('\n', '').replace('\r', '')
    linha_class = linha['Class'].strip().replace('\n', '').replace('\r', '')
    linha_category = linha['Category'].strip().replace('\n', '').replace('\r', '')
    linha_movie = linha['Movie'].strip().replace('\n', '').replace('\r', '')
    linha_name = linha['Name'].strip().replace('\n', '').replace('\r', '')
    linha_nominees = linha['Nominees'].strip().replace('\n', '').replace('\r', '')
    linha_wineer = linha['Winner'].strip().replace('\n', '').replace('\r', '')
    linha_detail = linha['Detail'].strip().replace('\n', '').replace('\r', '')
    linha_note = linha['Note'].strip().replace('\n', '').replace('\r', '')

    oscar_id = next((row[0] for row in all_oscar if row[1] == int(linha_ceremony) or row[2] == int(linha_year)), None)
    class_id = next((row[0] for row in all_class if row[1] == linha_class), None)
    category_id = next((row[0] for row in all_category if row[1] == linha_category), None)
    movie_id = next((row[0] for row in all_movie if row[1] == linha_movie), None)
    
    # print(oscar_id, class_id, category_id, movie_id)
    # print(type(oscar_id), type(class_id), type(category_id), type(movie_id))

    # (self, oscar_id, class_id, category_id, movie_id, name, nominees, winner, detail, note)

    item = nomminees(oscar_id, class_id, category_id, movie_id, linha_name, linha_nominees, linha_wineer, linha_detail, linha_note)
    lista_nominees.append(item)

print(f'Objetos criados: {len(lista_nominees)}')

dados = []
for n in lista_nominees:
    dados.append((n.oscar_id, n.class_id, n.category_id, n.movie_id, n.name, n.nominees, n.winner, n.detail, n.note))

# for dado in dados:
#     print(dado)

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
    cursor.executemany(
        """
        INSERT INTO tbl_nominees (oscar_id, class_id, category_id, movie_id, name, nominees, winner, detail, note)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """,
        dados
    )
    connection.commit()
    print("Todos os dados foram inseridos com sucesso!")
except psycopg2.errors.UniqueViolation:
    print("Algum registro já existe!")
except Exception as e:
    print(f"Ocorreu um erro: {e}")

cursor.close()
connection.close()
print('Tudo certo por aqui... verifique o banco!')