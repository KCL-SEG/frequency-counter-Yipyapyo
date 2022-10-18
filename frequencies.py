"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(itemsIn):
    items = map(str, itemsIn)
    frequencies = {}
    for item in items:
        if item in frequencies:
            frequencies[item] += 1
        else:
            frequencies[item] = 1
    
    return frequencies
