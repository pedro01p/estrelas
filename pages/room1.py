import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import random
from io import BytesIO
import time
import webbrowser
from time import sleep
from PIL import Image
import pandas as pd 

#cores

st.markdown("""
        <style>
            /*Estilo para o título */
            h1 {
                color: #FFFCCC;
                font-size: 30px;
                font-weight: bold;
            }

        .stButton>button {
            width: 260px;
            background-color: green;
            color: white;     
            padding: 15px 30px;
            font-size: 16px;
            border-radius: 30px;
            cursor: pointer;
            display: flex;
            justify-content: center;
            align-items: left;
            margin: 0 auto;

        }

        .stButton>button:hover {
            background-color: darkred;  /* Cor do botão ao passar o mouse */
        }
        .bt1 >button {
            background-color: #777666;  /* Cor do botão 1 */
            color: white;  /* Cor do texto */
            font-size: 18px;
            border-radius: 10px;
            padding: 10px 20px;
            border: none;
            transition: background-color 0.3s ease;
        }
        .bt1 > button:hover {
            background-color: #777666;  /* Cor ao passar o mouse para o botão 1 */
        }
            
             .candidato > button {
            background-color: #777555;  /* cor para o botao de resultado */
            color: white;
            border-radius: 10px;
            padding: 10px 20px;
            border: none;
            font-size: 18px;
        }

        .button_candidato2 > button:hover {
            background-color: #0000FF;  /* Cor ao passar o mouse para o botão do Candidato 2 */
        }

        .col5
            {

            justify-content: center;
            align: center;
            
            }

        </style>
            
    """, unsafe_allow_html=True)

# Configuração inicial da págin


# Títulos e descrição
st.title("🗳️ Sistema de Votação")

st.write("Vote com cuidado! Veja com atenção o discurso de cada um, e então vote. Você só pode votar uma vez!")

st.write("")
st.write("")
st.write("")


# Variáveis de estado para armazenar votos
if "votos_candidato1" not in st.session_state:
    st.session_state.votos_candidato1 = 0

if "votos_candidato2" not in st.session_state:
    st.session_state.votos_candidato2 = 0

if "ja_votou" not in st.session_state:
    st.session_state.ja_votou = False

# Verifica se o usuário já votou

col1, col2 = st.columns(2)

with col1:
    if st.button("Discurso do candidato 1"):
        webbrowser.open("https://drive.google.com/file/d/11IVI3_s0NYogvjrYesEWxzz2KC7oO9Wv/view")
with col2:
        if st.button("Discurso do candidato 2"):
            webbrowser.open("https://drive.google.com/file/d/1AZausUdYaAfLX70AU1VNTdWBbg1MxvQd/view")

if st.session_state.ja_votou:
    st.warning("Você já votou! Obrigado por participar.")
else:
    # Botões de votação
    col3, col4 = st.columns(2)

    with col3:
        if st.button("Votar no Candidato 1"):  
            
            st.session_state.votos_candidato1 += 1
            st.session_state.ja_votou = True
            st.success("Seu voto foi registrado para o Candidato 1!")
 
    with col4:
        if st.button("Votar no Candidato 2"):
            st.session_state.votos_candidato2 += 1
            st.session_state.ja_votou = True
            st.success("Seu voto foi registrado para o Candidato 2!")

votos_can_1 = []

col5, col6 = st.columns(2)
with col5:
    st.image("data:image/jpeg;base64,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", width=160)
with col6:
    st.image("https://media.tenor.com/UPiEUVO2Q04AAAAe/mulch-mulch-dog.png", width=160)

#cofiguraçaodo botao resultado



#o botao agora

if st.button("Resultado", key="candidato", help="Ver resultado das eleições", use_container_width=True):
            st.session_state.votos_candidato2 += 1
            st.session_state.ja_votou = True
            st.success("Seu voto foi registrado para o Candidato 2!")
