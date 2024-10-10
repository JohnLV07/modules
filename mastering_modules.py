# Mastering python modules and aliases

'''
Task 1: Custom module with aliases

Problem Statement:
    -Create a custom module named: 'text_utils.py' with functions for string manipulation
    (reversing a string, capitalization)
    In your main script, import this module using an alias utilize its functions.

'''
#Code Example:
  # text_utils.py
    # def reverse_string(s):
    #     # function to reverse a string

    # def capitalize_string(s):
    #     # function to capitalize a string

    # main.py
    # Import text_utils using an alias and utilize its functions

    # Expected Outcome: Your main script should be able to use the functions from `text_utils.py` via an alias, demonstrating an understanding of custom module creation and aliasing.


    # main.py

# Import the text_utils module using an alias
import text_utils as alias

def main():
    user_input = input("Enter a word: ")

    reversed_word = alias.reverse_string(user_input)
    capitalized_word = alias.capitalize_string(user_input)

    print(f"Reversed String: {reversed_word}")
    print(f"Capitalized String: {capitalized_word")

if __name__ == "__main__":
    main()
