#!/usr/bin/python3

def multiple_returns(sentence):
    first_letter = sentence[0] if sentence else None
    return len(sentence), first_letter
