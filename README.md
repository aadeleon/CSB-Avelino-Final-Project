# CSB Avelino Final Project

This straightforward program is meant to automate the analysis of In-Cell Western (ICW)
assays in my lab and to very quickly visualize the acquired data before variance analysis.

Instructions:
    
    (1) Run Final_Project_Avelino.py file to define/load modules, functions, and variables
    (2) Run the "plot_data" function with the appropriate arguments:
        - the first argument is the file name/path of the .csv
        - the second argument is the dictionary "well_values"
            * well_values can be modified as per experimental parameters
    (3) Visualize data
    
Notes:
    
    - The .csv files are produced by Image Studio connected to a near-IR imager (Li-Cor).
    - There are 3 .csv files  included
    - Sample types ("Sample", "Background", "None") are set using the Image Studio GUI.
    - Programmed using Spyder IDE
