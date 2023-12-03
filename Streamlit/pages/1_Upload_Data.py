import streamlit as st 
import pandas as pd

st.title('Upload Iris Data')

if 'data' in st.session_state:
    st.info('Data is already uploaded!')  # This is the process that happens after you uploaded file
    st.write(st.session_state['data'].head())

else:
    uploaded_file = st.file_uploader("", type=['csv', 'xlsx'])
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        actual = list(df.columns)
        expected = ['Id',
            'SepalLengthCm',
            'SepalWidthCm',
            'PetalLengthCm',
            'PetalWidthCm',
            'Species']
        if actual == expected:
            st.write(df.head())
            st.session_state['data'] = df
            st.success('Data uploaded successfully!')
        else:
            st.error('Please upload the correct file!')
