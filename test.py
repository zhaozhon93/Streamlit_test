import streamlit as st
import pandas as pd
import os



st.title("Hello This is the Demo")
st.subheader("lets test it out")
st.text('looks good')
a = st.image("Bonterra_Logo.jpg")
data_file = st.file_uploader("please upload an CSV file",type=["csv","xlsx"],accept_multiple_files=True)

try:
   
    
    if data_file is not None:

        for i in data_file:

             ext = os.path.splitext(i.name)[-1].lower()

             if ext == '.csv':
                 df = pd.read_csv(i)
             elif ext == '.xlsx':
                df = pd.read_excel(i)
             else:
                 st.error("File is not a CSV or EXCEL file")

        
             file_detail = {"FileName":i.name,"FileType":i.type,"File_ize":i.size}
             st.write(file_detail)
            
            
             st.download_button(
                label="Download data as CSV",
                data=i,
                file_name='large_df.csv')
                
             if i.name == 'us_quarters.csv':
                df = df.filter(items =['State'])
                df['External_User_ID'] = df['State']

             if "constituents" in i.name.lower():
                 df = df.filter(items=['LGL Constituent ID', 'Constituent Name','Constituent Type','Contact Type','Spouse Name','Communication Tags','Background Info'])
                 df['External_user_id'] = df['LGL Constituent ID']

             st.dataframe(df)


except AttributeError:
    st.write("Please Upload A Dataset to Continue")
