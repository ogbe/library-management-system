from library import Library

library = Library("books.json")
library.load_books()

while True:

    print("=== Library Management System ===")

    print(
        "1. Add Book \n"
        "2. Find Book \n"
        "3. Update Book \n"
        "4. Remove Book \n"
        "5. List Books \n"
        "6. Exit"
    )


    try:
        choice = int(input("Choose an option: "))
    except ValueError:
        print("Please enter a number")
        
        continue


    if choice == 1:
        print("Add book selected")
        title = input("Type in the title of the book you want to add: ")
        author = input("Type in the author of the book you want to add: ")

        if library.add_book(title, author):
            print(f"{title} by {author} has been added to the library.")
        
        else: pass
    elif choice == 2:
        print("Find book selected")
        book_id = int(input("Type in the ID of the book you want to find: "))
        
        if not library.find_book(book_id):
            print("The ID does not match any book in the library")

    elif choice == 3:
        print("Update book selected")
        book_id = int(input("Type in the ID of the book you wish to update: "))
        new_title = input("Type in the new title of the book: ")
        new_author = input("Type in the name of the author of the book you wish to update: ")
        library.update_book(book_id, new_title, new_author)

    elif choice == 4:
        print("Remove book selected")
        book_id = int(input("Type in the ID of the book you wish to remove: "))
        library.remove_book(book_id)

        if not library.remove_book(book_id):
            print("The ID does not match any book in the library")

    elif choice == 5:
        print("List books selected")
        library.list_books()

    elif choice == 6:
        print("Goodbye")
        break

    else:
        print(f"Invalid option. Please choose a number between 1 and 6")




    
