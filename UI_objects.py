# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 16:38:21 2020

@author: Alexandra Coroiu

This module defines the clickable elements of a page. 

"""
import pygame
from program_invariables import Colors, Positions, Sizes, Fonts

pygame.font.init()

#button class
class Button(object):
    def __init__(self, text, pos, size, color, font_size, font_col):
        self.text = text
        rect = pygame.Rect(pos,size)
        self.rect = rect
        self.color = color
        f = pygame.font.Font(None,font_size)
        self.font = f.render(text, True, font_col)
    
    def get_color(self):
        return self.color
    
    def get_rect(self):
        return self.rect
    
    def get_text(self):
        return self.text
    
    def get_font(self):
        return self.font

#button subclasses

#big button at the middle of the page   
#predefined values except text                
class BigButton(Button):
    def __init__(self, text):
        super().__init__(text,
                         Positions.BIG_BUTTON.value, 
                         Sizes.BIG_BUTTON.value,
                         Colors.DARK_GREY.value,
                         Fonts.BIG_BUTTON.value, 
                         Colors.WHITE.value)

#small button 
#predefined values, except text and position
class SmallButton(Button):
    def __init__(self, text, pos):
        super().__init__(text, pos,
                         Sizes.SMALL_BUTTON.value,
                         Colors.DARK_GREY.value,
                         Fonts.SMALL_BUTTON.value,
                         Colors.BLACK.value)

#category button
#predefined values, except text, position and data
class CategoryButton(Button):
    def __init__(self, data, text, pos):
        super().__init__(text, pos,
                         Sizes.CATEGORY.value,
                         Colors.DARK_GREY.value,
                         Fonts.CATEGORY.value,
                         Colors.BLACK.value)
        #also stored the category object associated with the category button
        self.data = data
    def get_data(self):
        return self.data

#category button
#predefined values, except text, position and data
class CardButton(Button):
    def __init__(self,data, text, pos):
        super().__init__(text, pos,
                         Sizes.CARD.value,
                         Colors.LIGHT_GREY.value,
                         Fonts.CARD.value,
                         Colors.BLACK.value)
        #also stored the category object associated with the card button
        #the category refers to the one that the card belongs to
        self.data = data
    def get_data(self):
        return self.data

#arrow navigation buttons
#predefined values, except text and position
class Arrow(Button):
    def __init__(self, text, pos):
        super().__init__(text, pos,
                         Sizes.ARROW.value,
                         Colors.WHITE.value,
                         Fonts.CARD.value,
                         Colors.BLACK.value)




