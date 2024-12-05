import streamlit as st
import streamlit_authenticator as stauth
from time import sleep

#Barra lateral0101010
st.set_page_config(initial_sidebar_state="collapsed")

# REGISTRO / LOGIN DO ALUNO para verificação

def ver_preenchidos(campos): # funcao que ve se cada entrada foi preenchida
    return all(campos.values())

# informações sobre o aluno

foto = st.file_uploader("Foto do aluno:", type=["jpg", "jpeg", "png"])
nome = st.text_input("Nome do aluno:", value="", placeholder="Digite aqui...")
cpf = st.text_input("CPF do aluno:", placeholder="Digite aqui...")
responsavel = st.text_input("Responsável do aluno:", value="", placeholder="Digite aqui...")
id_es = st.text_input("Número ID da escola:", value="", placeholder="Digite aqui...")

if foto is not None:
    st.image(foto, caption="Foto do aluno", width=100)

# id's de quais escolas participam do site

ids_escolas = [
    
    "123",
    "12",
    "1"

]

# dicionario dos nomes dos alunos ( correspondendo ao ID de sua escola )

escolas_alunos = {

    "1": [
        "Max Cavalera",
        "Jasmine",
        "Lain",
        "Bruno Reis"],
        
    "12": ["Uff referencias", 
           "Savio Cunha", 
           "Patrick Bateman", 
           "Jair Messias Bolsonaro", 
           "Luís Inácio Lula da Silva"],

    "123": ["Alexi Laiho", 
            "Deftonerson Scrobblers da Silva", 
            "Chris Jones", 
            "Evgeny Linnik"]

}

# dicionarios de cada informação do aluno

campos_aluno = {
    'Nome': nome,
    'CPF': cpf,
    'Responsável': responsavel,
    'Foto': foto,
    'Id da ecola': id_es
}

# com base nas informações do aluno, ele é redirecionado para as paginas corresnondentes das escolas

if st.button("Concluir"):
    if not ver_preenchidos(campos_aluno):
     st.error("Por favor, preencha todos os campos.")
    elif id_es not in escolas_alunos:
     st.error("Este ID não está cadastrado.")
    elif nome not in escolas_alunos[id_es]:
     st.error("Nome do aluno não corresponde ao ID da escola")
    elif len(str(cpf)) != 11:
     st.error("CPF inválido")
    elif not cpf.isdigit():
     st.error("CPF tem que ser só número, meu parceiro!")
    elif not id_es.isdigit():
     st.error("IDs tem que ser só numero, meu parceiro!")
    else:
        cpf = int(cpf)
        st.session_state["nome1"] = nome
        st.session_state["cpf1"] = cpf
        st.session_state["responsavel1"] = responsavel
        st.session_state["foto1"] = foto
        st.success("Concluído com sucesso!")
        sleep(0.5)
        if id_es == "1":
        

            st.switch_page("pages/room1.py")
        elif id_es == "12":
            st.switch_page("pages/room12.py")
        elif id_es == "123":
            st.switch_page("pages/room123.py")