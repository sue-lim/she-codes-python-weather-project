import csv
from datetime import datetime

DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees
        and celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees celcius."
    """
    return f"{temp}{DEGREE_SYBMOL}"


#################### PASSED #################### 

def convert_date(iso_string):
    from datetime import datetime
    original_date = iso_string
    new_date = datetime.strptime(original_date, "%Y-%m-%dT%H:%M:%S%z")
    new_date_string = datetime.strftime(new_date, "%A %d %B %Y")
    return(str(new_date_string))
        
    """Converts and ISO formatted date into a human readable format.
        expected_result = "Wednesday 27 January 2010"
        result = weather.convert_date(date)
    Args:
        iso_string: An ISO date string..
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """
pass

#################### PASSED #################### 
def convert_f_to_c(temp_in_farenheit):
    c = (float(temp_in_farenheit)-32)* 5/9
    return round(c,1)
    # """Converts an temperature from farenheit to celcius.

    # Args:
    #     temp_in_farenheit: float representing a temperature.
    # Returns:
    #     A float representing a temperature in degrees celcius, rounded to 1dp.
    # """
pass

#################### PASSED #################### 
def calculate_mean(weather_data):
    num = 0
    for t in weather_data:
        num = num + float(t)
    avg = num / len(weather_data)
    return (avg)
    # """Calculates the mean value from a list of numbers.
    #  input   temperatures = [49, 57, 56, 55, 53]
    #   output   expected_result = 54
    # Args:
    #     weather_data: a list of numbers.
    # Returns:
    #     A float representing the mean value.
    # """
    
pass

import csv


def load_data_from_csv(csv_file):
    weather_data = [] #define this as a list
    with open(csv_file, 'r') as csv_file:
        reader = csv.reader(csv_file)
        next(reader) #skip the header line
        data = list(reader) #sublist command
        print(data) #row
        for line in data: 
                    
            if line: ##check for if line is not empty then append##
                weather_data.append([line[0],int(line[1]),int(line[2])])
                    
    return weather_data

# """Reads a csv file and stores the data in a list.

#     Args:
#         csv_file: a string representing the file path to a csv file.
#     Returns:
#         A list of lists, where each sublist is a (non-empty) line in the csv file.
#     """
pass



def find_min(weather_data):
    val_idx = min_val_idx = 0
    if weather_data:
        min_val = float(min(weather_data))
        for i in range(len(weather_data)):
            if float(weather_data[i])==min_val:
                min_val_idx = float(weather_data[i])
                val_idx = i
        return(float(min_val_idx), val_idx)
    else:
        return()
pass

def find_max(weather_data):
    val_idx = max_val_idx = 0
    if weather_data:
        max_val = float(max(weather_data))
        for i in range(len(weather_data)):
            if float(weather_data[i])==max_val:
                max_val_idx = float(weather_data[i])
                val_idx = i
        return(float(max_val_idx), val_idx)
    else:
        return()
#     """Calculates the maximum value in a list of numbers.

#     Args:
#         weather_data: A list of numbers.
#     Returns:
#         The maximum value and it's position in the list.
#     """
# pass


# def generate_summary(weather_data):
#     """Outputs a summary for the given weather data.

#     Args:
#         weather_data: A list of lists, where each sublist represents a day of weather data.
#     Returns:
#         A string containing the summary information.
#     """
#     pass


import csv
def generate_daily_summary(weather_data):
    weather_data = []
    with open(csv_file, 'r') as csv_file:
        reader = csv.reader(csv_file)
        next(reader) #skip the header line
        data = list(reader) #sublist command
        print(data) #row
        for line in data: 
                    
            if line: ##check for if line is not empty then append##
                weather_data.append([line[0],int(line[1]),int(line[2])])
                    
    print (weather_data)
    # """Outputs a daily summary for the given weather data.

    # Args:
    #     weather_data: A list of lists, where each sublist represents a day of weather data.
    # Returns:
    #     A string containing the summary information.
    # """
    pass
