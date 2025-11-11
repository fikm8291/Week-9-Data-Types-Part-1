# -------------------------------------------
# Exercise 1: Functions
# -------------------------------------------
# In this exercise, you'll work in groups of 2–3.
# You'll learn about FUNCTIONS - reusable blocks of code.
#
# Basic function:
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
# 1. Create a function called 'display_header' that prints:
#    "=== LIBRARY BOOK LOAN SYSTEM ==="
#    "Manchester Central Library"
# 2. Create a function called 'display_menu' that prints:
#    "1. Record new loan"
#    "2. View all loans"
#    "3. Exit"
# 3. Call both functions to test them.
#
# Write your code below:




# -------------------------------------------
# SWAP COMPUTERS
# -------------------------------------------
# git add Ex1_functions.py
# git commit -m "Completed Task 1"
# git push origin main
# Next learner: git pull origin main
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
# Write your code below:




# -------------------------------------------
# SWAP COMPUTERS
# -------------------------------------------
# git add Ex1_functions.py
# git commit -m "Completed Task 2"
# git push origin main
# Next learner: git pull origin main
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
#    - Returns a dictionary: {"title": title, "author": author, "borrower": borrower}
#
# Test by calling all four functions, storing results, and printing the dictionary.
#
# Write your code below:




# -------------------------------------------
# SWAP COMPUTERS
# -------------------------------------------
# git add Ex1_functions.py
# git commit -m "Completed Task 3"
# git push origin main
# Next learner: git pull origin main
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
# Write your code below:




# -------------------------------------------
# SWAP COMPUTERS
# -------------------------------------------
# git add Ex1_functions.py
# git commit -m "Completed Extension 1"
# git push origin main
# Next learner: git pull origin main
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
# Write your code below:




# -------------------------------------------
# SWAP COMPUTERS
# -------------------------------------------
# git add Ex1_functions.py
# git commit -m "Completed Extension 2"
# git push origin main
# Next learner: git pull origin main
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
# Write your code below:




# -------------------------------------------
# SWAP COMPUTERS
# -------------------------------------------
# git add Ex1_functions.py
# git commit -m "Completed Extension 3"
# git push origin main
# Next learner: git pull origin main
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
# Write your code below:




# -------------------------------------------
# Submitting Your Work
# -------------------------------------------
# git add Ex1_functions.py
# git commit -m "Completed Advanced"
# git push origin main
# -------------------------------------------
