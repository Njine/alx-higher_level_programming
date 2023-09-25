#!/usr/bin/python3
def safe_print_division(a, b):
    division = None
    try:
        division = a / b
    except ZeroDivisionError:
        pass
    finally:
        print("Inside result: {}".format(division))
    return division
