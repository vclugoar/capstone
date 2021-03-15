import streamlit as st 
import itertools 
import pandas as pd 
import numpy as np 
import altair as alt
import matplotlib.pyplot as plt
import time
import seaborn as sns 
from streamlit_embedcode import pastebin_snippet


def app():

    # brief about 
    with st.beta_container():
        st.image('https://i.ibb.co/RH2SWMk/Hello-This-tool-started-as-a-capstone-project-for-the-MS-in-Data-Analysis-and-Visualization-program.png', use_column_width=True)
    
    # form 
    with st.beta_container():
        st.markdown('<h2> Would you like to add a book or author?</h2>', unsafe_allow_html=True)
        st.markdown('<h4>Book Name(s)</h4>', unsafe_allow_html=True)
        newBookName = st.text_area("Please enter the book name(s), separated by commas")
        st.markdown('<h4>Author Name(s)</h4>', unsafe_allow_html=True)
        newBookAuthor = st.text_area("Enter the author name(s), separated by commas")

        st.markdown('<h2> Any questions, feedback or recommendations? </h2>', unsafe_allow_html=True)
        newFeedback = st.text_area("Enter questions, feedback or recommendations")

        st.markdown('<h2> Would you like to receive email updates about this or similar projects?</h2>', unsafe_allow_html=True)
        st.markdown('<h4> If so, enter your contact information below</h4>', unsafe_allow_html=True)
        emailName = st.text_input('Enter name')
        emailAddress = st.text_input('Enter a valid email address')

        # submit button 
        clickSubmit = st.button('Submit')

        if clickSubmit == True:
            st.markdown('<h3>Thank you for your feedback!</h3>', unsafe_allow_html=True)
            # save into dictionary and then dataframe 
            d = {'Book Name(s)': [newBookName], 
                'Book Author(s)': [newBookAuthor],
                'Feedback': [newFeedback],
                'Name': [emailName],
                'Email': [emailAddress]}
            df = pd.DataFrame(data=d)
            st.markdown('Submitted responses:')
            st.write(df)
        
        else:
            st.markdown("Click submit to save form responses.")

#app()

