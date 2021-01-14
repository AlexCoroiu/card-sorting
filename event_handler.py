# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 18:35:21 2020

@author: Alex
"""
import pygame
from program_invariables import Actions, Names, Display
import data_manager
import painter 

root_tree = None
#cards = None
tree = None
selected = None
finished = False
subcategory = False

def handle_setup():
    #get file data
    global cards, root_tree, tree
    cards, root_tree = data_manager.open_cards(Names.INPUT_FILE.value)
    tree = root_tree
    print("cards loaded")

def handle_start(event):
    if event.type == pygame.MOUSEBUTTONUP:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        rect = painter.start_button.get_rect()
        if rect.collidepoint(mouse_x,mouse_y):
            #add default nr of categories
            for i in range (0, Display.CATEGORIES.value):
                tree.add_new_child()
            print('experiment started')
            return Actions.NEXT

def handle_experiment(event):
    if event.type == pygame.MOUSEBUTTONUP:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        
        global finished
        global selected
        
        #check next button
        if finished:
            rect = painter.next_button.get_rect()
            if rect.collidepoint(mouse_x, mouse_y):
                print('cards sorted')
                return Actions.NEXT
            
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
                if c.get_text() == selected:
                    selected = None
                    print('card de-selected')
                    return None
                    
                else:
                    #select
                    category = c.get_data()
                    if  category == painter.unsorted_category.get_data():
                        selected = c.get_text()
                    print('card selected')
                    return None
        
        #check categories buttons
        if selected != None: 
            for c in painter.categories_buttons:
                rect = c.get_rect()
                if rect.collidepoint(mouse_x, mouse_y):
                    #change data
                    data_tree = c.get_data()
                    data_cards = data_tree.get_cards()
                    if selected not in data_cards:
                        data_tree.add_card(selected)
                    selected = None
                    if len(tree.get_unsorted()) == 0:
                        finished = True
                    print('card moved')
                    return None

def handle_instructions(event):
    if event.type == pygame.MOUSEBUTTONUP:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        rect = painter.back_button.get_rect()
        if rect.collidepoint(mouse_x, mouse_y):
            print('instructions read')
            return Actions.BACK
    
     
def handle_finish(event):
    if event.type == pygame.MOUSEBUTTONUP:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        rect = painter.finish_button.get_rect()
        if rect.collidepoint(mouse_x, mouse_y):
            print('experiment finished')
            return Actions.NEXT
        
def handle_results():
    #save results
    data_manager.save_results(Names.RESULTS_FILE.value)
    data_manager.save_matrix(Names.MATRIX_FILE.value)
    print('results saved')