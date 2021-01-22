# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 18:35:21 2020

@author: Alexandra Coroiu

This module deals with the input from the user for each state.
It updates the data structure according to the user actions.

"""
import pygame
from program_invariables import Actions, Names, BoardStates, new_children, Display
import data_manager
import painter 

#variables used to store the information about the state of the data
root_tree = None
tree = None
selection = None
board_state = BoardStates.NEW
subcategory = False #experiment starts at the base of the data tree
page = 0 
prev_page = 0

#functions that check the pygame event, update the data and return actions 
#actions are determined by checking what element of a page was clicked on

#BEGIN
def handle_begin():
    print('welcome')
    #load data from file
    global cards, root_tree, tree
    cards, root_tree = data_manager.open_cards(Names.INPUT_FILE.value)
    tree = root_tree
    print("cards loaded")

#SETUP    
def handle_setup(event):
    if event.type == pygame.MOUSEBUTTONUP:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        #check next button
        rect = painter.next_button.get_rect()
        if rect.collidepoint(mouse_x, mouse_y):
            print('setup checked')
            return Actions.NEXT

#START    
def handle_start(event):
    if event.type == pygame.MOUSEBUTTONUP:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        #check start button
        rect = painter.start_button.get_rect()
        if rect.collidepoint(mouse_x,mouse_y):
            #add default nr. of categories
            for i in range (0, new_children):
                tree.add_new_child()
            print('experiment started')
            return Actions.NEXT

#EXPERIMENT
#also considers the state of the working board when interpreting user input
def handle_experiment(event):
    if event.type == pygame.MOUSEBUTTONUP:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        
        global board_state
        global selection
        global tree
        global subcategory
        global page
        global prev_page
                
        
        #check next button (can only be clicked when finshed)
        if board_state == BoardStates.FINAL and not subcategory:
            rect = painter.next_button.get_rect()
            if rect.collidepoint(mouse_x, mouse_y):
                print('cards sorted')
                return Actions.NEXT
        
        #check back button (can only be clicked when finished with a subcategory)
        if board_state != BoardStates.EDITING and subcategory:
            rect = painter.back_button.get_rect()
            if rect.collidepoint(mouse_x, mouse_y):
                #recreate final state of previous category
                parent = tree.get_parent()
                #check if going back to base
                if parent.get_parent() == None:
                    subcategory = False
                board_state = BoardStates.FINAL
                selection = None
                page = prev_page
                tree = parent
                print('category sorted')
                return Actions.BACK
            
        #check left navigation arrow
        if page > 0:
            rect = painter.left_arrow.get_rect()
            if rect.collidepoint(mouse_x, mouse_y):
                #update board page number 
                page = page- 1
                print('previous categories')
                return None
        
        #check right navigation arrow
        nr_categories = len(tree.get_children())
        displayed_cat = (page +1)*Display.CATEGORIES.value
        if nr_categories > displayed_cat:
            rect = painter.right_arrow.get_rect()
            if rect.collidepoint(mouse_x, mouse_y):
                #update board page 
                page = page + 1
                print('next categories')
                return None
                       
        #check help button
        rect = painter.help_button.get_rect()
        if rect.collidepoint(mouse_x, mouse_y):
            print('help')
            return Actions.HELP
        
        #check card buttons
        for c in painter.cards_buttons:
            rect = c.get_rect()
            if rect.collidepoint(mouse_x, mouse_y):
                #de-select
                if c.get_text() == selection:
                    #update selection
                    selection = None
                    print('card de-selected')
                    return None     
                #select
                else:
                    category = c.get_data()
                    #can only select unsorted cards
                    if  category == painter.unsorted_category.get_data():
                        #update selection
                        selection = c.get_text()
                        print('card selected')
                        return None
        
        #check categories buttons for sorting a card
        if selection != None: 
            for c in painter.categories_buttons:
                rect = c.get_rect()
                if rect.collidepoint(mouse_x, mouse_y):
                    #update data
                    data_tree = c.get_data()
                    data_cards = data_tree.get_cards()
                    if selection not in data_cards:
                        data_tree.add_card(selection)
                    selection = None
                    #update board state after move
                    board_state = BoardStates.EDITING
                    if len(tree.get_unsorted()) == 0:
                        board_state = BoardStates.FINAL
                    print('card moved')
                    return None     
                
        #check categories button for going into category (can only be clicked when finished sorting)
        elif board_state == BoardStates.FINAL:
            for c in painter.categories_buttons:
                rect = c.get_rect()
                if rect.collidepoint(mouse_x, mouse_y):
                    #new current tree
                    tree = c.get_data()
                    subcategory = True
                    prev_page = page
                    page = 0
                    #create environment for new category
                    if len(tree.get_children()) == 0:
                        for i in range (0, new_children):
                            tree.add_new_child()                 
                        board_state = BoardStates.NEW
                    print('entered category')
                    return None           

#INSTRUCTIONS                               
def handle_instructions(event):
    if event.type == pygame.MOUSEBUTTONUP:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        #check back button
        rect = painter.back_button.get_rect()
        if rect.collidepoint(mouse_x, mouse_y):
            print('instructions read')
            return Actions.BACK
    
#FINISH     
def handle_finish(event):    
    if event.type == pygame.MOUSEBUTTONUP:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        #check finish button
        rect = painter.finish_button.get_rect()
        if rect.collidepoint(mouse_x, mouse_y):
            print('experiment finished')            
            return Actions.NEXT
        #check back button
        rect = painter.back_button.get_rect()
        if rect.collidepoint(mouse_x, mouse_y):
            print('experiment not finished')
            return Actions.BACK

#RESULTS                
def handle_results(event):    
    if event.type == pygame.MOUSEBUTTONUP:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        #check next button
        rect = painter.next_button.get_rect()
        if rect.collidepoint(mouse_x, mouse_y):
            print('experiment ended')
            return Actions.NEXT

#END
def handle_end():
    #save results
    data_manager.save_results(Names.RESULTS_FILE.value)
    data_manager.save_matrix(Names.MATRIX_FILE.value)
    print('results saved')
    print('good bye')
