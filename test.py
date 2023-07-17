import streamlit as st



st.title("Hello This is the Demo")
st.subheader("lets test it out")
st.text('looks good')
st.image("1.jpg")
Table = st.file_uploader("please upload an CSV file",type=["csv","xlsx"],accept_multiple_files=True)
if Table is not None:
    for i in Table:
        st.table(i)