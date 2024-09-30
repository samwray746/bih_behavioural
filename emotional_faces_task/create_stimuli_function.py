import psychopy
from psychopy import visual, core

def create_stimuli(win):
  
  
  ### INSTRUCTIONS ###
   instruction_one_str = "Welcome to the emotional faces task! Press the space bar to continue."
   instruction_two_str = "In each trial of this task, you will be shown two pictures of the same person. Pay attention to the faces."
   instruction_three_str = "Every few trials, an arrow will appear in front of a face.\n\n\n Please indicate which way the arrow is pointing by pressing the left/right arrow keys."
   instructions_four_str = "There are 21 experimental blocks in total, which each contain 40 trials.\n\n\nYou can take a break in-between blocks, then press spacebar to begin the next block."
   instruction_five_str = "If you have any questions, please ask the researcher before continuing.\n\n\n Click the space bar to start the experiment."

   instructions_one = psychopy.visual.TextStim(win, text = instruction_one_str, height = 0.80)
   instructions_two = psychopy.visual.TextStim(win, text = instruction_two_str, height = 0.80)
   instructions_three = psychopy.visual.TextStim(win, text = instruction_three_str, height = 0.80)
   instructions_four = psychopy.visual.TextStim(win, text = instruction_four_str, height = 0.80)
   instructions_five = psychopy.visual.TextStim(win, text = instruction_five_str, height = 0.80)
  
  ### COLOURS ###
   grey = '#808080'
   red = '#FF0000'
   white = '#F0F8FF'
   green = '#008000'
   yellow = '#FFFF00'	

  ### FIXATION CROSS COORDINATES ### 
   horiz_line_fixation_start = [-25, 0]
   horiz_line_fixation_end = [25, 0]

   vert_line_fixation_start = [0, 25]
   vert_line_fixation_end = [0, -25]
   
  ### FIXATION CROSS WHITE ### 
    fixation_cross_vertical_white = psychopy.visual.Line(
    win=win,
    units="pix",
    lineWidth = 5,
    lineColor=white)

    fixation_cross_horizontal_white = psychopy.visual.Line(
    win=win,
    units="pix",
    lineWidth = 5,
    lineColor=white)

    fixation_cross_vertical_white.start = vert_line_fixation_start
    fixation_cross_vertical_white.end = vert_line_fixation_end

    fixation_cross_horizontal_white.start = horiz_line_fixation_start
    fixation_cross_horizontal_white.end = horiz_line_fixation_end

   ### FIXATION CROSS RED ### 
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
    fixation_cross_vertical_red.end = vert_line_fixation_end

    fixation_cross_horizontal_red.start = horiz_line_fixation_start
    fixation_cross_horizontal_red.end = horiz_line_fixation_end

    ### FIXATION CROSS GREEN ### 
    fixation_cross_vertical_green = psychopy.visual.Line(
    win=win,
    units="pix",
    lineWidth = 5,
    lineColor=green)

    fixation_cross_horizontal_green = psychopy.visual.Line(
    win=win,
    units="pix",
    lineWidth = 5,
    lineColor=green)

    fixation_cross_vertical_green.start = vert_line_fixation_start
    fixation_cross_vertical_green.end = vert_line_fixation_end

    fixation_cross_horizontal_green.start = horiz_line_fixation_start
    fixation_cross_horizontal_green.end = horiz_line_fixation_end

    ### FIXATION CROSS YELLOW ###   
    fixation_cross_vertical_yellow = psychopy.visual.Line(
    win=win,
    units="pix",
    lineWidth = 5,
    lineColor=yellow)

    fixation_cross_horizontal_yellow = psychopy.visual.Line(
    win=win,
    units="pix",
    lineWidth = 5,
    lineColor=yellow)

    fixation_cross_vertical_yellow.start = vert_line_fixation_start
    fixation_cross_vertical_yellow.end = vert_line_fixation_end

    fixation_cross_horizontal_yellow.start = horiz_line_fixation_start
    fixation_cross_horizontal_yellow.end = horiz_line_fixation_end

  ### LEFT POINTING RED ARROW
   arrow_left = visual.TextStim(win, text='<', color='red', height=0.2) # not sure about height?

 ### RIGHT POINTING RED ARROW 
   arrow_right = visual.TextStim(win, text='>', color='red', height=0.2) # not sure about height?
 
  ### Images - path to where the images will be saved
   ###TO BE ADDED 
   
   return n_1, d_1, n_2, d_2, n_3, d_3, n_4, d_4, n_5, d_5, n_6, d_6, n_7, d_7, n_8, d_8, n_9, d_9, n_10, d_10, n_11, d_11, n_12, d_12, n_13, d_13, n_14, d_14, n_15, d_15, n_16, d_16, n_17, d_17, n_18, d_18, n_19, d_19, n_20, d_20, n_21, d_21, n_22, d_22, n_23, d_23, n_24, d_24, n_25, d_25, n_26, d_26, n_27, d_27, n_28, d_28, n_29, d_29, n_30, d_30, n_31, d_31, n_32, d_32, n_33, d_33, n_34, d_34, n_35, d_35, n_36, d_36, n_37, d_37, n_38, d_38, n_39, d_39, n_40, d_40, instructions_one, instructions_two, instructions_three, instructions_four, instructions_five, fixation_cross_vertical_white, fixation_cross_horizontal_white, fixation_cross_vertical_red, fixation_cross_horizontal_red, fixation_cross_vertical_green, fixation_cross_horizontal_green, fixation_cross_vertical_yellow, fixation_cross_horizontal_yellow, arrow_left, arrow_right






