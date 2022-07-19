import streamlit as st
import joblib
model = joblib.load('iris')
st.title('iris')
st.title('SPECIES CLASSIFIER')
ip = st.text_input('Enter the sepal_length,sepal_width,petal_length,petal_widthin this formatx,x,x,x')
op = model.predict([ip])
if st.button('Predict'):
  st.title(op[0])
                  
