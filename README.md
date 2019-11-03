# Border Crossing Analysis

## Table of Contents
1. [Introduction](README.md#problem)
1. [Problem](README.md#problem)
1. [Input Dataset](README.md#input-dataset)
1. [Expected output](README.md#expected-output)
1. [Questions?](README.md#questions?)

## Introduction
This is the coding challenge project by Insight Data Engineering.

## Problem
```
The Bureau of Transportation Statistics regularly makes available data on the number of vehicles, 
equipment, passengers and pedestrians crossing into the United States by land.

**For this challenge, we want to you to calculate the total number of times vehicles, equipment, passengers 
and pedestrians cross the U.S.-Canadian and U.S.-Mexican borders each month. We also want to know the 
running monthly average of total number of crossings for that type of crossing and border.**
```

## Input Dataset

For this challenge, an input file, `Border_Crossing_Entry_Data.csv`, resides in the top-most `input` directory of the repository.

The file contains data of the form:

```
Port Name,State,Port Code,Border,Date,Measure,Value,Location
Derby Line,Vermont,209,US-Canada Border,03/01/2019 12:00:00 AM,Truck Containers Full,6483,POINT (-72.09944 45.005)
Norton,Vermont,211,US-Canada Border,03/01/2019 12:00:00 AM,Trains,19,POINT (-71.79528000000002 45.01)
Calexico,California,2503,US-Mexico Border,03/01/2019 12:00:00 AM,Pedestrians,346158,POINT (-115.49806000000001 32.67889)
Hidalgo,Texas,2305,US-Mexico Border,02/01/2019 12:00:00 AM,Pedestrians,156891,POINT (-98.26278 26.1)
Frontier,Washington,3020,US-Canada Border,02/01/2019 12:00:00 AM,Truck Containers Empty,1319,POINT (-117.78134000000001 48.910160000000005)
Presidio,Texas,2403,US-Mexico Border,02/01/2019 12:00:00 AM,Pedestrians,15272,POINT (-104.37167 29.56056)
Eagle Pass,Texas,2303,US-Mexico Border,01/01/2019 12:00:00 AM,Pedestrians,56810,POINT (-100.49917 28.70889)
```
See the [notes from the Bureau of Transportation Statistics](https://data.transportation.gov/Research-and-Statistics/Border-Crossing-Entry-Data/keg4-3bc2) for more information on each field.

The input data must have at least the following fields provided.
* `Border`: Designates what border was crossed
* `Date`: Timestamp indicating month and year of crossing
* `Measure`: Indicates means, or type, of crossing being measured (e.g., vehicle, equipment, passenger or pedestrian)
* `Value`: Number of crossings

The columns needs to be separated by comma.
The first line must be the header line. 


## Expected Output
The output file will output
* Sum the total number of crossings (`Value`) of each type of vehicle or equipment, or passengers or pedestrians, that crossed the border that month, regardless of what port was used. 
* Calculate the running monthly average of total crossings, rounded to the nearest whole number, for that combination of `Border` and `Measure`, or means of crossing.

For example, given the above input file, the output file, `report.csv` would be:

```
Border,Date,Measure,Value,Average
US-Mexico Border,03/01/2019 12:00:00 AM,Pedestrians,346158,114487
US-Canada Border,03/01/2019 12:00:00 AM,Truck Containers Full,6483,0
US-Canada Border,03/01/2019 12:00:00 AM,Trains,19,0
US-Mexico Border,02/01/2019 12:00:00 AM,Pedestrians,172163,56810
US-Canada Border,02/01/2019 12:00:00 AM,Truck Containers Empty,1319,0
US-Mexico Border,01/01/2019 12:00:00 AM,Pedestrians,56810,0

```

The lines should be sorted in descending order by 
* `Date`
* `Value` (or number of crossings)
* `Measure`
* `Border`

The column, `Average`, is for the running monthly average of total crossings for that border and means of crossing in all previous months. In this example, to calculate the `Average` for the first line (i.e., running monthly average of total pedestrians crossing the US-Mexico Border in all of the months preceding March), it takes the average sum of total number of US-Mexico pedestrian crossings in February `156,891 + 15,272 = 172,163` and January `56,810`, and round it to the nearest whole number `round(228,973/2) = 114,487`

## Repo directory structure

Here is the repo directory structure:

    ├── README.md
    ├── run.sh
    ├── src
    │   └── border_analytics.py
    ├── input
    │   └── Border_Crossing_Entry_Data.csv
    ├── output
    |   └── report.csv
    ├── insight_testsuite
        └── run_tests.sh
        └── tests
            └── test_1
            |   ├── input
            |   │   └── Border_Crossing_Entry_Data.csv
            |   |__ output
            |   │   └── report.csv
            ├── your-own-test_1
                ├── input
                │   └── Border_Crossing_Entry_Data.csv
                |── output
                    └── report.csv


# Questions?
Email us at wangzqi@gamil.com
