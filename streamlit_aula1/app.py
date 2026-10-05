import streamlit as st
import pandas as pd

nome = "Carlos"
idade = 17

st.write("Olá, mundo")
st.write("Meu nome é", nome, "e eu tenho", idade, "anos.")



nome = "Carlos"
idade = 17

df = pd.DataFrame({
    "Matéria": ["Português", "Matemática", "Python", "Frame"],
    "Nota": [5, 9, 7, 10]
})

st.title("Meu primeiro dash")
st.subheader(nome)

st.write("Olá, mundo")
st.write("Meu nome é", nome, "e eu tenho", idade, "anos.")

st.write(df)
