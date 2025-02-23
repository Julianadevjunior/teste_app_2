import datetime

from twilio.rest import Client
import streamlit as st
import pandas as pd
import os

import mysql.connector

# Conexão com o MySQL
conexao = mysql.connector.connect(
    host='127.0.0.1',  # Ou 'localhost'
    user='root',  # Seu usuário
    password='4m0@p40Ma',  # Sua senha
    database='teste'  # Nome do banco de dados
)

# Executar a conexão do comando acima
cursor = conexao.cursor()
nome = "Luis"
telefone = "11998542631"
bairro = "Ocian"
valor = 380000
descricao = "Lazer completo"
data_in = datetime.datetime.today().now()
data_upload = datetime.datetime.today().now()
data_agenda = datetime.datetime.today().now()


# CREATE
def create(nome="", telefone="", bairro="", valor="", descricao="", data_in="", data_update="", data_agenda=""):
    comando = f'INSERT INTO tabela_teste (nome, telefone, bairro, valor, descricao, data_in, data_upload, data_agenda) VALUES ("{nome}", "{telefone}", "{bairro}", "{valor}", "{descricao}", "{data_in}", "{data_upload}", "{data_agenda}")'
    cursor.execute(comando)  # EXECUTAR O COMANDO
    conexao.commit()  # SALVA NO BANCO DE DADOS


# READ
def read(tabela):
    comando = f'SELECT * FROM {tabela}'
    cursor.execute(comando)  # EXECUTAR O COMANDO
    resultado = cursor.fetchall()
    return resultado


# UPDATE
def update(valor, idx, coluna):
    comando = f'UPDATE tabela_teste SET {coluna} = "{valor}" WHERE idtabela_teste = {idx}'
    cursor.execute(comando)  # EXECUTAR O COMANDO
    conexao.commit()  # SALVA NO BANCO DE DADOS


# DELETE
def delete(idx):
    comando = f'DELETE FROM tabela_teste WHERE idtabela_teste = {idx}'
    cursor.execute(comando)  # EXECUTAR O COMANDO
    conexao.commit()  # SALVA NO BANCO DE DADOS


# create(nome, telefone, bairro, valor, descricao, data_in, data_upload, data_agenda)

for item in read("tabela_teste"):
    st.text(item[0])

print(st.secrets["TWILIO"]["passwordmysql"])

# Fechar conexão
cursor.close()
conexao.close()
