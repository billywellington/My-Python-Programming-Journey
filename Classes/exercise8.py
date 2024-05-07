# Exercise 8: Modeling a Library with Books and Members
# Question:
# Define a Python class named Book to represent a book in a library, similar to Exercise 3.
# Additionally, define a class named Member to represent a member of the library.
# The Member class should have attributes for name and id.
# Implement methods in both classes to perform actions like checking out a book, returning a book,
# and displaying information about the book or member.


class Books_List:
    books = []
    
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        # self.books = []
    def display_info(self):
        # print(f"The title of this book is: {self.title}")
        # print(f"The author of this book is: {self.author}")
        # print(f"The title of the book is: {self.pages}")

        print(f"This book called \"{self.title}\" was authored by {self.author} and it has {self.pages} pages\n")
class Member:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def display_member_info(self):
        print(f"About this member.\nName: {self.name}\nID Number: {self.id}\n")

    def check_out(self, book):
        self.book = book
        #after a member checks out a book, we need to remove it from the books list
        print(f"{self.name} has checked out the following book: {self.book} ")

        Books_List.books.remove(self.book)
        print("Here's the updated Libray book list:")
        i = 0
        while i < len(Books_List.books):
            print(Books_List.books[i])
            i +=1

    def return_book(self, book):
        self.book = book
        #after a member checks in  a book, we need to add it back to  books list

        print(f"{self.name} has returned the following book: {self.book}\n")

        Books_List.books.append(self.book)
        print("Here's the updated Libray book list:")
        i = 0
        while i < len(Books_List.books):
            print(Books_List.books[i])
            i +=1

book1 = Book("The Alchemist", "Paulo Coelho", 208)
book2 = Book("To Kill a Mockingbird", "Harper Lee", 281)
book3 = Book("1984", "George Orwell",276)

member1 = Member("Billy", 2345)
member2 = Member("Kay", 3478)
member3 = Member("Jay", 2537)

book3.display_info()
book2.display_info()
book1.display_info()

member3.display_member_info()
member1.display_member_info()
member2.display_member_info()



member1.return_book("The Alchemist")
member3.return_book("To Kill a Mockingbird")
member2.return_book("1984")

print(Books_List.books)

member1.check_out("The Alchemist")
# member2.check_out("1984")

print(Books_List.books)
