#!/usr/bin/python3

"""3-say_my_name Contains a function that prints names."""


def say_my_name(first_name, last_name=""):
    
    """
    Python function takes two strings and prints them
    """


msgerr = 'first_name must be a string'


msgerr1 = 'last_name must be a string'
name = 'My name is '


def say_my_name(first_name, last_name=""):
    """Print first name and last."""
    if not isinstance(first_name, str):
        raise TypeError(msgerr)
    if not isinstance(last_name, str):
        raise TypeError(msgerr1)
    else:
        print('My name is {} {}'.format(first_name, last_name))
