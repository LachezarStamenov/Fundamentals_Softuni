shelf_with_books = input().split("&")

command = input()

while not command == "Done":

    current_command = command.split(" | ")
    action = current_command[0]

    if action == "Add Book":
        book = current_command[1]
        if book not in shelf_with_books:
            shelf_with_books.insert(0, book)
    elif action == "Take Book":
        book = current_command[1]
        if book in shelf_with_books:
            shelf_with_books.remove(book)
    elif action == "Swap Books":
        book_one = current_command[1]
        book_two = current_command[2]
        if book_one in shelf_with_books and book_two in shelf_with_books:
            idx1 = shelf_with_books.index(book_one)
            idx2 = shelf_with_books.index(book_two)
            shelf_with_books[idx1], shelf_with_books[idx2] = shelf_with_books[idx2], shelf_with_books[idx1]
    elif action == "Insert Book":
        book = current_command[1]
        if book not in shelf_with_books:
            shelf_with_books.append(book)
    elif action == "Check Book":
        book = current_command[1]
        idx = int(current_command[1])
        if 0 <= idx < len(shelf_with_books):
            print(shelf_with_books[idx])
    command = input()

print(*shelf_with_books, sep=", ")
