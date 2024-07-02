def library_update_system(library, title, author):
    for book in library:
        if (title, author) == (book[0], book[1]):
            print(f"The book '{title}' by {author} is already present in this library.")
            return
        
    library.append((title, author))
    print(f"The Book '{title}' by {author} has been successfully added to the library.")

library = [("1984", "George Orwell"), ("Brave New World", "Aldus Huxley")]

library_update_system(library, "1984", "George Orwell")
library_update_system(library, "20,000 Leagues Under The Sea", "Jules Verne")
library_update_system(library, "A Time to Kill", "John Grisham" )

print("Current Library:")
for i, book in enumerate(library):
    print(f"{i + 1}. {book[0]} by {book[1]}")