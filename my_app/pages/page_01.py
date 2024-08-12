import streamlit as st

my_secret = st.secrets['MY_SECRET']
st.write('This is page 1')
st.write('And this is my secret:')
st.write(my_secret)
