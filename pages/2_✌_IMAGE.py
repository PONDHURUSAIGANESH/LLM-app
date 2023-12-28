from dotenv import load_dotenv
load_dotenv()

from PIL import Image
import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model=genai.GenerativeModel("gemini-pro-vision")
def get_geminires(input,image):
    if(input!=""):
        response=model.generate_content([input,image])
    else:
        response=model.generate_content(image)
    return response.text

st.set_page_config(page_title="Image demo",page_icon="🗄",)
st.header("New Gpt")
input= st.text_input("Input: ",key="input")

upload=st.file_uploader("Choose an image ..",type=["jpg","png","jpeg"])

image=""
if upload is not None:
    image=Image.open(upload)
    st.image(image, caption="Uploaded",use_column_width=True)

submit=st.button("Tell about the image")
if submit:
    res=get_geminires(input,image)
    st.subheader("The Response that you asked: ")
    st.write(res)
    