import psycopg2
from dotenv import load_dotenv
import os

from pathlib import Path

load_dotenv()

db_user = os.getenv("DB_USER")
db_senha = os.getenv("DB_SENHA")
db_porta = os.getenv("DB_PORTA")
db_host = os.getenv("DB_HOST")
db_nome = 'db_oscar'

connection = psycopg2.connect(
    dbname = db_nome,
    user = db_user,
    password = db_senha,
    host = db_host,
    port = db_porta
)

cursor = connection.cursor()

# Atores/Atrizes que mais venceram
cursor.execute("""
                SELECT name, COUNT(*) AS vitorias FROM tbl_nominees
                WHERE winner = TRUE
                GROUP BY name
                ORDER BY vitorias DESC
               """)

resultados_1 = cursor.fetchall()
print("Atores/atrizes que venceram mais vezes:")
for name, vitorias in resultados_1[:5]:
    print(f"{name}: {vitorias} vitórias")

print('--------------------')

# Categorias que Interestellar venceu
cursor.execute("""
                SELECT 
                c.description AS category_name, 
                o.year AS year, 
                o.ceremony AS ceremony
                FROM tbl_nominees n
                JOIN tbl_category c ON n.category_id = c.id
                JOIN tbl_oscar o ON n.oscar_id = o.id
                JOIN tbl_movie m ON n.movie_id = m.id
                WHERE n.winner = TRUE 
                AND m.title = 'Interstellar'
               """)

resultados_2 = cursor.fetchall()
print("Categorias que 'Interstellar' venceu:")
for category_name, year, ceremony in resultados_2[:5]:
    print(f"Categoria: {category_name} - Ano: {year} - Cerimonia: {ceremony}")

print('--------------------')

# Diretores indicados mais de 2 vezes
cursor.execute("""
               SELECT nominees, COUNT(*) AS indicacoes FROM tbl_nominees
                GROUP BY nominees
                HAVING COUNT(*) > 2
                ORDER BY COUNT(*) DESC;
               """)

resultados_3 = cursor.fetchall()
print("Diretores que foram indicados mais de 2 vezes:")
for nomeinees, indicacoes in resultados_3[:5]:
    print(f"{nomeinees}: {indicacoes} indicações")

cursor.close()
connection.close()

# Exportando resultados em .txt

caminho_arquivo_txt = Path(__file__).parent / 'relatorios/questao_1.txt'

with open(caminho_arquivo_txt, mode='w', encoding='utf-8') as file:
    file.write("Atores/atrizes que venceram mais vezes:\n")
    for name, vitorias in resultados_1:
        file.write(f"{name}: {vitorias} vitórias\n")

caminho_arquivo_txt = Path(__file__).parent / 'relatorios/questao_2.txt'

with open(caminho_arquivo_txt, mode='w', encoding='utf-8') as file:
    file.write("Categorias que 'Interstellar' venceu:\n")
    for category_name, year, ceremony in resultados_2:
     file.write(f"Categoria: {category_name} - Ano: {year} - Cerimonia: {ceremony}\n")

caminho_arquivo_txt = Path(__file__).parent / 'relatorios/questao_3.txt'

with open(caminho_arquivo_txt, mode='w', encoding='utf-8') as file:
    file.write("Diretores que foram indicados mais de 2 vezes:\n")
    for nomeinees, indicacoes in resultados_3:
        file.write(f"{nomeinees}: {indicacoes} indicações\n")