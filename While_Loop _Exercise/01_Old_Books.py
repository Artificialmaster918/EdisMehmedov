NO_MORE_BOOKS_COMMAND = "No More Books"

book_name = 0
target_book = input()

while True:
    current_command = input()  # current_book OR "No More Books"
    if current_command == NO_MORE_BOOKS_COMMAND:
        print("The book you search is not here!")
        print(f"You checked {book_name} books.")
        break

    book_name += 1

    current_book = current_command
    if current_book == target_book:
        book_name -= 1
        print(f"You checked {book_name} books and found it.")
        break