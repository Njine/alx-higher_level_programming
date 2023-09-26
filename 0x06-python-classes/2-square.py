#!/usr/bin/python3
'''2-square.py: Defines size as an int and also greater or equal to 0'''


class Square:
    '''Creates  Square type'''

    def __init__(self, dimention=0):
        '''Initializes Square with size'''
        self.__size = dimention
        if type(dimention) is not int:
            raise TypeError('size in not an integer')
        if dimention < 0:
            raise ValueError('size is not greater or equal 0')
