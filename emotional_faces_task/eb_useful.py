# Function for the cue-useful experimental block

import random

def eb_useful(win, fch_w, fcv_w, fch_nw, fcv_nw, isi, iti, arrow_left, arrow_right, n_1, d_1, n_2, d_2, n_3, d_3, n_4, d_4, n_5, d_5, n_6, d_6, n_7, d_7, n_8, d_8, n_9, d_9, n_10, d_10, n_11, d_11, n_12, d_12, n_13, d_13, n_14, d_14, n_15, d_15, n_16, d_16, n_17, d_17, n_18, d_18, n_19, d_19, n_20, d_20, n_21, d_21, n_22, d_22, n_23, d_23, n_24, d_24, n_25, d_25, n_26, d_26, n_27, d_27, n_28, d_28, n_29, d_29, n_30, d_30, n_31, d_31, n_32, d_32, n_33, d_33, n_34, d_34, n_35, d_35, n_36, d_36, n_37, d_37, n_38, d_38, n_39, d_39, n_40, d_40):
    condition_record = [] # a record that this is a cue_useful trial
    cue_present = [] # was the cue present this trial? 
    type_of_trial = [] # we know that if the cue is present it will be a repetition trial as this is a cue-useful block, but just adding for consistency 
    stimulus_one = [] # the first stimulus presented in the trial 
    stimulus_two = [] # the second stimulus presented in the trial 
    catch = [] # was the trial a catch trial? 
    arrow_direction = [] # if it was a catch trial, what direction was the arrow pointing? 
    correct_incorrect = [] # was the response on the catch trial correct or incorrect 
    iti = [] # what was the inter-trial interval for the trial? 
    
    # Setting up the structure of the experimental block. Some details: 
        
    # 1) Each block consists of 40 trials i.e., the same number of actors we have in our stimulus set
    # 2) In each block, there are 20 repetition trials and 20 alternation trials
    # 3) In half of the 20 repetition/alternation trials a disgust face will be presented first, and in the other half a neutral face will be presented 
    # 4) In a cue useful block, whenever it's a repetition trial the fixation cross will always be non-white 
    
    
    diff_poss_trials = ['disgust_r', 'disgust_a', 'neutral_r', 'neutral_a']
    
    block_structure = [] 
    
    for trial in range(40): # creating the structure of each experimental block 
        
        if len(diff_poss_trials)== 0:
            diff_poss_trials = ['disgust_r', 'disgust_a', 'neutral_r', 'neutral_a']
        
        
        trial_pick = random.choice(diff_poss_trials)
        diff_poss_trials.remove(trial_pick)
        block_structure.append(trial_pick)
        
    # appending the lists with relevant info 
    for trial in range(40):
        
        condition_record.append('cue_useful')
        if block_structure[trial] == 'disgust_r': #So a repetition trial, and disgust is shown first
            condition_record.append('disgust_r')
            cue_present.append(1)
            type_of_trial.append('r')
            stimulus_one.append('
            
        
    
    
    
    
    
    
    

