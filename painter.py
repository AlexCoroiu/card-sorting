# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 19:19:22 2020

@author: Alexandra Coroiu

This module prints output to the user.
It draws the pages and all the elements on them according to the data.

"""

import pygame
import UI_objects
from program_invariables import Colors, Names, Fonts, Positions, Sizes, instructions, Display, BoardStates

#variables used to store information about the state of the data
tree = None
selection = None
board_state = BoardStates.NEW
subcategory = False
page = 0

#initializing the pygame screen
screen = None
def set_screen():
    global screen
    screen = pygame.display.get_surface()

#button varibales

#predefined buttons
start_button = UI_objects.BigButton(Names.START_BUTTON.value)
finish_button = UI_objects.BigButton(Names.FINISH_BUTTOn.value)
next_button = UI_objects.SmallButton(Names.NEXT_BUTTON.value,
                          Positions.NEXT_BUTTON.value)
back_button = UI_objects.SmallButton(Names.BACK_BUTTON.value,
                          Positions.BACK_BUTTON.value)
help_button = UI_objects.SmallButton(Names.HELP_BUTTON.value,
                                     Positions.HELP_BUTTON.value)
left_arrow = UI_objects.Arrow(Names.LEFT.value, Positions.LEFT.value)
right_arrow = UI_objects.Arrow(Names.RIGHT.value, Positions.RIGHT.value)

#buttons that will be created and updated during th eexperiment
unsorted_category = None
categories_buttons = []
cards_buttons = []

#functions that draw the pages for each program state

#BEGIN
def draw_begin():
    screen.fill(Colors.BLACK.value)
    draw_big_title(Names.BEGIN.value, Names.EXPERIMENT.value)
    pygame.display.update()

#SETUP    
def draw_setup(tree_update):
    #update the tree variable with the current value from the model
    global tree
    tree = tree_update       
    #draw page
    screen.fill(Colors.WHITE.value)
    #print title
    draw_page_title(Names.SETUP.value)
    #print next button
    draw_button(next_button)
    #print text
    cards = tree.get_cards()
    nr = len(cards)
    text = str(nr) + Names.SETUP_TEXT.value
    draw_line(text,Positions.WORKING_BOARD.value)
    #print loaded cards: up to 28 to fit in the page
    if nr <= Display.LINES.value -1:
        for i in range(0,nr):
            pos = (Positions.TEXT.value[0],
               Positions.TEXT.value[1] + 2*(i+1)*Sizes.MARGINS.value)
            draw_line(cards[i], pos)
    else:
        for i in range(0,Display.LINES.value -1):
            pos = (Positions.TEXT.value[0],
               Positions.TEXT.value[1] + 2*(i+1)*Sizes.MARGINS.value)
            draw_line(cards[i], pos)
        pos = (Positions.TEXT.value[0],
               Positions.TEXT.value[1] + 2*Display.LINES.value*Sizes.MARGINS.value)
        draw_line("...", pos)
    pygame.display.update()

#START
def draw_start():
    screen.fill(Colors.BLACK.value)
    #print start button
    draw_button(start_button)
    pygame.display.update()

#EXPERIMENT   
#also considers the state of the working board when printing the experiment page
def draw_experiment(tree_update, selection_update, board_state_update, subcategory_update, page_update):    
    #update variables according to current values from the model
    global tree
    global selection
    global board_state
    global subcategory
    global page
    tree = tree_update
    selection = selection_update
    board_state = board_state_update
    subcategory = subcategory_update
    page = page_update
    
    #draw page
    screen.fill(Colors.WHITE.value)
    #print title
    draw_page_title(Names.EXPERIMENT.value)    
    #print help button
    draw_button(help_button)
   
    #print navigation buttons according to the working board state
    if board_state != BoardStates.EDITING:
        #print back button       
        if subcategory:
            draw_button(back_button)           
        #print next button
        elif board_state == BoardStates.FINAL:
            draw_button(next_button)
    
    global categories_buttons, cards_buttons
    categories_buttons = []
    cards_buttons = []
    #print unsorted cards
    draw_unsorted()
    #print sorted cards
    draw_sorted()
    #print navigation arrows
    draw_arrows()
    pygame.display.update()
  
#print unsorted category and cards
def draw_unsorted():
    #print unsorted category tab
    name = Names.UNSORTED_CATEGORY.value + " " + str(len(tree.get_unsorted())) + "/" + str(len(tree.get_cards()))
    global unsorted_category
    unsorted_category = UI_objects.CategoryButton(tree, name,
                                   Positions.UNSORTED_CATEGORY.value)
    draw_button(unsorted_category)
    #print one card to be sorted
    unsorted_cards = tree.get_unsorted()
    draw_cards(unsorted_cards[:Display.UNSORTED.value],unsorted_category)
    
#print sorted categories and cards  
def draw_sorted():
    data_categories = tree.get_children()
    offset = page*Display.CATEGORIES.value
    length = min(offset + Display.CATEGORIES.value, len(data_categories))
    for i in range (offset,length):
        #print category tab
        p = i - offset
        pos = (Positions.SORTED_CATEGORIES.value[0] + p*(Sizes.CATEGORY.value[0]+Sizes.SPACING.value*Sizes.MARGINS.value),
               Positions.SORTED_CATEGORIES.value[1])     
        name = data_categories[i].get_name()
        #add symbol that signifies a tab is clickable
        if board_state == BoardStates.FINAL:
            name = name + Names.OPEN.value    
        sorted_category = UI_objects.CategoryButton(data_categories[i],name,pos)
        categories_buttons.append(sorted_category)
        draw_button(sorted_category)
        #print cards
        sorted_cards = data_categories[i].get_cards()
        draw_cards(sorted_cards[:Display.SORTED.value],sorted_category)
    #at the end of this loop the data_categories from the model and sorted_categories from this module should be mapped 1 to 1

#print cards in a category
def draw_cards(category_cards, category_button):
    length = len(category_cards)
    for i in range(0,length):
        rect = category_button.get_rect()
        left = rect.centerx - Sizes.CARD.value[0]/2
        top = rect.top + rect.height + Sizes.MARGINS.value + i*(Sizes.CARD.value[1] + Sizes.MARGINS.value)
        data = category_button.get_data()
        card_button = UI_objects.CardButton(data,category_cards[i], (left,top))
        cards_buttons.append(card_button)
        #print selection 
        if category_cards[i] == selection:
            draw_selection(card_button)
        draw_button(card_button) 

#print selection
def draw_selection(button):
    #add a border to the selected button
    rect = button.get_rect()
    left = rect.left - 2
    top = rect.top - 2
    width = rect.width + 4
    height = rect.height + 4
    border = pygame.Rect(left, top, width, height)
    pygame.draw.rect(screen, Colors.BLACK.value, border)

#print navigation arrows
def draw_arrows():
    #print left arrow
    if page > 0:
        draw_button(left_arrow)
    #print right arrow
    nr_categories = len(tree.get_children())
    displayed_cat = (page +1)*Display.CATEGORIES.value
    if nr_categories > displayed_cat:
        draw_button(right_arrow)

#INSTRUCTIONS        
def draw_instructions():
    #draw page
    screen.fill(Colors.WHITE.value)
    draw_page_title(Names.INSTRUCTIONS.value)
    #print back button
    draw_button(back_button)
    #print content: up to 30 lines to fit in the screen
    pos = Positions.TEXT.value
    draw_multiple_lines(instructions, pos)
    pygame.display.update()

#FINISH                       
def draw_finish():
    screen.fill(Colors.BLACK.value)
    #print finihs button
    draw_button(finish_button)
    #print back button
    draw_button(back_button)
    pygame.display.update()

#RESULTS
def draw_results():
    #draw page
    screen.fill(Colors.WHITE.value)
    draw_page_title(Names.RESULTS.value)
    #print content
    draw_multiple_lines(Names.RESULTS_TEXT.value, Positions.TEXT.value)
    #print next button
    draw_button(next_button)
    pygame.display.update()

#END    
def draw_end():
    screen.fill(Colors.BLACK.value)
    draw_big_title(Names.END.value, "")
    pygame.display.update()

#helper functions
def draw_multiple_lines(lines, position):
    length = min(Display.LINES.value, len(lines))
    for i in range(0,length):
        pos = (position[0],
               position[1] + 2*i*Sizes.MARGINS.value)
        draw_line(lines[i],pos)
    
def draw_page_title(text):
    f = pygame.font.Font(None, Fonts.PAGE_TITLE.value)
    font = f.render(text, True, Colors.BLACK.value)
    font_rect = font.get_rect()
    font_rect.left = Positions.PAGE_TITLE.value[0]
    font_rect.top = Positions.PAGE_TITLE.value[1]
    screen.blit(font,font_rect)
    
def draw_line(text, pos):
    f = pygame.font.Font(None, Fonts.TEXT.value)
    font = f.render(text, True, Colors.BLACK.value)
    font_rect = font.get_rect()
    font_rect.left = pos[0]
    font_rect.top = pos[1]
    screen.blit(font,font_rect)
        
def draw_button(button):
    col = button.get_color()
    rect = button.get_rect()
    font = button.get_font()
    pygame.draw.rect(screen, col, rect)
    font_rect = font.get_rect(center=rect.center)
    screen.blit(font,font_rect)
    
def draw_big_title(title,subtitle):
    #print title
    f = pygame.font.Font(None,Fonts.BIG_BUTTON.value)
    font = f.render(title, True, Colors.WHITE.value)
    font_rect = font.get_rect(center = Positions.SCREEN_CENTER.value)
    screen.blit(font,font_rect)
    #print subtitle
    f_1= f = pygame.font.Font(None,Fonts.PAGE_TITLE.value)
    font_1 = f_1.render(subtitle, True, Colors.WHITE.value)
    font_rect_1 = font_1.get_rect()
    font_rect_1.left =  font_rect.center[0] - (font_rect_1.width/2)
    font_rect_1.top = font_rect.bottom + 2*Sizes.MARGINS.value
    screen.blit(font_1,font_rect_1)
    
