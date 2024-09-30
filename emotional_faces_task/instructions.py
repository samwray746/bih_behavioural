import psychopy
from psychopy import event

def instructions(win, instructions_one, instructions_two, instructions_three, instructions_four, instructions_five):
    training_instructions_one.draw()
    win.flip()
    event.waitKeys(keyList=['space'])
    win.flip()
    training_instructions_two.draw()
    win.flip()
    event.waitKeys(keyList=['space'])
    win.flip()
    training_instructions_three.draw()
    win.flip()
    event.waitKeys(keyList=['space'])
    win.flip()
    training_instructions_four.draw()
    win.flip()
    event.waitKeys(keyList=['space'])
    win.flip()
    training_instructions_five.draw()
    win.flip()
   
