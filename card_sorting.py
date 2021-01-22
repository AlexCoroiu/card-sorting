# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 13:50:59 2020

@author: Alexandra Coroiu

This is the main file used to run the Card Sorting program. 
This module uses the painter and event handler to interact with the user.

"""
import pygame
from program_invariables import Names,Sizes,ProgramStates, Actions

import event_handler
import painter

import time

#Initialize the program
#BEGGIN
pygame.init()
screen = pygame.display.set_mode(Sizes.SCREEN.value)
painter.set_screen()
pygame.display.set_caption(Names.EXPERIMENT.value)
state = ProgramStates.BEGIN
on = True

#The main program loop used to interact with the user 
#It prints and listens for user input
while on:
    
    #automatic transition at the beggining of the program
    if state == ProgramStates.BEGIN:
        #print welcome screen
        painter.draw_begin()
        time.sleep(5)
        #load input
        event_handler.handle_begin()
        state = ProgramStates.SETUP
    
    #loop that deals with user input in the form of pygame events
    #It updates the program state accordingly
    for event in pygame.event.get():  
        #user ends program by clicking on the X button of the program window
        if event.type == pygame.QUIT:
            on = False     
        #check all the other types of events for each program state
        #use the event handler to interpret user actions
        else: 
            #SETUP
            if state == ProgramStates.SETUP:
                action = event_handler.handle_setup(event)
                #check next
                if action == Actions.NEXT:
                    state = ProgramStates.START 
            #START
            elif state == ProgramStates.START:
                action = event_handler.handle_start(event)
                #check next
                if action == Actions.NEXT:
                    state = ProgramStates.EXPERIMENT    
            #EXPERIMENT
            elif state == ProgramStates.EXPERIMENT:
                action = event_handler.handle_experiment(event)
                #check finish
                if action == Actions.NEXT:
                    state = ProgramStates.FINISH
                #check help
                elif action == Actions.HELP:
                    state = ProgramStates.INSTRUCTIONS
            #INSTRUCTIONS
            elif state == ProgramStates.INSTRUCTIONS:
                action = event_handler.handle_instructions(event)
                #check back
                if action == Actions.BACK:
                    state = ProgramStates.EXPERIMENT     
            #FINISH
            elif state == ProgramStates.FINISH:
                action = event_handler.handle_finish(event)
                #check next
                if action == Actions.NEXT:
                    state = ProgramStates.RESULTS
                #check next
                elif action == Actions.BACK:
                    state = ProgramStates.EXPERIMENT
            #RESULTS        
            elif state == ProgramStates.RESULTS:
                action = event_handler.handle_results(event)
                #check next
                if action == Actions.NEXT:
                    state = ProgramStates.END
                            
    #printing visuals for each non-automatic program state 
    #SETUP
    if state == ProgramStates.SETUP:
        painter.draw_setup(event_handler.tree)
    #START
    if state == ProgramStates.START:
        painter.draw_start()
    #EXPERIMENT
    if state == ProgramStates.EXPERIMENT:
        #always draw according to up to date tree and other viariables
        painter.draw_experiment(event_handler.tree, 
                                event_handler.selection, 
                                event_handler.board_state,
                                event_handler.subcategory,
                                event_handler.page)
    #INSTRUCTIONS
    if state == ProgramStates.INSTRUCTIONS:
        painter.draw_instructions()
    #FINISH
    if state == ProgramStates.FINISH:
        painter.draw_finish()
    #RESULTS
    if state == ProgramStates.RESULTS:
        painter.draw_results()
        
    #automatic transition at the end of the program
    if state == ProgramStates.END:
        #save results
        event_handler.handle_end()
        #print good bye screen
        painter.draw_end()
        time.sleep(5)
        on = False
           
#END
pygame.quit()
  
