import streamlit as st

if "feedback_list" not in st.session_state:
    st.session_state.feedback_list = []

# Estilo personalizado
st.markdown("""
    <style>
        body {
            background-color: #f9fbfd;
        }
        h1 {
            color: #356abb;
            font-size: 36px;
            font-weight: bold;
            text-align: center;
            margin-bottom: 30px;
        }
        .stButton button {
            background-color:#628af0 ;
            color: white;
            border: none;
            padding: 10px 20px;
            font-size: 16px;
            border-radius: 8px;
            transition: background-color 0.3s;
        }
        .stButton button:hover {
            background-color: ;
        }
        .feedback-box {
            background-color: #eef7ff;
            border: 1px solid #cce5ff;
            border-radius: 10px;
            padding: 15px;
            margin-bottom: 10px;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
        }
        .feedback-box h6 {
            color: #5c85d6;
            margin: 0 0 5px 0;
            font-weight: bold;
        }
        .feedback-box p {
            color: #333;
            margin: 0;
        }
    </style>
""", unsafe_allow_html=True)

st.title("🌟 Feedbacks")

st.write("")
st.write("")

name = st.text_input("Digite seu nome:")
feedback = st.text_area("Deixe seu feedback:")
st.success("Obrigado pelo seu feedback!")

genre = st.radio(
    "Como você avalia nosso site?",
    ["⭐", "***⭐⭐***", "⭐⭐⭐", "⭐⭐⭐⭐", "🌟🌟🌟🌟🌟"],
    index=None,
)


st.write("voce selecionou:", genre)

if st.button("Enviar"):
    if feedback:
        st.session_state.feedback_list.append({"name": name or "Anônimo", "feedback": feedback})
    else:
        st.warning("Por favor, insira seu feedback antes de enviar.")

st.write("---")
st.subheader("📋 Feedbacks Recebidos:")


if st.session_state.feedback_list:
    for fb in st.session_state.feedback_list:
        st.markdown(f"""
            <div class="feedback-box">
                <h6>{fb["name"]}</h6>
                <p>{fb["feedback"]}</p>
                <p> Avaliou com {genre} estrelas! </p>
            </div>
        """, unsafe_allow_html=True)
else:
    st.info("Nenhum feedback recebido ainda.")