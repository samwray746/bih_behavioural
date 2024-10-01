from psychopy import core

def experimental_variables(win):
    experiment_clock = core.MonotonicClock() # the main clock used in the experiment 
    countdown = core.CountdownTimer()
    
    fr = win.getActualFrameRate() # getting frame rate of the monitor 
    one_frame = 1/fr

    blocks_per_condition = 7
    total_blocks = blocks_per_condition*3
    trials_per_block = 40 
  
    iti = [1.5, 1.6, 1.7, 1.8, 1.9, 2.0, 2.1, 2.2, 2.3, 2.4, 2.5] # inter-trial interval
    isi = 0.5
    stim_pres = 0.5

    return experiment_clock, countdown, fr, one_frame, blocks_per_condition, total_blocks, trials_per_block, iti, isi, stim_pres
  

  
  
