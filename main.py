import streamlit as st

# Carrega a variável do ambiente (local) ou dos secrets (deploy)
def get_secret(key):
    try:
        # Modo local (usa .env)
        from dotenv import load_dotenv
        import os
        load_dotenv()
        return os.getenv(key)
    except:
        # Modo deploy (usa secrets do Streamlit)
        return st.secrets[key]

# Acessa a variável
SENHA_SECRETA = get_secret("SENHA_SECRETA")

# Resto do código...
st.write(SENHA_SECRETA)