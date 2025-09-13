import datetime

class Book:
    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year

    def calculate_book_age(self):
        current_year = datetime.datetime.now().year
        print(current_year)
        return current_year-self.publication_year
    


book1 = Book("Lone Wolf", "Jodi", 1975)
print(book1.calculate_book_age())

book2 = Book("Sapiens", "Noah", 2024)
print(book2.calculate_book_age())