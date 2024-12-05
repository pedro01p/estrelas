import streamlit as st
import streamlit_authenticator as stauth
from time import sleep


# exibir infos

if "nome1" in st.session_state and "cpf1" in st.session_state and "responsavel1" in st.session_state and "foto1" in st.session_state:
 st.header(f"nome: {st.session_state["nome1"]}")
 st.header(f"cpf: {st.session_state["cpf1"]}")
 st.header(f"responsavel: {st.session_state["responsavel1"]}")

if "foto1" in st.session_state:
    if st.session_state["foto1"] is not None:
        st.image(
            st.session_state["foto1"], caption="Foto do aluno", width=300
        )
