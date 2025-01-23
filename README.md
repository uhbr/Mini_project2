# Mini_project2

Hi! This is my project :)

# *ERP Data Analysis for Finger Movements*
  This project is focused on analyzing brain data (ECoG) to compute the Event-Related Potentials (ERPs) for finger movements. It takes trial points from a CSV file, extracts the relevant ECoG signal segments        around each movement, and computes the average ERP for each finger.

## Project Structure
  Main.py: The Python script that contains the logic to read the trial data, process the ECoG signal, and compute the mean ERP for each finger.
  mini_project_2_data: Folder containing the required data files.
  events_file_ordered.csv: CSV file containing the trial information (start time, peak time, and finger identifier).
  brain_data_channel_one.csv: CSV file containing the ECoG signal data.

## Dependencies
  ### To run this project, you'll need the following Python libraries:
  
  pandas
  numpy
  
  ### You can install the necessary dependencies using pip:
  
    pip install pandas numpy

## Description of the Functionality
  Function: calc_mean_erp(trial_points, ecog_data)
  This function computes the mean ERP for each finger based on the trial data and ecog signal.

  ### Input:
  
  trial_points: A CSV file containing trial information. It has three columns:
  start: The starting point of the finger movement (in ms).
  peak: The peak point of the movement (in ms).
  finger: An integer representing the finger number (1-5).
  ecog_data: A CSV file containing ECoG signal time-series data. This signal is recorded around the time of each movement.
  
  ### Output:
  
  A 5x1201 matrix (fingers_erp_mean), where:
  Each row corresponds to a finger (1 through 5).
  Each column represents a time point around the movement (from -200 ms before the start to +1000 ms after the start).
