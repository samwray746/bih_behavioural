import psychopy
from psychopy import visual, core

def create_stimuli(win):
  
  
  ### INSTRUCTIONS
   instruction_one_str = "Welcome to this part of the experiment! Click the space bar to continue."
   instruction_two_str = "In this experiment, you will be shown different faces. Please pay attention to the faces"
   instruction_three_str = "Every few trials, you will see an arrow pointin either left or right. Please indicate which way the arrow is pointing by pressing the arrrow buttons."
   instruction_four_str = "If you have any questions, please ask the researcher before continuing. Click the space bar to start the experiment."

   instructions_one = psychopy.visual.TextStim(win, text = instruction_one_str, height = 0.80)
   instructions_two = psychopy.visual.TextStim(win, text = instruction_two_str, height = 0.80)
   instructions_three = psychopy.visual.TextStim(win, text = instruction_three_str, height = 0.80)
   instructions_four = psychopy.visual.TextStim(win, text = instruction_four_str, height = 0.80)

   ### Colours ###
  grey = '#808080'
   
  
  ### FIXATION CROSS WHITE 
    horiz_line_fixation_start = [-25, 0]
    horiz_line_fixation_end = [25, 0]

    vert_line_fixation_start = [0, 25]
    vert_line_fixation_end = [0, -25]
     
    fixation_cross_vertical_white = psychopy.visual.Line(
    win=win,
    units="pix",
    lineWidth = 5,
    lineColor=grey)

    fixation_cross_horizontal_white = psychopy.visual.Line(
    win=win,
    units="pix",
    lineWidth = 5,
    lineColor=grey)

    fixation_cross_vertical_white.start = vert_line_fixation_start
    fixation_cross_vertical_white.end = vert_line_fixation_end

    fixation_cross_horizontal_white.start = horiz_line_fixation_start
    fixation_cross_horizontal_white.end = horiz_line_fixation_end

  ### FICATION CROSS RED
    horiz_line_fixation_start = [-25, 0]
    horiz_line_fixation_end = [25, 0]

    vert_line_fixation_start = [0, 25]
    vert_line_fixation_end = [0, -25]
     
    fixation_cross_vertical_red = psychopy.visual.Line(
    win=win,
    units="pix",
    lineWidth = 5,
    lineColor=red)

    fixation_cross_horizontal_red = psychopy.visual.Line(
    win=win,
    units="pix",
    lineWidth = 5,
    lineColor=red)

    fixation_cross_vertical_red.start = vert_line_fixation_start
    fixation_cross_vertical.end = vert_line_fixation_end

    fixation_cross_horizontal_red.start = horiz_line_fixation_start
    fixation_cross_horizontal.end = horiz_line_fixation_end


  ### LEFT POINTING RED ARROW
   arrow_left = visual.TextStim(win, text='<', color='red', height=0.2) # not sure about height?
   arrow_left.draw()
   win.flip()
   core.wait(2) # how long should the arrow show? 
   win.close() # not sure we need to close the window? 

 ### RIGHT POINTING RED ARROW 
   arrow_right = visual.TextStim(win, text='>', color='red', height=0.2) # not sure about height?
   arrow_right.draw()
   win.flip()
   core.wait(2) # how long should the arrow show? 
   win.close() # not sure we need to close the window? 


  ### Images - path to where the images will be saved
###TO BE ADDED 
   
   return instructions_one, instructions_two, instructions_three, instructions_four, arrow_left, arrow_right, fixation_cross_vertical_white, fixation_cross_horizontal_white, fixation_cross_vertical_red, fixation_cross_horizontal_red






