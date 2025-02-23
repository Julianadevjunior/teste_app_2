import streamlit as st
import os
from dotenv import load_dotenv
from twilio.rest import Client
import datetime
import time

# Inicializa o estado da sessão para armazenar o alarme
if "alarme" not in st.session_state:
    st.session_state.alarme = None
    st.session_state.alarme_ativado = False


def definir_alarme():
  st.title("⏰ Definir Alarme")

  data = st.date_input("Insira a data")
  hora = st.time_input("Insira a hora")

  if st.button("Definir Alarme"):
    data_hora = datetime.datetime.combine(data, hora)
    st.session_state.alarme = data_hora
    st.session_state.alarme_ativado = True
    st.success(f"Alarme definido para {data_hora.strftime('%d/%m/%Y %H:%M')}")

# Função para verificar se o alarme deve tocar


def verificar_alarme(tel):
  # Verifica o alarme em tempo real sem travar o Streamlit

  load_dotenv()
  account_sid = st.secrets["TWILIO"]["account_sid"]  # Acessa a seção TWILIO
  auth_token = st.secrets["TWILIO"]["auth_token"]
  twilio_phone = st.secrets["TWILIO"]["SENHA_SECRETA"]

  if st.session_state.alarme and st.session_state.alarme_ativado:
    agora = datetime.datetime.now()
    if agora >= st.session_state.alarme:
      st.session_state.alarme_ativado = False  # Desativa o alarme após tocar
      st.warning("⏰ Alarme tocando agora!")
      for _ in range(3):  # Reproduz o som 3 vezes
        client = Client(account_sid, auth_token)
        message = client.messages.create(
          from_=twilio_phone,
          body='Mensagem enviada',
          to='+5513996376382'
        )
  client = Client(account_sid, auth_token)
  message = client.messages.create(
    from_=twilio_phone,
    body='Mensagem enviada',
    to=tel
  )

  # Chama a função para definir o alarme


definir_alarme()
telefone = st.text_input(label="telefone")
verificar_alarme(telefone)
print('oi')



