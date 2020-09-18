"""
Name: Banana McClane
Date created: 24-Jan-2020
Version of Python: 3.4
This script is for randomly selecting restaurants! It takes a list as an input and randomly selects one item from the list, which is output in human readable form on-screen.
"""
import random # importing 'random' allows us to pick a random element from a list
restaurant_list = ['Dominos Pizza', 'Mysore', 'Restaurant Thailande', 'Lemeac', 'Chez Leveque', 'Sushi', 'Italian', 'Poutineville']
restaurant_item = random.choice(restaurant_list)
print ("Randomly selected item from list is " + restaurant_item)
