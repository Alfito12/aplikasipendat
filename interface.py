import streamlit as st
import re
import pandas as pd 
import numpy as np

st.title("""
form input data
""")

#Fractional Knapsack Problem
#Getting input from user
Umur = int(st.number_input("Masukan Umur: ",0))
Jenis_Kelamin = int(st.number_input("Durasi : ",0))
Total_Bilirubin = int(st.number_input("Total : ",0))
Direct_Bilirubin = int(st.number_input("DIrect : ",0))
Alkaline_Phosphotase = int(st.number_input("alkaline : ",0))
Alamine_Aminotransferase = int(st.number_input("alamine : ",0))


submit = st.button("submit")


if submit:
    st.info("Jadi,dinyakataan . ")


