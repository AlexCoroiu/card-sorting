# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 17:02:08 2020

@author: Alexandra Coroiu

"""
import pandas

#TODO: use csv.s
#TODO: create proper results matrix

class Tree(object):
    def __init__(self):
        self.name = ""
        self.children = [] #subcategories
        self.cards = []
        self.level = 0
        self.unsorted = []
    
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
        child.set_level(self.level+1)
        self.children.append(child)
    
    def add_card(self,card):
        self.cards.append(card)
    
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
    
    #this should make a matrix and keep track of the depth as well
    def get_matrix(self,matrix,input):
        for card1 in input:
            i = input.index(card1)
            for card2 in input:
                j = input.index(card2)
                if card1 in self.cards and card2 in self.cards:
                    matrix[i][j] = self.level
        if len(self.children)>0:  
            for child in self.children:
                matrix = child.get_matrix(matrix, input)
        return matrix                

input_cards = None #the list of cards that needs to be sorted
cards_tree = None #the tree structure used to represent the sorted cards

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
              
def save_results(file):
    results_file = open(file,'w')
    result = ""
    result = cards_tree.get_results(result)
    results_file.write(result)
    results_file.close()

def save_matrix(file):
    cards_len = len(input_cards)
    results_matrix = [[0 for i in range(cards_len)] for j in range(cards_len)] 
    results_matrix = cards_tree.get_matrix(results_matrix,input_cards)
    results_matrix = calculate_jaccard(results_matrix)
    data_frame = pandas.DataFrame(results_matrix, index = input_cards, columns = input_cards)
    data_frame.to_csv(file)
    
def calculate_jaccard(matrix):
    cards_len = len(input_cards)
    jaccard = [[0 for i in range(cards_len)] for j in range(cards_len)] 
    for i in range(0,cards_len):
        for j in range(0,cards_len):
            jaccard[i][j] = matrix[i][j]/(matrix[i][i] + matrix[j][j] - matrix[i][j])
    return jaccard
    
    
