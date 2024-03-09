import pandas as pd

class Book:
    def __init__ (self, image, title, author, genre, pdf, summary):
        self.image = image
        self.title = title
        self.author = author
        self.genre = genre
        self.pdf = pdf
        self.summary = summary
        
    def set_sno(self, sno):
        self.__sno = sno

    def get_sno(self):
        return self.__sno
    
class Library:
    
    def __init__(self):
        self.books = []
    
    def add_book(self, book):
        sno = len(self.books) + 1
        book.set_sno(sno)
        self.books.append(book)

    def display_books(self):
        return self.books
    

