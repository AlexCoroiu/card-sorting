# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 17:02:08 2020

@author: Alexandra Coroiu

This module holds the tree data structure that represents the cards and categories of the experiment

"""
import pandas

#tree class
class Tree(object):
    #constructor
    def __init__(self):
        self.name = ""
        self.children = [] #subcategories
        self.cards = []
        self.level = 0
        self.unsorted = []
        self.parent = None
    
    #functions to updateclass variables
    def set_name(self,name):    
        self.name = name
        
    def set_level(self,lvl):
        self.level = lvl
    
    def set_children(self,children):
        self.children = children
    
    def set_cards(self,cards):
        self.cards = cards
        
    def add_child(self, child):
        self.children.append(child)
    
    def add_new_child(self):
        child = Tree()
        child.set_parent(self)
        child.set_level(self.level+1)
        self.children.append(child)
    
    def add_card(self,card):
        self.cards.append(card)
    
    def set_parent(self,parent):
        self.parent = parent
    
    #functions that return class variables
    def get_name(self):
        return self.name

    def get_level(self):
        return self.level
    
    def get_children(self):
        return self.children
    
    def get_cards(self):
        return self.cards
    
    def get_unsorted(self):
        sorted = []
        for c in self.children:
            sorted.extend(c.get_cards())
        self.unsorted = list(set(self.cards) - set(sorted))
        return self.unsorted
    
    def get_parent(self):
        return self.parent
           
    #function that returns a string representing the tree structure
    def get_results(self,result):
        i = self.level
        indent = '\t'*i
        result = result + indent + self.name + ": ["
        for card in self.cards:
                result = result + card + ", "
        result = result[:-2]
        result = result + ']\n'
        if len(self.children)>0:  
            for child in self.children: 
                #doesn't print empty categories
                if len(child.get_cards()) >0:
                    result = child.get_results(result)          
        return result
    
    #function that returns a matrix representing the tree structure 
    def get_matrix(self,matrix,input):
        for card1 in input:
            i = input.index(card1)
            for card2 in input:
                j = input.index(card2)
                if card1 in self.cards and card2 in self.cards:
                    #stored the deepest common level of two cards 
                    #this represents the cardinality of the intersection between two cards
                    matrix[i][j] = self.level
        if len(self.children)>0:  
            for child in self.children:
                matrix = child.get_matrix(matrix, input)
        return matrix                

input_cards = None #the list of cards that needs to be sorted
cards_tree = None #the tree structure used to represent the sorted cards

#functions to deal with external files

#read input file
def open_cards(file):
    global input_cards
    input_cards = []
    data_frame = pandas.read_csv(file, names=['cards'])
    #delete duplicated cards
    data_frame.drop_duplicates(keep='first', inplace = True)
    input_cards = data_frame.cards.to_list()
    #start tree
    global cards_tree
    cards_tree = Tree()
    cards_tree.set_cards(input_cards)
    return input_cards,cards_tree

#save simple text results             
def save_results(file):
    results_file = open(file,'w')
    result = ""
    result = cards_tree.get_results(result)
    results_file.write(result)
    results_file.close()

#save processed complex results in the form of a matrix to a.csv file
def save_matrix(file):
    cards_len = len(input_cards)
    results_matrix = [[0 for i in range(cards_len)] for j in range(cards_len)] 
    results_matrix = cards_tree.get_matrix(results_matrix,input_cards)
    #calculate jaccard similarity coefficient for the whole matrix
    results_matrix = calculate_jaccard(results_matrix)
    data_frame = pandas.DataFrame(results_matrix, index = input_cards, columns = input_cards)
    data_frame.to_csv(file)

#calculates the jaccard index for all the elements of a matrix 
#the parameter matrix has to already contain the cardinality of the intersection of any two cards    
def calculate_jaccard(matrix):
    cards_len = len(input_cards)
    jaccard = [[0 for i in range(cards_len)] for j in range(cards_len)] 
    for i in range(0,cards_len):
        for j in range(0,cards_len):
            #calculate jaccard index for two cards
            jaccard[i][j] = matrix[i][j]/(matrix[i][i] + matrix[j][j] - matrix[i][j])
    return jaccard
    
    
