import streamlit as st
from dotenv import load_dotenv
import os

# Carrega variáveis do .env
load_dotenv()  # Certifique-se de ter o arquivo .env na raiz do projeto

st.title("Tela Teste")

# Recupera a senha secreta do .env
SENHA_SECRETA = os.getenv("SENHA_SECRETA")  # Adicione esta variável no seu .env

# Campo para digitar a senha
senha_digitada = st.text_input("Digite um número")

# Verificação
if senha_digitada == SENHA_SECRETA:
    st.success("Certo! 🎉")  # Melhor que print() para exibir no Streamlit
else:
    st.error("Errado! ❌")

if not SENHA_SECRETA:
    st.warning("Variável de ambiente SENHA_SECRETA não encontrada!")
    st.stop()  # Para a execução do app