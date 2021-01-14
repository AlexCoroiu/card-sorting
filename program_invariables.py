# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 16:46:00 2020

@author: Alexandra Coroiu
"""
from enum import Enum
import pandas

class ProgramStates(Enum):
    BEGIN = 'begin'
    SETUP = 'setup'
    START = 'start'
    EXPERIMENT = 'experiment'
    FINISH = 'finish'
    RESULTS = 'results'
    END = 'end'
    INSTRUCTIONS = 'instructions'

class Actions(Enum):
    NEXT = 'next'
    BACK = 'back'
    ADD = 'add'
    HELP = 'help'

class Names(Enum):
    EXPERIMENT = 'Card Sorting'
    INPUT_FILE = 'cards_file.csv'
    RESULTS_FILE = 'results_file.txt'
    MATRIX_FILE = 'matrix_file.csv'
    START_BUTTON = 'START'
    FINISH_BUTTOn = 'FINISH'
    BACK_BUTTON = '< BACK'
    NEXT_BUTTON = 'NEXT >'
    UNSORTED_CATEGORY = 'Unsorted'
    NEW_CATEGORY = '+ new category'
    INSTRUCTIONS = "Instructions"
    HELP_BUTTON = "HELP !"

class Colors(Enum):
    BLACK = (0, 0, 0)
    DARK_GREY = (128,128,128)
    LIGHT_GREY = (192,192,192)
    WHITE =  (255, 255, 255)

class Sizes(Enum):
    SCREEN = (1280, 720)
    MARGINS = 10
    PAGE_TITLE = 40
    BIG_BUTTON =(500,250)
    SMALL_BUTTON = (75,30)
    CATEGORY = (150,25)
    CARD = (125,50)
    NEW_CATEGORY = ()
    
class Display(Enum):
    LINES = 30
    UNSORTED = 1
    CATEGORIES = 5
    SORTED = 10

class Fonts(Enum):
    BIG_BUTTON = 140
    PAGE_TITLE = 30
    SMALL_BUTTON = 25
    CATEGORY = 20
    CARD = 30
    TEXT = 20

class Positions(Enum):
    SCREEN_CENTER = (Sizes.SCREEN.value[0]/2,Sizes.SCREEN.value[1]/2)
    BIG_BUTTON = (SCREEN_CENTER[0]-(Sizes.BIG_BUTTON.value[0]/2),
                  SCREEN_CENTER[1]-(Sizes.BIG_BUTTON.value[1]/2))
    PAGE_TITLE = (Sizes.MARGINS.value,Sizes.MARGINS.value)
    TEXT = (PAGE_TITLE[0], PAGE_TITLE[1]+Sizes.PAGE_TITLE.value)
    NEXT_BUTTON = (Sizes.SCREEN.value[0]-Sizes.MARGINS.value-Sizes.SMALL_BUTTON.value[0],
                   Sizes.SCREEN.value[1]-Sizes.MARGINS.value-Sizes.SMALL_BUTTON.value[1])
    BACK_BUTTON = (Sizes.MARGINS.value,
                   Sizes.SCREEN.value[1]-Sizes.MARGINS.value-Sizes.SMALL_BUTTON.value[1])
    HELP_BUTTON = (Sizes.SCREEN.value[0]-Sizes.MARGINS.value-Sizes.SMALL_BUTTON.value[0],
                   Sizes.MARGINS.value)
    WORKING_BOARD = (Sizes.MARGINS.value,
                     Sizes.MARGINS.value + Sizes.PAGE_TITLE.value)
    UNSORTED_CATEGORY = WORKING_BOARD
    SORTED_CATEGORIES = (WORKING_BOARD[0] + Sizes.CATEGORY.value[0] + 4*Sizes.MARGINS.value,
                         WORKING_BOARD[1])

#load insructions
file = "instructions.txt"
data_frame = pandas.read_csv(file, sep = "\n", names=['instructions'])
instructions = data_frame.instructions.to_list()
print('instructions loaded')



    

    
