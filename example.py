"""
Main module for Python starter template.
This is a simple Hello World placeholder to get started.

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
  6. Use format string (f string) function


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
    Thank you John Smith, you checked out 3 today! Enjoy!
"""


def check_library_rules(account_is_active: bool, books_checked_out: int) -> str:
    """
    Checks to see if a member can check out more books based on the input parameters
    and returns a message indicating the result.
    """

    # create a variable to store the result of the rules
    message = ""

    # conditional statement to check the library rules
    if not account_is_active:
        message = "You must have an active account in order to check out any books."
    elif books_checked_out >= 5:
        message = "You cannot check out anymore books, 5 is the limit." 
    else:
        message = "You can check out more books."

    return message

def main():  
    print("=" * 75)

    # store the member's name (string)
    member_name = "John Smith"

    # ------------------------------------------------------------
    # STEP 1: 
    #   Use a List data type to store the books the member has checked out
    # ------------------------------------------------------------

    # create a List variable to store the books
    member_books = [
        "The Hobbit",
        "The Lord of the Rings",
        "The Hunger Games"
    ]
 
    # ------------------------------------------------------------
    # STEP 2: 
    #   Use a for loop to print out each of the books from the variable in step 1
    # ------------------------------------------------------------

    # create a for loop and print out each book
    print("iterate books using for loop")
    for book in member_books:
        print(book)

    # ------------------------------------------------------------
    # STEP 3: 
    #   Update the books_checked_out variable to use len() function 
    #   to set the variable value to match the len of the variable in step 1
    #   and then write a for loop that uses a range to print out each book
    # ------------------------------------------------------------

    # store the books that are checked out (number)
    books_checked_out = len(member_books)

    print("iterate books using for..range")
    for i in range(books_checked_out):
        print(member_books[i])

    # store whether the library account is active (boolean)
    account_is_active = True

    # print("Member Name:", member_name)
    # print("Books Checked Out:", books_checked_out)
    # print("Account Active:", account_is_active)

    # ------------------------------------------------------------
    # STEP 4: 
    #   Create a Function that checks the library rules. It should have
    #   two parameters:
    #     1. account_is_active (bool)
    #     2. books_checked_out (int)
    #   It should return a variable called message that is a string
    # ------------------------------------------------------------

    # message = check_library_rules(account_is_active, books_checked_out)
    # print(message)
 
    # ------------------------------------------------------------
    # STEP 5: 
    #   Use a WHILE loop to with the input function to ask the user
    #   if they are ready to check out and print the message
    # ------------------------------------------------------------

    ready_to_checkout = False
    while not ready_to_checkout:
        # check the library rules
        message = check_library_rules(account_is_active, books_checked_out)
        print(message)

        # ask the user if they are ready to checkout
        user_ready = input("Are you ready to checkout your books? Enter a y if so: ")

        # check the user input
        if user_ready == "y":
            ready_to_checkout = True

    # ------------------------------------------------------------
    # STEP 6: 
    #   Use f string to print out the member name and the number of books checked out
    # ------------------------------------------------------------ 
    print(f"Thank you {member_name}, you checked out {books_checked_out} books today! Enjoy!")

    print("=" * 75)
 

if __name__ == "__main__":
    main()
