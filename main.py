import datetime
from twilio.rest import Client
import streamlit as st
import pandas as pd
import os
import requests


url = f"https://script.google.com/macros/s/AKfycbwMnd9TxGAv0ibanXgv9fq81lNXK3v2s4DvH0RYUqSjx9jh2pCEVSuO2Sy7EDq3lmbp/exec"

# # Faz a requisição
# response = requests.get(url)
#
# # Verifica o conteúdo da resposta
# if response.status_code == 200:
#     print(response.json())
#     try:
#         data = response.json()
#         df = pd.DataFrame(data[1:], columns=data[0])  # Cabeçalho + dados
#         st.dataframe(df)
#     except requests.exceptions.JSONDecodeError:
#         st.error("Erro ao decodificar JSON. Verifique a resposta da URL.")
# else:
#     st.error(f"Erro na requisição: {response.status_code}")

