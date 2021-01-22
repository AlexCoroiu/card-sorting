# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 15:31:27 2020

@author: Alexandra Coroiu

This module tests the functionality of the data_manager.

"""

import data_manager

#automatic test
#test correctly reading cards from a file
def test_open_cards():
    print('\nTEST open_cards')
    #expected contains no duplicates
    expected = ['cheese','pineapple','kimchi','pink','seaweed','blue','water','flying','jewelry','biodegradable','towel','static','laptop','maroon','charger','tomato','pillow','wireless','blanket','plastic']
    actual, actual_tree = data_manager.open_cards('test_cards_file.csv')
    print(actual)
    actual_tree_cards = actual_tree.get_cards()
    return expected == actual and expected == actual_tree_cards


#manual tests
#after running please check the output file to see if it has the desired structure

#test the creation and writing to a file of the simple results
def test_save_results():
    print('\nTEST save_results')
    file = 'test_results_file.txt'
    data_manager.save_results(file)  

#test the creationg and writing to a file of the matrix results   
def test_save_matrix():
    print('\nTEST save_matrix')
    file = 'test_matrix_file.csv'
    data_manager.save_matrix(file)

#execute the test function that reads cards from the input file         
#test open_cards 
if test_open_cards():
    print('==> open_cards PASSED: all cards were succesfully read')
else:
    print('==> open_cards FAILED')

#creating a test data tree
test_cards,test_tree = data_manager.open_cards('test_cards_file.csv')

food = ['cheese','pineapple','kimchi','seaweed','tomato']
food_tree = data_manager.Tree()
food_tree.set_cards(food)
food_tree.set_level(1)

food_fruit = ['pineapple','tomato']
food_fruit_tree = data_manager.Tree()
food_fruit_tree.set_cards(food_fruit)
food_fruit_tree.set_level(2)

food_fruit_sweet = ['pineapple']
food_fruit_sweet_tree = data_manager.Tree()
food_fruit_sweet_tree.set_cards(food_fruit_sweet)
food_fruit_sweet_tree.set_level(3)

food_fruit_other = list(set(food_fruit) - set(food_fruit_sweet))
food_fruit_other_tree = data_manager.Tree()
food_fruit_other_tree.set_cards(food_fruit_other)
food_fruit_other_tree.set_level(3)

food_other = list(set(food) - set(food_fruit))
food_other_tree = data_manager.Tree()
food_other_tree.set_cards(food_other) 
food_other_tree.set_level(2)

colors = ['pink','blue','maroon']
colors_tree = data_manager.Tree()
colors_tree.set_cards(colors)
colors_tree.set_level(1)

home = ['blanket','towel','pillow']
home_tree = data_manager.Tree()
home_tree.set_cards(home)
home_tree.set_level(1)

water = ['water']
water_tree = data_manager.Tree()
water_tree.set_cards(water)
water_tree.set_level(1)

flying = ['flying']
flying_tree = data_manager.Tree()
flying_tree.set_cards(flying)
flying_tree.set_level(1)

jewelry = ['jewelry']
jewelry_tree = data_manager.Tree()
jewelry_tree.set_cards(jewelry)
jewelry_tree.set_level(1)

waste = ['biodegradable','plastic']
waste_tree = data_manager.Tree()
waste_tree.set_cards(waste)
waste_tree.set_level(1)

computer = ['static','laptop','charger','wireless']
computer_tree = data_manager.Tree()
computer_tree.set_cards(computer)
computer_tree.set_level(1)

children_tree = [food_tree,colors_tree,home_tree,water_tree,flying_tree,jewelry_tree,waste_tree,computer_tree]
test_tree.set_children(children_tree)

children_food = [food_fruit_tree, food_other_tree]
food_tree.set_children(children_food)

children_food_fruit = [food_fruit_sweet_tree,food_fruit_other_tree]
food_fruit_tree.set_children(children_food_fruit)

#execute the test functions that write results to output files    
#test save_results
test_save_results()
print('-> please inspect test_results_file.txt')

#test save_matrix
test_save_matrix()
print('-> please inspect test_matrix_file.txt')