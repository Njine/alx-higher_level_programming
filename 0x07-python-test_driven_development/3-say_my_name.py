#!/usr/bin/python3

'''
   3-say_my_name
   Contains a function that prints names
'''

def say_my_name(first_name, last_name=""):
    """
    Print the formatted name "My name is <first name> <last name>".

    Args:
        first_name (str): The first name.
        last_name (str, optional): The last name (default is an empty string).

    Raises:
        TypeError: If first_name or last_name is not a string.
    """
    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')
    if not isinstance(last_name, str):
        raise TypeError('last_name must be a string')
    
    formatted_name = "My name is {} {}".format(first_name, last_name)
    print(formatted_name)

if __name__ == "__main__":
    say_my_name("John", "Smith")
    say_my_name("Walter", "White")
    say_my_name("Bob")
