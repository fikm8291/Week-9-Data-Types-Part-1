# -------------------------------------------
# Exercise 1: Functions
# -------------------------------------------
#
# GOAL:
# 1. Master the concept of Functions: def, parameters, and return values.
# 2. Review Data Structures: Storing dictionaries inside a list.
# 3. Build a prototype similar to Assessment 3 requirements.
#
# CONCEPT:
# A function is a named block of code. Think of it like a "recipe" 
# that you store away and only use when you call its name.
#
# -------------------------------------------



# -------------------------------------------
# Task 1: Display Functions (No Parameters)
# -------------------------------------------
print("-------------------------------------------\n"
    + "Task 1: Display Functions\n"
    + "-------------------------------------------")

# To create a function, use 'def' followed by a name and brackets.
# Example:
# def say_hello():
#     print("Hello!")
#
# To use it, you must "call" it by name: say_hello()

# TODO:
# 1. Create a function called 'display_header' that prints:
#    "=== GM PUBLIC SERVICE RECORD SYSTEM ==="
#    "Official Prototype v1.0"
# 2. Create a function called 'display_menu' that prints:
#    "1. Add New Record"
#    "2. View All Records"
#    "3. Search Records"
#    "4. Exit"
# 3. Call both functions at the bottom of this task to test them.

# Write your code below:


# -------------------------------------------
# Task 2: Formatting Summaries (Using Parameters)
# -------------------------------------------
print("\n-------------------------------------------\n"
    + "Task 2: Formatting Summaries\n"
    + "-------------------------------------------")

# Parameters are "placeholders" for information the function needs.
# Example:
# def show_age(name, age):
#     print(f"{name} is {age} years old.")
#
# When calling it, you provide the real data: show_age("Alice", 25)

# TODO:
# 1. Create a function 'display_record' that takes three parameters:
#    primary_item, category, and location.
# 2. Use an f-string to print a clean summary that works for any brief.
# 3. Test it by calling: display_record("Emergency Call", "Medical", "Manchester")
#
# EXPECTED OUTPUT:
# --- RECORD DETAILS ---
# Subject: Emergency Call
# Category: Medical
# Location: Manchester
# ----------------------

# Write your code below:


# -------------------------------------------
# Task 3: Capturing Data (Return Values)
# -------------------------------------------
print("\n-------------------------------------------\n"
    + "Task 3: Capturing Data\n"
    + "-------------------------------------------")

# 'return' is used to send information BACK to the main program.
# Example:
# def get_colour():
#     ans = input("Enter colour: ")
#     return ans
#
# my_choice = get_colour()  # The returned value is stored in 'my_choice'

# TODO:
# 1. Create three input functions: 'get_subject()', 'get_category()', 
#    and 'get_location()'. Each should return the user's input.
# 2. Create 'create_entry(sub, cat, loc)' that returns a dictionary 
#    using those three variables as values.
# 3. Test: Call the inputs, pass them to create_entry, and print the dictionary.

# Write your code below:


# -------------------------------------------
# SAVING YOUR WORK
# -------------------------------------------
# You have completed the Core Tasks. Let's save.
# 1. Save this file.
# 2. Use Git in the terminal to:
#    - Stage your changes.
#    - Commit with a message (e.g. "Core logic complete").
#    - Push your work to the main branch.
# -------------------------------------------


# -------------------------------------------
# EXTENSION ACTIVITIES
# -------------------------------------------

# Extension 1: The Master Database
# -------------------------------------------
print("\n-------------------------------------------\n"
    + "Extension 1: The Master Database\n"
    + "-------------------------------------------")

# TODO:
# 1. Create an empty list called 'database' at the top of your script.
# 2. Create 'add_new_record()' that:
#    - Calls your Task 3 input functions.
#    - Creates a dictionary and appends it to 'database'.
#    - Prints "Entry successfully logged!"
# 3. Create 'view_database()' that loops through 'database' 
#    and calls 'display_record()' for every item.

# Write your code below:


# Extension 2: Data Validation
# -------------------------------------------
print("\n-------------------------------------------\n"
    + "Extension 2: Data Validation\n"
    + "-------------------------------------------")

# Use a while loop inside your function to keep asking until the user
# types something valid.
# Example:
# def get_name():
#     name = ""
#     while name == "":
#         name = input("Enter name: ").strip()
#     return name

# TODO:
# 1. Create 'get_valid_input(prompt)' that uses a while loop to 
#    ensure the user doesn't leave a field blank (.strip() != "").
# 2. Update your Task 3 functions to use 'get_valid_input' 
#    instead of standard 'input()'.

# Write your code below:


# Extension 3: Search
# -------------------------------------------
print("\n-------------------------------------------\n"
    + "Extension 3: Search\n"
    + "-------------------------------------------")

# TODO:
# 1. Create 'search_records()' that asks the user for a search term.
# 2. Loop through 'database' variable from Extension 1 task.
# 3. IF the search term is 'in' the record subject (use .lower()), 
#    call your 'display_record()' function from Task 2 to show it.

# Write your code below:


# -------------------------------------------
# SAVING YOUR WORK
# -------------------------------------------
# You have completed the Extensions. Let's save.
# 1. Save this file.
# 2. Use Git in the terminal to:
#    - Stage your changes.
#    - Commit with a message (e.g. "Validation and search complete").
#    - Push your work to the main branch.
# -------------------------------------------


# -------------------------------------------
# ADVANCED ACTIVITY: The System Controller
# -------------------------------------------
print("\n-------------------------------------------\n"
    + "ADVANCED ACTIVITY: The System Controller\n"
    + "-------------------------------------------")

# A "Main Menu" loop keeps your program running until the user wants to quit.
# Use your 'display_menu()' function inside a 'while True' loop.

# TODO:
# 1. Create 'get_menu_choice()' that only returns "1", "2", "3", or "4".
# 2. Create a 'main()' function with a 'while True' loop that:
#    - Displays the branding and menu.
#    - Routes the user to the correct function based on their choice.
#    - Exits the loop if "4" is selected.
# 3. Call 'main()' at the very bottom of your file.

# Write your code below:


# -------------------------------------------
# SAVING YOUR WORK
# -------------------------------------------
# You have completed the Advanced Activity. Let's save.
# 1. Save this file.
# 2. Use Git in the terminal to:
#    - Stage your changes.
#    - Commit with a message (e.g. "Full program complete").
#    - Push your final work to the main branch.
# -------------------------------------------
