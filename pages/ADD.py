import streamlit as st
from lib import get_library
from app import Book

def main():

    library = get_library()
    st.subheader("Add a new book")
    title = st.text_input('Title')
    author = st.text_input('Author')
    genre = st.text_input('Genre')
    summary = st.text_input('Summary')
    image = st.file_uploader('Upload Image',  type=['jpg', 'jpeg', 'png', 'heic', 'webp'])
    pdf = st.file_uploader('Upload PDF', type='pdf')
    
    if st.button('Add'):
        new_book = Book(image, title, author, genre, pdf, summary)
        library.add_book(new_book)
        st.success('Book added successfully! \n')
    return library

if __name__ == "__main__":
    st.set_page_config(page_title="Add Book", page_icon="➕")
    main()
