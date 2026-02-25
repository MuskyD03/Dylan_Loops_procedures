"""
Assignment:
  Loops, Events, and Procedures

Instructions:
  Review the details below and complete the 5 steps. Be sure to commit and sync your
  code often so that you do not lose your work. Be sure to test your code using
  python main.py

Items to discuss in this lesson:

  - Previous Assignment:
    - Variables
      - Identifier
      - Value
      - Assignment Operator
    - Conditional Statements
      - if..then
    - Data Types (a few of them)
      - String
      - Number
      - Boolean
      - List (Array)

  - This Assignment:
    - Built-In Functions (e.g. print, len, input) - think of Tools - f string
    - Loops: allow you to easily repeat a chunk of code many times
    - Functions (Procedures): a piece of code you can easily use over and over
        - parameters
        - return value

Steps
  1. Create a list variable to store the books the member has checked out
  2. Use a for loop to print out each of the books from the variable in step 1
  3. Use for loops to iterate the list created in step 1
  4. Create a function to check the library rules
  5. Use a WHILE loop to keep checking until the user is ready to checkout


Expected Output:
    iterate books using for loop
    The Hobbit
    The Lord of the Rings
    The Hunger Games
    iterate books using for..range
    The Hobbit
    The Lord of the Rings
    The Hunger Games
    You can check out more books.
    Are you ready to checkout your books? Enter a y if so: y
    You are checked out, have a great day
"""

# add check library rules function here
# def your_function():


def main():
    print("=" * 75)

    # variables used in prior assignment
    member_name = "Dylan"
    books_checked_out = 3
    account_is_active = True

    # ------------------------------------------------------------
    # STEP 1:
    #   Use a List data type to store the books the member has checked out
    # ------------------------------------------------------------

    # create a List variable to store the books
    # HINT: []
    books = ["'Dog Man', 'Captain Underpants', The Holy Bible"]

    # ------------------------------------------------------------
    # STEP 2:
    #   Use a for loop to print out each of the books from the variable in step 1
    for book in books:
        print(books)
    # ------------------------------------------------------------

    # create a for loop and print out each book

    # for item in list
    for i in range (1000):
        print("index:", i + 1)
        print("move up")
        print("fall down")
    # ------------------------------------------------------------
    # STEP 3:
    #   Update the books_checked_out variable to use len() function
    #   to set the variable value to match the len of the variable in step 1
    #   and then write a for loop that uses a range to print out each book
    # ------------------------------------------------------------

    # store the books that are checked out (number)
    books_checked_out = len(books)
    for i in range(books_checked_out):
        print(books[i])

    # iterate the books using range
    # for i in range

    # after adding the loops, comment out or remove these print statements
  
    print("Member Name:", member_name)
    print("Books Checked Out:", books_checked_out)
    print("Account Active:", account_is_active)

    def main():
        books = ["'Dog Man', 'Captain Underpants', The Holy Bible"]
        for book in books:
            print(book)

        books_checked_out = len(books)

        for i in range(books_checked_out):
            print(books[i])

    # ------------------------------------------------------------
    # STEP 4:
    #   Create a Function that checks the library rules. It should have
    #   two parameters:
    #     1. account_is_active (bool)
    #     2. books_checked_out (int)
    #   It should return a variable called message that is a string
    # ------------------------------------------------------------

    # call your function here
    # conditional statement to check the library rules - remove this code
    # after you have added a function to replace it

    def check_library_rules(account_is_active, books_checked_out):
        if not account_is_active:
            message = "you must have an active account in order to check out any books"
        elif books_checked_out >= 5:
            message = "you cannot check out anymore books, 5 is the limit"
        else:
            message = "you can check out more books."
        return message

    # ------------------------------------------------------------
    # STEP 5:
    #   Use a WHILE loop to with the input function to ask the user
    #   if they are ready to check out and print the message
    #   HINT: us the input() function to ask the user and then
    #   check if they entered a value such as y
    # ------------------------------------------------------------

    # add WHILE LOOP here

    account_is_active = True
    books_checked_out = 3

    ready_to_checkout = ""
    while ready_to_checkout.lower() != "yes":
        ready_to_checkout = input("Are you ready to check out? Type 'yes' when ready: ")
        if ready_to_checkout.lower() == "yes":
          final_message =  check_library_rules(account_is_active, books_checked_out)
          print(final_message)
    else:
          print("please indicate you are ready to check out to proceed.")
    print("=" * 75)


if __name__ == "__main__":
    main()

