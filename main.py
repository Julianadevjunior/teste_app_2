from twilio.rest import Client
import streamlit as st

account_sid = st.secrets["TWILIO"]["account_sid"]
auth_token = st.secrets["TWILIO"]["auth_token"]
twilio_phone = st.secrets["TWILIO"]["SENHA_SECRETA"]
st.write(account_sid, auth_token)
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='+18575678828',
  body='oi',
  to='+5513996260027'
)

print(message.sid)