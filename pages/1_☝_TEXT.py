from dotenv import load_dotenv
load_dotenv()


import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model=genai.GenerativeModel("gemini-pro")
def get_geminires(question):
    response=model.generate_content(question)
    return response.text

st.set_page_config(page_title="AnyQuestions?",page_icon="👍",)
st.header("New Gpt")
input= st.text_input("Input: ",key="input")

submit=st.button("Ask question")

if submit:
    response=get_geminires(input)
    st.subheader("The Response is")
    st.write(response)
    