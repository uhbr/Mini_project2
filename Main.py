import pandas as pd
import numpy as np
# import matplotlib.pyplot as plt

# Paths to the data
trial_points = "mini_project_2_data/events_file_ordered.csv"
ecog_data = "mini_project_2_data/brain_data_channel_one.csv"

# In this project we'll take 2 data files - 1 of brain data and 1 of events. We want to understand the brain signal that came before and after the movement.
# To do so, I'll write a function that will calculate the ERP.

def calc_mean_erp(trial_points, ecog_data):
    '''This function will define every finger movement as a block of time that is 200 ms before the starting point of the movement, 1 ms of the starting point, and 1000 ms after the starting point of the movement. Such that each finger movement will extract 1201 indices of brain data that relate to the movement of that finger
    Gather all the signals for each event and average across them such that there is a list of averaged brain signals of length 1201 for each unique finger movement. 
    For example – let’s say the patient was asked to move finger 1 one hundred times (100 trials), there are now 100 samples of a block of time in brain data of length 1201. Average across the 100 trials such that we only end up with 1 list of length 1201 for that finger.
    This function will plot the averaged brain response for each finger
    This function will return a matrix with the averaged brain response list for each finger – matrix size will be 5x1201 – five finger events, and the length of brain data for each event – 1201 – order by finger – finger 1 should be the first row.
    '''
    # Reading the files
    trial_points = pd.read_csv(trial_points).copy().astype(int)  #Assuming that all the data in the file is Float or Int. I'm copying it because I have the tendency to ruin files accidently
    ecog_data = pd.read_csv(ecog_data).copy()
    trial_points.columns = ["start", "peak", "finger"]  #Naming the file's column so it will be easier for me to work on each of them
    
    # Creating a numpy array of 5X1201
    fingers_erp_mean = np.zeros((5,1201))

    # Calculating the ERP mean for each finger
    for finger in range(1, 6): #For each finger out of 5 fingers
        finger_trials = trial_points[trial_points["finger"] == finger] #Looking only at this specific finger (The one from the line above)

        # creating empty list so later I'd be able to update it with the data
        finger_erp_list = []
        for _, trial in finger_trials.iterrows(): #For a specific trial, looping through the rows of finger_trials
            trial_start = int(trial['start'] - 200)  # 200 ms before the trial's start
            trial_end = int(trial['start'] + 1000)  # 1000 ms after the trial's start

            ecog_segment = ecog_data[trial_start:trial_end+1]  #a segment of ecog is from the starting point (defined above) to the ending poing (included)
            finger_erp_list.append(ecog_segment)  #Appending the empty list with the segment 
            
    
    
        fingers_erp_mean[finger - 1, :] = np.mean(finger_erp_list, axis=0).flatten()  #Selecting a row, : so it'd take all the columns needed,
        # calculating the mean of all the ERP segments of the finger along the row, Flattening it because otherwise it can't broadcast input array 

    
    return fingers_erp_mean


fingers_erp_mean = calc_mean_erp(trial_points, ecog_data)

# Checking visualy that I got results that makes sense
# for finger in range(1, 6):
#     plt.plot(fingers_erp_mean[finger - 1, :], label=f"Finger {finger}")

# plt.title('Averaged ERP for Each Finger')
# plt.xlabel('Time (ms)')
# plt.ylabel('Amplitude')
# plt.legend()
# plt.show()

