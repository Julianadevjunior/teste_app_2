import streamlit as st
import os
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()
account_sid = st.secrets["TWILIO"]["account_sid"]  # Acessa a seção TWILIO
auth_token = st.secrets["TWILIO"]["auth_token"]
twilio_phone = st.secrets["TWILIO"]["SENHA_SECRETA"]

if st.button("Enviar"):
  client = Client(account_sid, auth_token)
  message = client.messages.create(
    from_=twilio_phone,
    body='Mensagem enviada',
    to='+5513996376382'
  )

# print(os.getenv(key="account_sid"))
# print(os.getenv(key="auth_token"))
# print(os.getenv(key="my_number"))
