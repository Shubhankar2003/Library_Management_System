import streamlit as st
from app import Book
from app import Library

def main():
    st.set_page_config(page_title="Add Book", page_icon="➕")

    library = Library()
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
        st.success('Book added successfully!')

    book1 = Book("https://images.unsplash.com/photo-1529778873920-4da4926a72c2?q=80&w=1936&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", "Title 1", "Author 1", "Genre 1", "C:/Users/shubh/Desktop/Library Management System/2. Lecture_Telecommunication Network Model and Types.pdf", "Summary1")
    book2 = Book("https://images.unsplash.com/photo-1529778873920-4da4926a72c2?q=80&w=1936&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", "Title 2", "Author 2", "Genre 2", None, "Summary2")
    library.add_book(book1)
    library.add_book(book2)

if __name__ == "__main__":
    main()