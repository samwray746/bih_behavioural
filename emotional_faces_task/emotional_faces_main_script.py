# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 10:45:02 2024

@author: bsms9zh8
"""


# This is the main script for a task investigating repetition suppression of the heartbeat-evoked potential. Some key details: 
    
# - Stimuli will be ontained from the NimStim dataset of face stimuli. Faces either show disgust (D), or are neutral (N)

# - There will be 21 experimental blocks, with each block consisting of 40 trials (40 being the number of actors in the NimStim dataset)
# - In each trial, the same identity face will be presented for 500ms, interspersed with a 500ms fixation cross
# - During a repetition trial, face presentations are identical (D-D or N-N)
# - During an alternation trial, the face presentations are non-identical (D-N or N-D)

# - Trials are presented in three stimulus contexts, which each occur in 7 blocks: 1) Cue-useful blocks 2) Cue-sometimes useful blocks 3) Cue-useless blocks 
# - During a cue-useful block, whenever the fixation cross is red/green/yellow (i.e., non-white), a repetition trial ALWAYS occurs
# - During a cue-sometimes useful block, the non-white fixation cross predicts a repetition trial with 75% accuracy 
# - During a cue-useless block, the non-white fixation cross predicts a repetition trial with 50% accuracy (i.e., chance)

# - In 20% of all trials, arrows apppear overlaying the faces, necessitating a which-direction response to maintain and check for attention

 
### IMPORTS ### 
import psychopy
import os.path as op
from psychopy import event, visual, gui, core

from experimental_variables_function import experimental_variables # importing function that creates the main variables for the experiment 

### GATHERING PARTICIPANT INFO ### 

participant_info = {'Subject ID': '', 'Age': '',
                    'Order': '', 'Random seed': ''} # dictionary specifying participant info 

myDlg = gui.DlgFromDict(participant_info, title="Emotional faces experiment") # creating the dialogue box object 

if not myDlg.OK:
    core.quit()
    
## Converting participant info to appropriate data-types ##     
order = int(participant_info['Order']) # Following Marshall & Schutz-Bosach 2017, we want to present the different experimental blocks as a unit. So we have 6 different 'orders',
# corresponding to the 6 permutations of presentation (i.e., ABC, ACB, BCA, BAC, CAB, CBA)
subject_id = str(participant_info['Subject ID'])
random_seed = int(participant_info['Random seed'])
age = str(participant_info['Age'])

### CREATING THE WIN OBJECT ### 

win = visual.Window(color = '#000000', fullscr = True, monitor="testMonitor", units="pix") # Will need to change units to 'degree' when we know distance from monitor 
win.mouseVisible = False

### FUNCTION TO CREATE SOME STIMULI ### 

# Note: n_1 and d_1 correspond to objects of the neutral and disgust image of 'actor 1', and so on with n_2, d_2...etc. 
n_1, d_1, n_2, d_2, n_3, d_3, n_4, d_4, n_5, d_5, n_6, d_6, n_7, d_7, n_8, d_8, n_9, d_9, n_10, d_10, n_11, d_11, n_12, d_12, n_13, d_13, n_14, d_14, n_15, d_15, n_16, d_16, n_17, d_17, n_18, d_18, n_19, d_19, n_20, d_20, n_21, d_21, n_22, d_22, n_23, d_23, n_24, d_24, n_25, d_25, n_26, d_26, n_27, d_27, n_28, d_28, n_29, d_29, n_30, d_30, n_31, d_31, n_32, d_32, n_33, d_33, n_34, d_34, n_35, d_35, n_36, d_36, n_37, d_37, n_38, d_38, n_39, d_39, n_40, d_40, instructions_one, instructions_two, instructions_three, instructions_four, instructions_five, fixation_cross_red, fixation_cross_white, arrow_left, arrow_right = create_stimuli(win)

### INSTRUCTIONS ### 
# Instructions
instruction_one.draw()
win.flip()

instruction_two.draw()
win.flip()

instruction_three.draw()
win.flip()

instruction_four.draw()
win.flip()

## Function needs to be written - remove comment when done ## 
instructions(win, 'all_instruction_variables')

### EXPERIMENTAL BLOCK FUNCTIONS ### 
## Functions need to be written - remove comment when done ## 
if order == 1: # experimental blocks run in order 'cue_useful', 'cue_sometimes_useful', 'cue_useless'
    eb_useful('all_relevant_variables')
    save_experimental_block('all_relevant_variables')

    eb_s_useful('all_relevant_variables')
    save_experimental_block('all_relevant_variables')

    eb_useless('all_relevant_variables')
    save_experimental_block('all_relevant_variables')

if order == 2: # experimental blocks run in order 'cue_useful', 'cue_useless', 'cue_sometimes_useful' 
    eb_useful('all_relevant_variables')
    save_experimental_block('all_relevant_variables')

    eb_useless('all_relevant_variables')
    save_experimental_block('all_relevant_variables')

    eb_s_useful('all_relevant_variables')
    save_experimental_block('all_relevant_variables')

if order == 3: # experimental blocks run in order 'cue_sometimes_useful', 'cue_useless', 'cue_useful'
    eb_s_useful('all_relevant_variables')
    save_experimental_block('all_relevant_variables')

    eb_s_useless('all_relevant_variables')
    save_experimental_block('all_relevant_variables')

    eb_useful('all_relevant_variables')
    save_experimental_block('all_relevant_variables')

if order == 4: # experimental blocks run in order 'cue_sometimes_useful','cue_useful', 'cue_useless'
    eb_s_useful('all_relevant_variables')
    save_experimental_block('all_relevant_variables')

    eb_s_useful('all_relevant_variables')
    save_experimental_block('all_relevant_variables')

    eb_useless('all_relevant_variables')
    save_experimental_block('all_relevant_variables')




    
    
    

