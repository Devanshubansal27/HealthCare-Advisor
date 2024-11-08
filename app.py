import streamlit as st
import google.generativeai as genai
import os
import pandas as pd
from dotenv import load_dotenv
import time

# Load environment variables
load_dotenv()

# Set up the Gemini API Key
genai.configure(api_key=os.getenv('GOOGLE-API-KEY'))

# Streamlit Page Configuration
st.set_page_config(page_title="Health Buddy", page_icon="👨‍⚕️", layout="centered")

# Sidebar Navigation
st.sidebar.markdown("<h2 style='text-align: center; color: #4CAF50;'>Health Buddy</h2>", unsafe_allow_html=True)
module = st.sidebar.radio("Navigate to:", ["Health Advice", "BMI Calculator"])

# Function to Get AI Response
def get_response(text):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(text)
    return response.text

# Generative AI Response Module
if module == "Health Advice":
    st.markdown(f"""
        <div style='text-align: center;'>
            <h1 style='color: #4CAF50;'>👨‍⚕️ Health Buddy</h1>
            <h3>Your Trusted Health Advisor for Well-being and Guidance </h3>
            <p>Ask questions, check your BMI, and get personalized health insights instantly.</p>
        </div>
        <hr style="border: 1px solid #4CAF50;">
    """, unsafe_allow_html=True)

    st.write("### 🤔 What would you like to know?")
    input_text = st.text_input("Ask me anything about health:", placeholder="e.g., How to manage stress?", help="Press Enter to submit")
    
    # Handle form submission
    submit_button = st.button("Get Advice")

    # Store user input and feedback in session state
    if 'input_text' not in st.session_state:
        st.session_state.input_text = ""
        st.session_state.feedback = None

    if input_text:
        st.session_state.input_text = input_text

    # Show response and feedback option
    if submit_button or st.session_state.input_text:
        if st.session_state.input_text.strip() == "":
            st.warning("Please enter something.")
        else:
            with st.spinner('Getting advice...'):
                time.sleep(1.5)
                response = get_response(st.session_state.input_text)
            st.markdown(f'<div class="response"><h4>🧑‍⚕️ Health Buddy\'s Response:</h4><p>{response}</p></div>', unsafe_allow_html=True)
            st.caption("🔹 Powered by Gemini AI.")

            # Ask for feedback after response
            st.write("### Was this response helpful?")
            feedback_yes = st.button("👍 Yes, helpful")
            feedback_no = st.button("👎 No, try another response")

            # Handle feedback
            if feedback_yes:
                st.session_state.feedback = "positive"
                st.success("Thank you for your feedback!")
            elif feedback_no:
                st.session_state.feedback = "negative"
                st.warning("Getting a new response, please wait...")
                time.sleep(1.5)
                new_response = get_response(st.session_state.input_text)
                st.markdown(f'<div class="response"><h4>🧑‍⚕️ Here\'s an alternative response:</h4><p>{new_response}</p></div>', unsafe_allow_html=True)

    st.markdown("""
        <hr style="border: 1px solid #4CAF50;">
        <div style='text-align: center; color: #888; margin-top: 20px;'>
            <h4><strong>Disclaimer:</strong></h4>
            <p>This is an advisor providing guidance and should not be construed as medical advice. Always consult a professional healthcare provider before making any health-related decisions.</p>
        </div>
    """, unsafe_allow_html=True)

# BMI Calculator Module
elif module == "BMI Calculator":
    st.markdown("<h2 style='text-align: center; color: #4CAF50;'>BMI Calculator</h2>", unsafe_allow_html=True)
    st.write("Calculate your Body Mass Index (BMI) to understand your health status.")

    # Weight and Height Inputs
    weight = st.text_input("Enter your weight (kg):", placeholder="e.g., 70")
    height = st.text_input("Enter your height (cm):", placeholder="e.g., 175")
    calculate_bmi = st.button("Calculate BMI")

    # BMI Calculation with Error Handling
    try:
        weight = pd.to_numeric(weight)
        height = pd.to_numeric(height)
        if calculate_bmi and weight > 0 and height > 0:
            bmi = weight / (height / 100) ** 2
            bmi_category = (
                "Underweight" if bmi < 18.5 else
                "Normal weight" if 18.5 <= bmi < 24.9 else
                "Overweight" if 25 <= bmi < 29.9 else
                "Obesity"
            )
            st.success(f"**Your BMI**: {bmi:.2f} \n**Category**: {bmi_category}")
        elif calculate_bmi:
            st.error("Please enter valid numbers for weight and height.")
    except ValueError:
        if calculate_bmi:
            st.error("Please enter numeric values for weight and height.")

# Footer Section with Powered by Gemini
st.markdown(f"""
    <hr style="border: 1px solid #4CAF50;">
    <div style='text-align: center; margin-top: 20px;'>
        <p><strong style="color: #4CAF50;">Health Buddy</strong> is proudly supported by advanced AI technology to provide reliable insights and advice.</p>
        <p style='font-size: 0.9em; color: #4CAF50;'>Powered by <span style='color: #4CAF50;'>Gemini AI</span> 🌐</p>
    </div>
""", unsafe_allow_html=True)
