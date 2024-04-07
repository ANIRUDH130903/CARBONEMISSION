import streamlit as st 
import joblib 

#load the joblib model
model_nb = joblib.load('Carbon-Emission')

st.title('Carbon-Emission predictor')
ip = st.text_input('ENTER YOUR YEAR:')

op= model_nb.predict([ip])
if st.button('PREDICT'):
  st.button(op[0])
  
