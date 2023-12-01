import streamlit as st 
import seaborn as sns
import matplotlib.pyplot as plt

st.title('Exploratry Data Analysis')

if 'data' in st.session_state:
    df = st.session_state['data']
    option = st.selectbox(
        'Select your favorite visualization:',
        ('--', 'Scatter Plot', 'Histogram', 'Heatmap'))
    if option == 'Scatter Plot':
        fig, ax = plt.subplots()
        sns.scatterplot(x=df['SepalLengthCm'], y=df['PetalLengthCm'], hue=df["Species"])
        st.pyplot(fig)

    elif option == 'Histogram':
        fig, ax = plt.subplots()
        sns.histplot(x=df['SepalLengthCm'])
        st.pyplot(fig)

    else:
        fig, ax = plt.subplots()
        sns.heatmap(df.drop('Id', axis=1).corr())
        st.pyplot(fig)
