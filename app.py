import streamlit as st
##import langchain 
import google.generativeai as genai
import os
import pandas as pd
from dotenv import load_dotenv
load_dotenv()


# Set up the Gemini API Key 
genai.configure(api_key=os.getenv('GOOGLE-API-KEY'))

# Streamlit Page

st.header("👨‍⚕️Health :blue[Buddy]",divider="green")
input = st.text_input("Hi, I am your 💊medical Expert. Ask me anything")
submit=st.button("Submit")


st.sidebar.subheader("BMI Calculator✍️")
weight=st.sidebar.text_input("Weight(in Kgs):")
height=st.sidebar.text_input("Height (in cms)")
calculate=st.sidebar.button("Calculate")
weight=pd.to_numeric(weight)
height=pd.to_numeric(height)
bmi=weight/(height/100)**2


notes=f""" The BMI Value can be interpreted as:
* Under Weight: BMI<18.5
* Normal Weight: BMI 18.5-24.9
* Over Weight : BMI 25 - 29.9
* Obesity : BMI>30
"""

if calculate:
    st.sidebar.markdown("The BMI is")
    st.sidebar.write(bmi)
    st.sidebar.write(notes)

# Generative ai Application
def get_response(text):
    model=genai.GenerativeModel("gemini-pro")
    if text!="":
        response=model.generate_content(text)
        return (response.text)
    else:
        st.write("Please Enter the Prompt!")

if submit:
    response = get_response(input)
    st.subheader("The :orange[Response] is: ")
    st.write(response)

# Disclaimer
st.subheader("Disclaimer:",divider=True)
notes=f'''
1. This is an advisor providing guidance and should not be construced as Medice
2. Before taking any action, It would be recommended to consult a DOctor.'''

st.markdown(notes)
