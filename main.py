import streamlit as st
import os
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()

client = Client(os.getenv(key="account_sid"), os.getenv(key="auth_token"))
message = client.messages.create(
  from_=os.getenv(key="my_number"),
  body='Mensagem enviada',
  to='+5513996376382'
)

# print(os.getenv(key="account_sid"))
# print(os.getenv(key="auth_token"))
# print(os.getenv(key="my_number"))
