# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 13:50:59 2020

@author: Alexandra Coroiu
"""
import pygame
from program_invariables import Names,Sizes,ProgramStates, Actions

import event_handler
import painter

#BEGIN   
pygame.init()
screen = pygame.display.set_mode(Sizes.SCREEN.value)
painter.set_screen()
pygame.display.set_caption(Names.EXPERIMENT.value)
state = ProgramStates.BEGIN
on = True


#CARD SORTING
while on:
    #automatic transitions
    #before experiment - happens only once
    if state == ProgramStates.BEGIN:
        #print welcome screen
        state = ProgramStates.SETUP
    if state == ProgramStates.SETUP:
        #prepae input
        event_handler.handle_setup()
        state = ProgramStates.START  
    
    #event handler - data updates loop
    for event in pygame.event.get():  
        #end program
        if event.type == pygame.QUIT:
            state = ProgramStates.END           
        #check click on buttons and change state accordingly   
        if state == ProgramStates.START:
            action = event_handler.handle_start(event)
            if action == Actions.NEXT:
                state = ProgramStates.EXPERIMENT
                
        elif state == ProgramStates.EXPERIMENT:
            #prepare board
            action = event_handler.handle_experiment(event)
            #check finish
            if action == Actions.NEXT:
                state = ProgramStates.FINISH
            #check help
            elif action == Actions.HELP:
                state = ProgramStates.INSTRUCTIONS
            #check other actions
        elif state == ProgramStates.INSTRUCTIONS:
            action = event_handler.handle_instructions(event)
            if action == Actions.BACK:
                state = ProgramStates.EXPERIMENT
                
        elif state == ProgramStates.FINISH:
            #save results
            action = event_handler.handle_finish(event)
            if action == Actions.NEXT:
                state = ProgramStates.RESULTS
                
    #automatic transitions  
    #after experiment
    if state == ProgramStates.RESULTS:
        event_handler.handle_results()
        state = ProgramStates.END
    if state == ProgramStates.END:
        on = False
               
    #visuals  
    #start page
    if state == ProgramStates.START:
        painter.draw_start()
    #experiment page
    if state == ProgramStates.EXPERIMENT:
        #always draw according to up to date tree
        painter.draw_experiment(event_handler.tree, 
                                event_handler.selected, 
                                event_handler.finished,
                                event_handler.subcategory)
    #help page
    if state == ProgramStates.INSTRUCTIONS:
        painter.draw_instructions()
    #finish page
    if state == ProgramStates.FINISH:
        painter.draw_finish()
   
#END
pygame.quit()
  
