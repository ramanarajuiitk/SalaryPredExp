
import streamlit as st

import pandas as pd

import numpy as np

import pickle

import base64





st.write("""

# Salary Prediction

This Machine learning app is for predicting salary

""")


Exp	= st.number_input('Experience:')



model = pickle.load(open(r'model.pkl','rb'))




if st.button('Salary is '):
    Temp1 = model.predict([[Exp]] )
    st.success(f'Salary is {Temp1[0]:.1f} ')			
