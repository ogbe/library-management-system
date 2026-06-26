import json

class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
    
    def describe(self):
        return f"This book is titled {self.title}, and was written by {self.author}"
        
    def to_dict(self):
        return {
            "book_id": self.book_id,
            "title": self.title,
            "author": self.author
        }
        
    def __str__(self):
        return self.describe()
        
    
            
class Library:
    def __init__(self, filename):
        self.books = []
        self.filename = filename

        
    def add_book(self, title, author):

        for book in self.books:
            if (
                book.title.lower().strip() == title.lower().strip() 
                and 
                book.author.lower().strip()== author.lower().strip()
            ):
                print("This book already exists")
                return False
            
        if not self.books:
            book_id = 1


        else:
            next_id = max(book.book_id for book in self.books)
            book_id = next_id + 1



        book = Book(book_id, title, author)
        self.books.append(book)
        self.save_books()
        return True
        
        
    def list_books(self):
        if len(self.books) == 0:
            print("Library is empty. Begin by adding a book")
            return
        for book in self.books:
            print(book)
            
    def find_book(self, book_id):
        
        for book in self.books:
            
            if book.book_id == book_id:
                #print(book)
                return book
    
    
        return None
        
    def remove_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                self.books.remove(book)
                print("Book removed") 

                self.save_books()

                return True
        
                
        print("Book not found")
        return False
        
    def update_book(self, book_id, new_title, new_author):
        for book in self.books:
            if book.book_id == book_id:
                book.title = new_title
                book.author = new_author

                self.save_books()
                return book
            
        print("Book not found")
        return False
        

    def save_books(self):

        try:
            data = [book.to_dict() for book in self.books]

            with open(self.filename, "w") as file:
                json.dump(data, file)


        except Exception as e:
            print(e)
            
    def load_books(self):
        try:
            with open(self.filename, "r") as file:
                data = json.load(file)
                self.books = [Book(**item) for item in data]

        except FileNotFoundError:
            print("No saved library found, starting with an empty library")
            self.books = []

        except (UnicodeDecodeError, json.JSONDecodeError):
            print("Could not load library data.")
            self.books = []

    def clear_saved_file(self):
        self.books.clear()
        with open(self.filename, "w") as file:
            json.dump(self.books, file)
        print("Library cleared")

            
    # def clear_books(self, filename):
    #    self.books.clear()
    #    print("Library cleared")
        
        
#book1 = Book(1, "Half of a yellow sun", "Chimamanda Adichie")
#book2 = Book(2, "Things fall apart", "Chinua Achebe")
#book3 = Book(3, "It's a long road to freedom", "Longinus Paul")
#book4 = Book(4, "October 1", "Muhammadu Buhari")

#book2.describe()
#library = Library("books.json")
#library.add_book("Half of a yellow sun", "Chimamanda Adichie")
#library.add_book("Things fall apart", "Chinua Achebe")
#library.add_book("It's a long road to freedom", "Longinus Paul")

#library.add_book(book4)
#library.list_books()

#print(library.book_id)





#library.list_books()

#library.find_book(5)

#library.remove_book(1)

#library.update_book(2, "it's a long road to sorrow", "Longinus Peter")

#library.save_books()
#library.clear_saved_file()

#new_library = Library("science.json")

#new_library.add_book(book1)
#new_library.add_book(book2)
#new_library.add_book(book3)
#new_library.add_book(book4)

#library.load_books()

#or book in new_library.books:
#    print(book)

#new_library.clear_saved_file("books.json")

#new_library.load_books("books.json")



