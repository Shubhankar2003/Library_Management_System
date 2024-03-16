import streamlit as st
from lib import get_library
import base64

def displayPDF(file):
    # Opening file from file path
    with open(file, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')

    # Embedding PDF in HTML  
    pdf_display = f'<embed src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf" target="_blank">'
    
    # Displaying File
    st.markdown(pdf_display, unsafe_allow_html=True)

def view():
    st.title('Library Management System')

    library = get_library()

    # Display the list of books
    list_books(library)

def list_books(library):
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
    view()
