import streamlit as st
import pandas as pd


st.image("Bonterra_Logo.jpg")
st.title("Hello This is the Demo")
st.subheader("lets test it out")
st.text('looks good')

data_file = st.file_uploader("please upload an CSV file",type=["csv","xlsx"],accept_multiple_files=True)

if data_file is not None:
    for i in data_file:
        
        file_detail = {"FileName":i.name,"FileType":i.type,"File_ize":i.size}
        st.write(file_detail)
        df = pd.read_csv(i)
        st.dataframe(df)
