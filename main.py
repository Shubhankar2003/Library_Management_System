import streamlit as st
from app import Book
from app import Library
import base64

def displayPDF(file):
    # Opening file from file path
    with open(file, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')

    # Embedding PDF in HTML  
    pdf_display = f'<embed src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf" target="_blank">'
    
    # Displaying File
    st.markdown(pdf_display, unsafe_allow_html=True)


def main():
    library = Library()

    st.title('Library Management System')
    
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
    
    st.subheader('Books in the Library:')
    
    # Display book data in a table
    for index, book in enumerate(library.display_books()):
        st.image(book.image, width=200)
        st.markdown(f"## **Title:** {book.title}")
        st.write(f"### **Author:** {book.author}")
        st.write(f"**Genre:** {book.genre}")
        st.write(f"**Summary:** {book.summary}")
        if st.button('Read PDF', key=f'PDF - {index}'):
            if book.pdf:
                displayPDF(book.pdf)
            else:
                st.warning("No PDF available for this book.")
        st.markdown("<hr>", unsafe_allow_html=True)
        st.write('\n')

if __name__ == "__main__":
    main()