import streamlit as st
from app import Library

def initialize_library():
    # Initialize the library
    return Library()

def get_library():
    # Retrieve the library object
    if 'library' not in st.session_state:
        st.session_state.library = initialize_library()
        print('init')
    return st.session_state.library
