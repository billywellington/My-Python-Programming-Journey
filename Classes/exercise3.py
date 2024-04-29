# Exercise 3: Modeling a Library with Books
# Question:
# Define a Python class named Book to represent a book in a library. The Book class should have:
#
# Attributes for title, author, and pages.
# A method named display_info() that prints out the title, author, and number of pages of the book.
# Create instances of the Book class for three different books
# and display their information using the display_info() method.

class Books:

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def display_info(self):
        # print(f"The title of this book is: {self.title}")
        # print(f"The author of this book is: {self.author}")
        # print(f"The title of the book is: {self.pages}")

        print(f"This book called \"{self.title}\" was authored by {self.author} and it has {self.pages} pages")

book1 = Books("The Alchemist", "Paulo Coelho", 208)
book2 = Books("To Kill a Mockingbird", "Harper Lee", 281)
book3 = Books("1984", "George Orwell",276)

book3.display_info()
book2.display_info()
book1.display_info()