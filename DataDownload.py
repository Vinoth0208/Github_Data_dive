import streamlit as st
import pandas as pd
def datadownload(topic):
    data=pd.read_csv(f'{topic}.csv')

    File = data.to_csv()
    st.download_button(
        label="Download data as CSV",
        data=File,
        file_name=f'{topic} Github Data Dive .csv',
        mime='text/csv', )
