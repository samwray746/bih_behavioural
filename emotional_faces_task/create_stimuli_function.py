import psychopy

def create_stimuli(win):
  
   ## Function needs to be written - remove comment when done ##
   instruction_one_str = "Welcome to this part of the experiment! Click the space bar to continue."
   instruction_two_str = "In this experiment, you will be shown different faces. Please pay attention to the faces"
   instruction_three_str = "Every few trials, you will see an arrow pointin either left or right. Please indicate which way the arrow is pointing by pressing the arrrow buttons."
   instruction_four_str = "If you have any questions, please ask the researcher before continuing. Click the space bar to start the experiment."

   instructions_one = psychopy.visual.TextStim(win, text = instruction_one_str, height = 0.80)
   instructions_two = psychopy.visual.TextStim(win, text = instruction_two_str, height = 0.80)
   instructions_three = psychopy.visual.TextStim(win, text = instruction_three_str, height = 0.80)
   instructions_four = psychopy.visual.TextStim(win, text = instruction_four_str, height = 0.80)

   # Fixation cross 
   # Images - path to where the images will be saved
   # left and right arrow 



