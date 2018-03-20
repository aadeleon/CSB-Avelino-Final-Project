print(
      
"""
      
Hi Stefano,

This straightforward program is meant to automate the analysis of In-Cell Western (ICW)
assays in my lab and to very quickly visualize the acquired data before variance analysis.

Instructions:
    
    (1) Run this .py file to define/load modules, functions, and variables
        * if you are reading this you may have already done so!
    (2) Run the "plot_data" function with the appropriate arguments:
        - the first argument is the file name/path of the .csv
        - the second argument is the dictionary "well_values"
            * well_values can be modified as per experimental parameters
    (3) Visualize data
    
Notes:
    
    (1) The .csv files are produced by Image Studio connected to a near-IR imager (Li-Cor).
    (2) Sample types ("Sample", "Background", "None") are set using the Image Studio GUI.
    (3) Programmed using Spyder IDE

Thank you for teaching this course!

Best,
Avelino

"""

)
    
import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as pyplot

# this dictionary represents default values
# keys correspond to the columns of a 96-well plate
# each column (given by well/column number) contains replicate samples
# values are variable insulin concentrations, modified as needed for experiments
well_values = {'01': 0.0, '02': 0.1, '03': 0.25, 
               '04': 0.50, '05': 0.75, '06': 1.0,
               '07': 2.0, '08': 3.0, '09': 4.0,
               '10': 5.0, '11': 10.0, '12': 20.0}

# this function extracts the data from the .csv file produced by Image Studio
# it only extracts from one column of the plate
def extract_data(file_name, well_num):
    values = {}
    with open(file_name) as f:
        reader = csv.DictReader(f)
        for row in reader:
            channel = row["Channel"]
            sample_type = row["ICW Type"]
            # make sure that only "Sample" or "Background" types are extracted
            if sample_type == "None":
                continue
            total = float(row["Total"])
            # each sample has two measurements (2 laser channels)
            # adds each replicate of given column to a "sample" or "background" list
            if well_num in row["Well Name"]:
                values[channel] = values.get(channel, {})
                values[channel][sample_type] = values[channel].get(sample_type, [])
                values[channel][sample_type].append(total)
    # in the rare case that "Background" samples were not run
    if "Background" not in values[channel]: 
        mean_700 = np.mean(values["700"]["Sample"])
        mean_800 = np.mean(values["800"]["Sample"])
    else: #subtract background mean from sample mean for each channel
        mean_700 = (np.mean(values["700"]["Sample"]) -
                    np.mean(values["700"]["Background"]))
        mean_800 = (np.mean(values["800"]["Sample"]) - 
                    np.mean(values["800"]["Background"]))
    # standard deviation of replicates
    std_700 = np.std(values["700"]["Sample"])
    std_800 = np.std(values["800"]["Sample"])
    ins_conc = well_values[well_num]
    # output is a list containing:
        # insulin concentration of the replicate group (column),
        # the ratio of 700 channel to 800 channel (normalization),
        # and error propagation
    return([ins_conc, mean_700/mean_800, (std_700 / mean_700) + (std_800 / mean_800)])

# this function runs the extract_data function for each column of the plate
# each column is given by the well number (i.e. the keys of well_values above)
def organize_data(file_name, well_num):
    clean_data = {}
    for well_num in well_values.keys():
        # unused wells will generate KeyError
        # the try-except KeyError statement allows the for loop to ignore unused wells
        try:
            raw_data = extract_data(file_name, well_num)
            clean_data["Ins_Conc"] = clean_data.get("Ins_Conc", [])
            clean_data["Ins_Conc"].append(raw_data[0])
            clean_data["Ratio"] = clean_data.get("Ratio", [])
            clean_data["Ratio"].append(raw_data[1])
            clean_data["Std"] = clean_data.get("Std", [])
            clean_data["Std"].append(raw_data[2])
        except KeyError:
            continue
    # output is the data organized into a pandas dataframe
    return(pd.DataFrame(clean_data))
    
# finally, this function plots the pandas dataframe produced by the previous function
# this is the only function to run in console since it calls the organize_data function above
def plot_data(file_name, well_num):
    to_plot = organize_data(file_name, well_num)
    pyplot.figure(figsize=(16,9))
    pyplot.title("Insulin Assay", fontsize=28)
    pyplot.xlabel("Insulin Concentration (nM)", fontsize=20)
    pyplot.ylabel("Ratio (pAkt / Akt)", fontsize=20)
    pyplot.errorbar(x=to_plot.Ins_Conc,
                    y=to_plot.Ratio,
                    yerr=to_plot.Std,
                    ecolor='black',
                    marker="o",
                    markersize=12,
                    capsize=10,
                    capthick=1,
                    linestyle="--")
