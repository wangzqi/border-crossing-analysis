"""
This program inputs the border crossing records provided by the Bureau of Transportation Statistics. It then calculates 
the total number of times vehicles, equipment, passengers and pedestrians cross the U.S.-Canadian and U.S.-Mexican borders 
each month, and also the running monthly average of total number of crossings for that type of crossing and border.

The input data must have at least the columns Border,Date,Measure,and Value provided.
The columns needs to be separated by comma.
The first line must be the header line. 
An example of the input is as follow:
******************************************************************************************************************
Port Name,State,Port Code,Border,Date,Measure,Value,Location
Derby Line,Vermont,209,US-Canada Border,03/01/2019 12:00:00 AM,Truck Containers Full,6483,POINT (-72.09944 45.005)
Norton,Vermont,211,US-Canada Border,03/01/2019 12:00:00 AM,Trains,19,POINT (-71.79528000000002 45.01)
...
******************************************************************************************************************
"""

import sys
from datetime import datetime

year=0
output_border_crossing_list = []

class output_record(object):
    def __init__(self,input_record_dict):
        self.Border = input_record_dict['Border']
        self.Date = input_record_dict['Date']
        self.Measure = input_record_dict['Measure']
        self.Value = input_record_dict['Value']
        self.Sum = 0
        self.Average = 0


#Record Validation Check
def validate_record(input_record_dict):
    global year
    try:                                                                                #Check the Date & Value valid or not
        input_record_dict['Date']=datetime.strptime(input_record_dict['Date'],'%m/%d/%Y %I:%M:%S %p')
        input_record_dict['Value'] = int(input_record_dict['Value'])
        if year==0:
            year=input_record_dict['Date'].year
        if year!=input_record_dict['Date'].year:                                        #invalidate year
            return False
        if input_record_dict['Value']<0 or input_record_dict['Value']>999999999:        #invalidate values
            return False
        return True
    except ValueError:
        return False


#Add a new record
def add_new_record(input_record_dict,output_border_crossing_list):
    if not output_border_crossing_list:
        output_border_crossing_list.append(output_record(input_record_dict))
    else:
        for line in output_border_crossing_list:
            if(line.Border==input_record_dict['Border'] and line.Measure==input_record_dict['Measure'] and line.Date==input_record_dict['Date']):
                line.Value += input_record_dict['Value']
                return
        output_border_crossing_list.append(output_record(input_record_dict))


#Define the sort key for the output
def sortKey(line):
    return line.Date,line.Border,line.Measure


# Main part starts here
with open(sys.argv[1],'r') as Border_Crossing_Entry_Input:                      # Read in all the records
    for line in Border_Crossing_Entry_Input:
        input_record=line.strip()
        input_record=input_record.split(',')
        if input_record.count('Border')!=0:                                     # If it is a header line
            header = input_record
        else:                                                                   # If it is a record
            try:                                                                # Make sure the header line exist
                header
            except NameError:
                sys.exit('Header line not defined. Please add a header line\n')

        input_record_dict=dict(zip(header,input_record))
        if validate_record(input_record_dict):                                  #For valid record, add it to the output
            add_new_record(input_record_dict,output_border_crossing_list)


if len(output_border_crossing_list)==0:
    print('No valid record found\n')
else:
    output_border_crossing_list.sort(key=sortKey,reverse=True)
    for line in output_border_crossing_list:                                    #loop through to calculate the running monthly average
        for line1 in output_border_crossing_list:
            if(line.Border==line1.Border and line.Measure==line1.Measure and line.Date>line1.Date and line.Date.month>1):
                line.Sum += line1.Value
                line.Average = Decimal(line.Sum/(line.Date.month-1)).to_integral(rounding=ROUND_HALF_UP)  #Use round_half_up to match the python 2 results              
                #line.Average = round(line.Sum/(line.Date.month-1))

    f=open(sys.argv[2],"w+")                                                    #print the output
    f.write('Border,Date,Measure,Value,Average\n')
    for line in output_border_crossing_list:
        f.write(line.Border+","+line.Date.strftime('%m/%d/%Y %I:%M:%S %p')+','+line.Measure+","+str(line.Value)+','+str(line.Average)+'\n')  
    f.close()
