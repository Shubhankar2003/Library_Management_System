import streamlit as st
from app import Book
from app import Library

def main():

    # Continue with other Streamlit commands
    if 'library' not in st.session_state:
        st.session_state.library = Library()

    library = st.session_state.library

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
        st.success('Book added successfully! \n')
        f = open("books.txt", "a")
        f.write(f'''
                Title: {new_book.title}
                Author: {new_book.author}
                Genre: {new_book.genre}
                Summary: {new_book.summary}
                ''')
        f.close()

    book1 = Book("images/The_Art_of_War_(Giles,_1910).pdf.jpg", "Title 1", "Author 1", "Genre 1", "books/The_Art_Of_War.pdf", "Summary1")
    book2 = Book("https://images.unsplash.com/photo-1529778873920-4da4926a72c2?q=80&w=1936&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", "Title 2", "Author 2", "Genre 2", None, "Summary2")
    library.add_book(book1)
    library.add_book(book2)

    return library

if __name__ == "__main__":
    st.set_page_config(page_title="Add Book", page_icon="➕")
    main()
