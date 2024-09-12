import streamlit as st
import pathlib
import textwrap
from PIL import Image
import os
os.environ['GEMINI_API_KEY']='AIzaSyDKUvvRLei5Rj_OhbmC0_QcYXzd5XZEbOI'

import google.generativeai as genai
genai.configure(api_key=os.environ['GEMINI_API_KEY'])

# function
def get_gemini_response(input,image):
    #model=genai.GenerativeModel('gemini-pro-vision')
    model=genai.GenerativeModel('gemini-1.5-flash')

    if input != "":
        response=model.generate_content([input,image])
    else:
        response=model.generate_content(image)
    return response.text

# streamlit 

st.set_page_config(page_title='Image Creation')

st.header('GEMINI AI IMAGE APP ANALYSIS')

input=st.text_input('Input Prompt :',key='input')
upload_file=st.file_uploader('Choose an image',type=['jpg','jpeg','png'])

image=""
if upload_file is not None:
    image=Image.open(upload_file)
    st.image(image, caption='Upload Image',use_column_width=True)
submit=st.button('Explain brief about image')

if submit:
    response=get_gemini_response(input,image)
    st.subheader('The response is ')
    st.write(response)
    