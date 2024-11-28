from dotenv import load_dotenv
load_dotenv() ## loading all the environment variables
import streamlit as st
import os
import google.generativeai as genai
key = "AIzaSyAZ6uVvPoLek51VPD2DSdf3Wh6alcbPhTA"
genai.configure(api_key=key)

## function to load Gemini Pro model and get repsonses
model=genai.GenerativeModel("gemini-pro") 
chat = model.start_chat(history=[])
def get_gemini_response(question):
    
    response=chat.send_message(question,stream=True)
    return response

question = input("Ask your question : ")
response = get_gemini_response(question=question)
for chunk in response:
    print(chunk.text)

