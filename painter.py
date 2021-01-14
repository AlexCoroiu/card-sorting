# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 19:19:22 2020

@author: Alex
"""

import pygame
import UI_objects
from program_invariables import Colors, Names, Fonts, Positions, Sizes, instructions, Display

screen = None

def set_screen():
    global screen
    screen = pygame.display.get_surface()

#final buttons that do not change
start_button = UI_objects.BigButton(Names.START_BUTTON.value)
finish_button = UI_objects.BigButton(Names.FINISH_BUTTOn.value)
next_button = UI_objects.SmallButton(Names.NEXT_BUTTON.value,
                          Positions.NEXT_BUTTON.value)
back_button = UI_objects.SmallButton(Names.BACK_BUTTON.value,
                          Positions.BACK_BUTTON.value)
help_button = UI_objects.SmallButton(Names.HELP_BUTTON.value,
                                     Positions.HELP_BUTTON.value)
unsorted_category = None
#clinon final buttons, when smth is drawn it will be added to these lists
categories_buttons = []
cards_buttons = []
#buttons contain links to the data_objects, such that when smth is clciked event_handler cna update the data

def draw_start():
    screen.fill(Colors.BLACK.value)
    draw_button(start_button)
    pygame.display.update()
    
def draw_experiment(tree, selected, finished, subcategory):
    screen.fill(Colors.WHITE.value)
    #add title
    draw_page_title(Names.EXPERIMENT.value)
    
    #add help button
    draw_button(help_button)
    
    if finished:
        if subcategory:
            #add back button
            draw_button(back_button)
        else:
            #add next button
            draw_button(next_button)

    
    global categories_buttons, cards_buttons
    categories_buttons = []
    cards_buttons = []
    #add unsorted cards
    draw_unsorted(tree, selected)
    #add sorted categories
    draw_sorted(tree, selected)
    pygame.display.update()
    
#unsorted category and cards
def draw_unsorted(tree, selected):
    name = Names.UNSORTED_CATEGORY.value + " " + str(len(tree.get_unsorted())) + "/" + str(len(tree.get_cards()))
    global unsorted_category
    unsorted_category = UI_objects.CategoryButton(tree, name,
                                   Positions.UNSORTED_CATEGORY.value)
    #unsorted category is always first
    draw_button(unsorted_category)
    #only draws the first card that still needs to be sorted
    unsorted_cards = tree.get_unsorted()
    draw_cards(unsorted_cards[:Display.UNSORTED.value],unsorted_category, selected)
    
#sorted categories and cards  
def draw_sorted(tree, selected):
    data_categories = tree.get_children()
    #establish positions
    length = len(data_categories)
    for i in range (0,length):
        pos = (Positions.SORTED_CATEGORIES.value[0] + i*(Sizes.CATEGORY.value[0]+4*Sizes.MARGINS.value),
               Positions.SORTED_CATEGORIES.value[1])     
        sorted_category = UI_objects.CategoryButton(data_categories[i],data_categories[i].get_name(),pos)
        categories_buttons.append(sorted_category)
        draw_button(sorted_category)
        sorted_cards = data_categories[i].get_cards()
        draw_cards(sorted_cards[:Display.SORTED.value],sorted_category, selected)
        #at the end of this the data_categories and sorted_categories should be mapped 1 to 1

def draw_cards(category_cards, category_button, selected):
    length = len(category_cards)
    for i in range(0,length):
        rect = category_button.get_rect()
        left = rect.centerx - Sizes.CARD.value[0]/2
        top = rect.top + rect.height + Sizes.MARGINS.value + i*(Sizes.CARD.value[1] + Sizes.MARGINS.value)
        data = category_button.get_data()
        card_button = UI_objects.CardButton(data,category_cards[i], (left,top))
        cards_buttons.append(card_button)
        #draw selection 
        if category_cards[i] == selected:
            draw_selection(card_button)
        draw_button(card_button) 

def draw_selection(button):
    rect = button.get_rect()
    left = rect.left - 2
    top = rect.top - 2
    width = rect.width + 4
    height = rect.height + 4
    border = pygame.Rect(left, top, width, height)
    pygame.draw.rect(screen, Colors.BLACK.value, border)

def draw_instructions():
    screen.fill(Colors.WHITE.value)
    draw_page_title(Names.INSTRUCTIONS.value)
    draw_button(back_button)
    #content
    #can only print 30 lines to fit in the screen
    length = min(Display.LINES.value, len(instructions))
    for i in range(0,length):
        pos = (Positions.TEXT.value[0],
               Positions.TEXT.value[1] + 2*i*Sizes.MARGINS.value)
        draw_line(instructions[i],pos)
    pygame.display.update()

                       
def draw_finish():
    screen.fill(Colors.BLACK.value)
    draw_button(finish_button)
    pygame.display.update()

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
