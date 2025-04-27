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
                id BIGSERIAL NOT NULL,
                title VARCHAR(500) NOT NULL,
                PRIMARY KEY (id),
                UNIQUE (title)
               )
               """)

cursor.execute("""
               CREATE TABLE IF NOT EXISTS tbl_class (
                id BIGSERIAL NOT NULL,
                description VARCHAR(255) NOT NULL,
                PRIMARY KEY (id),
                UNIQUE (description)
                )
               """)

cursor.execute("""
               CREATE TABLE IF NOT EXISTS tbl_category (
                id BIGSERIAL NOT NULL,
                description VARCHAR(500) NOT NULL,
                PRIMARY KEY (ID),
                UNIQUE(description)
                )
               """)

cursor.execute("""
               CREATE TABLE IF NOT EXISTS tbl_oscar (
                id BIGSERIAL NOT NULL,
                ceremony INT NOT NULL,
                year INT NOT NULL,
                PRIMARY KEY (id),
                UNIQUE(ceremony)
                )
               """)

cursor.execute("""
               CREATE TABLE tbl_nominees (
                id BIGSERIAL NOT NULL,
                oscar_id BIGINT NOT NULL,
                class_id BIGINT NOT NULL,
                category_id BIGINT NOT NULL,
                movie_id BIGINT NOT NULL,
                name VARCHAR(500),
                nominees VARCHAR(500),
                winner BOOLEAN NOT NULL DEFAULT FALSE,
                detail TEXT,
                note TEXT,
                PRIMARY KEY (id),
                FOREIGN KEY (oscar_id) REFERENCES tbl_oscar(id) ON UPDATE CASCADE ON DELETE CASCADE,
                FOREIGN KEY (class_id) REFERENCES tbl_class(id) ON UPDATE CASCADE ON DELETE CASCADE,
                FOREIGN KEY (category_id) REFERENCES tbl_category(id) ON UPDATE CASCADE ON DELETE CASCADE,
                FOREIGN KEY (movie_id) REFERENCES tbl_movie(id) ON UPDATE CASCADE ON DELETE CASCADE
                )
               """)