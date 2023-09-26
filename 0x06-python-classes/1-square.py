#!/usr/bin/python3
'''1-square.py: this python script defines a square,
   private attribution of size'''


class Square:
        '''Makes  Square type'''

        def __init__(self, dimention):
            '''Initializes Square with size'''

            self.__size = dimention
