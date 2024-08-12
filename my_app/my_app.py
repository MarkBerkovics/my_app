import streamlit as st

import numpy as np


st.markdown("# Cell phone company customer service wait time calculator 🧮")


col1, col2, col3 = st.columns(3)

with col1:
    st.write('')

with col2:
    st.text('')
    st.text('')

    st.markdown("### Day of the week")
    # day = st.number_input('Insert a number from 1 to 7', min_value=1, max_value=7)
    day = st.slider('Select a day between 1 and 7', 1, 7, 1)

    st.text('')
    st.text('')

    st.markdown("### Day of the week")
    # time = st.number_input('Enter a time of day between 1 and 24', min_value=1, max_value=24)
    time = st.slider('Select a time between 1 and 24', 1, 24, 1)

    st.text('')
    st.text('')

    if st.button('calculate'):
        st.write('The wait time is:', 3 * day + 5 * time + 500, 'minutes')

with col3:
    st.write('')
