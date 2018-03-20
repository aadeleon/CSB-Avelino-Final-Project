# CSB Avelino Final Project

This straightforward program is meant to automate the analysis of In-Cell Western (ICW)
assays in my lab and to very quickly visualize the acquired data before variance analysis.
Preliminary analysis is typically performed using Excel. The assay is performed at least
a couple times a week, so this program will surely save time in the long run as the assay
continues to be optimized for multiple conditions.

While this particular program was written for the analysis of insulin assays in cultured cells,
the code and its variables can easily be modified as per the necessary experimental conditions.

Overview:

The program begins by extracting the desired data from the relevant .csv file.

Then, the data is organized before finally being plotted with error bars.

Instructions:
    
    (1) Run Final_Project_Avelino.py file to define/load modules, functions, and variables
    (2) Run the "plot_data" function with the appropriate arguments:
        - the first argument is the file name/path of the .csv
        - the second argument is the variable "well_values" defined upon running the .py file
            * well_values can be modified as per experimental parameters
    (3) Visualize data
    
Notes:
    
    - The .csv files are produced by Image Studio connected to a near-IR imager (Li-Cor).
    - There are 3 .csv files included as examples
    - Sample types ("Sample", "Background", "None") are set using the Image Studio GUI.
    - Programmed using Spyder IDE
