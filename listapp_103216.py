import numpy as np
import pandas as pd
import streamlit as st
import base64

st.write("This Web Application is developed Using Python @ Dammyway")
remita = st.file_uploader("Kindly upload your csv or excel file here", type=["xlsx", "csv"])
if remita is not None:
    # Determine file type and read data into DataFrame
    if remita.name.endswith('.csv'):
        df = pd.read_csv(remita)
    elif remita.name.endswith('.xlsx'):
        df = pd.read_excel(remita, engine='openpyxl')
        
    df_shape = df.shape  # Store the shape of df for later use
    
    # Extract specific columns from df
    extractor = ["Unnamed: 4", "Unnamed: 5", "Unnamed: 10"]
    name_extractor = ["Staff Number", "Staff Name", "Amount"]
    p_xtractor = df[extractor]
    p_xtractor.columns = name_extractor
    
    p_xtractor.dropna(inplace = True)
    p_xtractor.drop_duplicates(inplace = True)
    p_xtractor  = p_xtractor.reset_index(drop = True)
    st.write(p_xtractor)
