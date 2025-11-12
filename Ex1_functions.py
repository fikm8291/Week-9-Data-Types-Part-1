# -------------------------------------------
# Exercise 1: Functions
# -------------------------------------------
# In this exercise, you'll work in groups of 2–3.
# You'll learn about FUNCTIONS - reusable blocks of code.
#
# Basic function example:
# def greet():
#     print("Hello!")
#
# Function with parameters:
# def greet(name):
#     print(f"Hello, {name}!")
#
# Function that returns a value:
# def add(a, b):
#     return a + b
#
# Each learner will build on the previous one's work.
# -------------------------------------------
# GROUP INSTRUCTIONS
# -------------------------------------------
# Work in groups of 2–3. Share the same GitHub repository.
# Roles:
# - One learner acts as the DRIVER (types the code and runs commands).
# - The other learners are NAVIGATORS (observe, guide, and provide suggestions).
#
# After each task:
# - Current learner: git add, commit, and push
# - Next learner: git pull origin main
# -------------------------------------------


# Task 1: Display Functions
# -------------------------------------------
print("-------------------------------------------\n"
    + "Task 1: Display Functions\n"
    + "-------------------------------------------")
# Create two functions that display information.
#
# TODO:
# 1. Create a function called 'display_header' that ONLY prints:
#    "=== LIBRARY BOOK LOAN SYSTEM ==="
#    "Manchester Central Library"
# 2. Create a function called 'display_menu' that ONLY prints:
#    "1. Record new loan"
#    "2. View all loans"
#    "3. Exit"
# 3. Call both functions to test them.
#
# Note: Only the DRIVER should be typing!
# Write your code below:




# -------------------------------------------
# SWAP COMPUTERS
# -------------------------------------------
# Use Git to:
# 1. Stage your changes.
# 2. Commit with an appropriate message (e.g. "Completed Task 1").
# 3. Push to the repository.
# The next learner must pull the latest version before continuing.
# -------------------------------------------


# Task 2: Functions with Parameters
# -------------------------------------------
print("-------------------------------------------\n"
    + "Task 2: Functions with Parameters\n"
    + "-------------------------------------------")
# Create a function that takes parameters and displays loan information.
#
# TODO:
# Create a function called 'display_loan' that:
# - Takes three parameters: title, author, borrower
# - Prints:
#   "--- Loan Record ---"
#   "Title: [title]"
#   "Author: [author]"
#   "Borrower: [borrower]"
#   "-------------------"
#
# Test it by calling: display_loan("1984", "George Orwell", "Sarah Smith")
#
# Note: Only the DRIVER should be typing!
# Write your code below:




# -------------------------------------------
# SWAP COMPUTERS
# -------------------------------------------
# Use Git to:
# 1. Stage your changes.
# 2. Commit with an appropriate message (e.g. "Completed Task 2").
# 3. Push to the repository.
# The next learner must pull the latest version before continuing.
# -------------------------------------------


# Task 3: Functions that Return Values
# -------------------------------------------
print("-------------------------------------------\n"
    + "Task 3: Functions that Return Values\n"
    + "-------------------------------------------")
# Create functions that return values instead of just printing.
#
# TODO:
# 1. Create a function called 'get_book_title' that:
#    - Asks the user "Enter book title: "
#    - Returns the input
# 2. Create a function called 'get_book_author' that:
#    - Asks the user "Enter book author: "
#    - Returns the input
# 3. Create a function called 'get_borrower_name' that:
#    - Asks the user "Enter borrower's name: "
#    - Returns the input
# 4. Create a function called 'create_loan_record' that:
#    - Takes three parameters: title, author, borrower
#    - Returns (NOT prints) a dictionary: {"title": title, "author": author, "borrower": borrower}
# 5. TESTING YOUR FUNCTIONS:
#    - Call each of the first three functions and store their results in variables:
#        E.g. book_title = get_book_title()
#    - Then pass those variables (e.g. book_title) into create_loan_record() and store the result:
#        E.g. loan = create_loan_record(book_title, another_variable, another_variable)
#    - Finally, print the dictionary to check your result.
#
# Test by calling all four functions, storing results, and printing the dictionary.
#
# Note: Only the DRIVER should be typing!
# Write your code below:




# -------------------------------------------
# SWAP COMPUTERS
# -------------------------------------------
# Use Git to:
# 1. Stage your changes.
# 2. Commit with an appropriate message (e.g. "Completed Task 3").
# 3. Push to the repository.
# The next learner must pull the latest version before continuing.
# -------------------------------------------


# -------------------------------------------
# EXTENSION ACTIVITIES
# -------------------------------------------

# Extension 1: Recording Multiple Loans
# -------------------------------------------
print("-------------------------------------------\n"
    + "Extension 1: Recording Multiple Loans\n"
    + "-------------------------------------------")
# Store loan records in a list so you can track multiple books.
#
# TODO:
# 1. Create an empty list at the top: loan_records = []
# 2. Create a function called 'record_new_loan' that:
#    - Calls get_book_title(), get_book_author(), get_borrower_name()
#    - Creates a loan dictionary using create_loan_record()
#    - Adds the dictionary to loan_records list
#    - Prints "Loan recorded successfully!"
#    - Prints "Total loans recorded: [number]"
# 3. Create a function called 'view_all_loans' that:
#    - Prints "=== ALL LOAN RECORDS ==="
#    - If loan_records is empty, print "No loans recorded yet."
#    - Otherwise, loop through loan_records and display each using display_loan()
#    - Print "Total loans: [number]" at the end
#
# Test by calling record_new_loan() twice, then view_all_loans().
#
# Note: Only the DRIVER should be typing!
# Write your code below:




# -------------------------------------------
# SWAP COMPUTERS
# -------------------------------------------
# Use Git to:
# 1. Stage your changes.
# 2. Commit with an appropriate message (e.g. "Completed Extension 1").
# 3. Push to the repository.
# The next learner must pull the latest version before continuing.
# -------------------------------------------


# Extension 2: Input Validation
# -------------------------------------------
print("-------------------------------------------\n"
    + "Extension 2: Input Validation\n"
    + "-------------------------------------------")
# Make sure staff don't leave any fields blank!
#
# TODO:
# 1. Create a function called 'get_valid_input' that:
#    - Takes one parameter: prompt
#    - Uses a while loop to keep asking for input
#    - Gets input using the prompt parameter
#    - Strips whitespace using .strip()
#    - If input is empty, print "This field cannot be blank!"
#    - If valid, return the input
# 2. Update these three functions to use get_valid_input:
#    - get_book_title: use get_valid_input("Enter book title: ")
#    - get_book_author: use get_valid_input("Enter book author: ")
#    - get_borrower_name: use get_valid_input("Enter borrower's name: ")
#
# Test by trying to leave fields blank - it should keep asking!
#
# Note: Only the DRIVER should be typing!
# Write your code below:




# -------------------------------------------
# SWAP COMPUTERS
# -------------------------------------------
# Use Git to:
# 1. Stage your changes.
# 2. Commit with an appropriate message (e.g. "Completed Extension 2").
# 3. Push to the repository.
# The next learner must pull the latest version before continuing.
# -------------------------------------------


# Extension 3: Search Functionality
# -------------------------------------------
print("-------------------------------------------\n"
    + "Extension 3: Search Functionality\n"
    + "-------------------------------------------")
# Let staff search for loans by borrower name.
#
# TODO:
# Create a function called 'search_by_borrower' that:
# - Asks "Enter borrower's name to search: "
# - Converts search to lowercase
# - Creates a variable found_count = 0
# - Loops through each loan in loan_records
# - If search term appears in borrower's name (both lowercase):
#   * Display that loan using display_loan()
#   * Increase found_count by 1
# - After loop, print "Found [found_count] loan(s)"
#
# HINT: if search.lower() in loan["borrower"].lower():
#
# Note: Only the DRIVER should be typing!
# Write your code below:




# -------------------------------------------
# SWAP COMPUTERS
# -------------------------------------------
# Use Git to:
# 1. Stage your changes.
# 2. Commit with an appropriate message (e.g. "Completed Extension 3").
# 3. Push to the repository.
# The next learner must pull the latest version before continuing.
# -------------------------------------------


# -------------------------------------------
# ADVANCED ACTIVITY
# -------------------------------------------
print("-------------------------------------------\n"
    + "ADVANCED ACTIVITY\n"
    + "-------------------------------------------")
# Create a complete working system with a menu loop.
#
# TODO:
# 1. Create a function called 'get_menu_choice' that:
#    - Uses a while loop to keep asking for input
#    - Asks "Choose option (1-3): "
#    - If input is "1", "2", or "3", return it
#    - Otherwise print "Invalid choice! Please enter 1, 2, or 3."
# 2. Create a function called 'main' that:
#    - Calls display_header()
#    - Uses a while loop that runs forever
#    - Calls display_menu()
#    - Gets choice using get_menu_choice()
#    - If choice is "1": call record_new_loan()
#    - If choice is "2": call view_all_loans()
#    - If choice is "3": print "Thank you!" and break
#    - Print a blank line after each action
# 3. At the very bottom of your file, call main()
#
# Note: Only the DRIVER should be typing!
# Write your code below:




# -------------------------------------------
# Submitting Your Work
# -------------------------------------------
# Use Git to:
# 1. Stage your final changes.
# 2. Commit with an appropriate message (e.g. "Completed Advanced Activity").
# 3. Push your final version to the repository.
# -------------------------------------------
