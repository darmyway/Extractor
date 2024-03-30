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

# Read the Excel file into a Pandas DataFrame
new = pd.read_excel('Book6.xlsx')

new.head()

new["Staff_Number"] = df["Unnamed: 4"]
new["Name"] = df["Unnamed: 5"]
new["Amount"] = df["Unnamed: 10"]
new.dropna(inplace = True)
new.drop_duplicates(inplace = True)
extracted_payment = new.reset_index(drop = True)

st.write(extracted_payment)
extracted_payment.shape

