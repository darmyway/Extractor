import numpy as np
import pandas as pd
import streamlit as st

remita = st.file_uploader("Kindly uploaded your csv or excel file here", type = ["csv", "xlsx"])

if remita is not None:
    # Determine file type and read data into DataFrame
    if remita.name.endswith('.csv'):
        df = pd.read_csv(remita)
    elif remita.name.endswith('.xlsx'):
        df = pd.read_excel(remita, engine='openpyxl')
    st.write(df)
    df.shape

extractor= ["Unnamed: 4", "Unnamed: 5", "Unnamed: 10"]
name_extractor = ["Staff Number", "Staff Name", "Amount"]

p_extract = remita[extractor]
p_extract.columns = name_extractor

p_extract.dropna(inplace = True)
p_extract.drop_duplicates(inplace = True)
p_extract = p_extract.reset_index(drop = True)

p_extract.shape
p_extract.head()
