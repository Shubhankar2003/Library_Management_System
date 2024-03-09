import streamlit as st
from app import Book
from app import Library

def main():
    library = Library()

    st.title('Library Management System')
    
    st.subheader("Add a new book")
    title = st.text_input('Title')
    image_url = st.text_input('Image URL')
    author = st.text_input('Author')
    genre = st.text_input('genre')
    summary = st.text_input('summary')
    if st.button('Add'):
        new_book = Book(image_url, title, author, genre, "pdf.pdf", summary)
        library.add_book(new_book)
        st.success('Book added successfully!')
    
    book1 = Book("https://placekitten.com/500/500", "Title 1", "Author 1", "Genre 1", "pdf1.pdf", "Summary1")
    book2 = Book("https://placekitten.com/500/500", "Title 2", "Author 2", "Genre 2", "pdf2.pdf", "Summary2")
    book3 = Book("https://placekitten.com/500/500", "Title 3", "Author 3", "Genre 3", "pdf3.pdf", "Summary3")
    book4 = Book("https://placekitten.com/500/500", "Title 4", "Author 4", "Genre 4", "pdf4.pdf", "Summary4")
    book5 = Book("https://placekitten.com/500/500", "Title 5", "Author 5", "Genre 5", "pdf5.pdf", "Summary5")
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)
    library.add_book(book4)
    library.add_book(book5)

    
    st.subheader('Books in the Library:')
    
    # Display book data in a table
    for book in library.display_books():
        st.image(book.image, width=200)
        st.markdown(f"## **Title:** {book.title}")
        st.write(f"### **Author:** {book.author}")
        st.write(f"**Genre:** {book.genre}")
        st.write(f"**Summary:** {book.summary}")
        st.markdown("<hr>", unsafe_allow_html=True)
        st.write('\n')

if __name__ == "__main__":
    main()