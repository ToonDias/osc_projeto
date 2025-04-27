from dotenv import load_dotenv
import os
import psycopg2

load_dotenv()

db_user = os.getenv("DB_USER")
db_senha = os.getenv("DB_SENHA")
db_porta = os.getenv("DB_PORTA")
db_host = os.getenv("DB_HOST")
db_nome = os.getenv("DB_NOME")

# print(f'db usuario: {db_user}')
# print(f'db senha: {db_senha}')
# print(f'db porta: {db_porta}')
# print(f'db host: {db_host}')
# print(f'db nome: {db_nome}')

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
    cursor.execute("CREATE DATABASE db_oscar")
    print('Banco criado com sucesso!')
except psycopg2.errors.DuplicateDatabase:
    print('Banco já existe!')

cursor.close()
connection.close()

connection = psycopg2.connect(
    dbname = 'db_oscar',
    user = db_user,
    password = db_senha,
    host = db_host,
    port = db_porta
)

connection.autocommit = True

cursor = connection.cursor()

cursor.execute("""
               CREATE TABLE IF NOT EXISTS tbl_movie (
               id BIGSERIAL PRIMARY KEY NOT NULL,
               title VARCHAR(500) NOT NULL
               )
               """)

cursor.execute("""
               CREATE TABLE IF NOT EXISTS tbl_class (
               id BIGSERIAL PRIMARY KEY NOT NULL,
               description VARCHAR(500) NOT NULL
               )
               """)

cursor.execute("""
               CREATE TABLE IF NOT EXISTS tbl_category (
               id BIGSERIAL PRIMARY KEY NOT NULL,
               description VARCHAR(500) NOT NULL
               )
               """)

cursor.execute("""
               CREATE TABLE IF NOT EXISTS tbl_oscar (
               id BIGSERIAL PRIMARY KEY NOT NULL,
               ceremony INT NOT NULL,
               year INT NOT NULL
               )
               """)

cursor.execute("""
               CREATE TABLE IF NOT EXISTS tbl_nominees (
               id BIGSERIAL PRIMARY KEY NOT NULL,
               oscar_id BIGINT NOT NULL,
               class_id BIGINT NOT NULL,
               category_id BIGINT NOT NULL,
               movie_id BIGINT NOT NULL,
               name VARCHAR(500),
               nominees VARCHAR(500),
               winner BOOLEAN NOT NULL,
               detail TEXT,
               note TEXT
               )
               """)