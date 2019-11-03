#!/bin/bash
#
# Use this shell script to compile (if necessary) your code and then execute it. Belw is an example of what might be found in this file if your program was written in Python 3.7

#The input data must have at least the columns Border,Date,Measure,and Value provided.
#The columns needs to be separated by comma.
#The first line must be the header line. 
#An example of the input is as follow:
#******************************************************************************************************************
#Port Name,State,Port Code,Border,Date,Measure,Value,Location
#Derby Line,Vermont,209,US-Canada Border,03/01/2019 12:00:00 AM,Truck Containers Full,6483,POINT (-72.09944 45.005)
#Norton,Vermont,211,US-Canada Border,03/01/2019 12:00:00 AM,Trains,19,POINT (-71.79528000000002 45.01)
#...
#******************************************************************************************************************


python3.7 ./src/border_analytics.py ./input/Border_Crossing_Entry_Data.csv ./output/report.csv
