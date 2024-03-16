import streamlit as st
from re import search, IGNORECASE
from lib import get_library

def search_books(library, query):
    results = []
    for book in library.display_books():
        # Create a string containing all relevant fields
        book_info = f"{book.title} {book.author} {book.genre} {book.summary}"
        # Use regex to search for the query within the book info
        if search(query, book_info, IGNORECASE):
            results.append(book)
    return results

def main():
    st.title('Book Search')
    library = get_library()

    # Add a search bar
    search_query = st.text_input("Search for books by title, author, genre, or summary")

    if search_query:
        # Perform search and display results
        results = search_books(library, search_query)
        if results:
            st.subheader('Search Results:')
            for book in results:
                st.write(f"Title: {book.title}")
                st.write(f"Author: {book.author}")
                st.write(f"Genre: {book.genre}")
                st.write(f"Summary: {book.summary}")
                st.markdown("---")
        else:
            st.write("No matching books found.")

if __name__ == "__main__":
    main()
