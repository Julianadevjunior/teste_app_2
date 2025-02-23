import datetime
from twilio.rest import Client
import streamlit as st
import pandas as pd
import os
import requests
link_google = "https://docs.google.com/spreadsheets/d/1NMM-IHZgF3aM0kqqDcGq_iRakOt5hogzkqxSrb2zK2E/edit?usp=sharing"
Código_de_implantação = "AKfycbxazn8Ci1UJw68ujjuXAY4PGfN-eOaTbgWWzZCwQkCogIwawe2OPWtVkRgC8KywSKo"
url_planilha = "https://script.google.com/macros/s/AKfycbxazn8Ci1UJw68ujjuXAY4PGfN-eOaTbgWWzZCwQkCogIwawe2OPWtVkRgC8KywSKo/exec"

# Link correto de implantação do Google Apps Script
codigo_implantacao = "AKfycbxazn8Ci1UJw68ujjuXAY4PGfN-eOaTbgWWzZCwQkCogIwawe2OPWtVkRgC8KywSKo"
url = f"https://script.google.com/macros/s/{codigo_implantacao}/exec"

# Faz a requisição
response = requests.get(url)

# Verifica o conteúdo da resposta
if response.status_code == 200:
    try:
        data = response.json()
        df = pd.DataFrame(data[1:], columns=data[0])  # Cabeçalho + dados
        st.dataframe(df)
    except requests.exceptions.JSONDecodeError:
        st.error("Erro ao decodificar JSON. Verifique a resposta da URL.")
else:
    st.error(f"Erro na requisição: {response.status_code}")

