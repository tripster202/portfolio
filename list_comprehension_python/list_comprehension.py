# IMPORTS #
import random

# NOTES #
# https://www.kaggle.com/code/colinmorris/loops-and-list-comprehensions

def squares():
    squares = [n**2 for n in range(10)]
    print(squares)

    squares = []
    for n in range(10):
        squares.append(n**2)
    print(squares)

def planets():
    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    short_planets = [planet for planet in planets if len(planet) < 6]
    print(short_planets)

def random_list(length):
    if 0 < length <= 10:
        print([random.randint(10,99) for idx in range(length)])
    else: print(list())

if __name__ == "__main__":
    squares()
    planets()
    random_list(10)