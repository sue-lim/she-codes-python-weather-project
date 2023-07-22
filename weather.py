import csv
from datetime import datetime
""" import dateime module for manipulatin date & time """
from statistics import mean
""" import statistic module fo rarithmetic mean of data """



""" TEST ONE """

"""Takes a temperature and returns it in string format with the degrees
and celcius symbols.
Args:
temp: A string representing a temperature.
Returns:
A string contain the temperature and "degrees celcius."
"""

DEGREE_SYMBOL = u"\N{DEGREE SIGN}C"
""" conversion of the degree sign """
def format_temperature(temp):

    return f"{temp}{DEGREE_SYMBOL}"


#################### PASSED #################### 

""" TEST TWO """

"""Converts and ISO formatted date into a human readable format.
expected_result = "Wednesday 27 January 2010"
result = weather.convert_date(date)
Args:
iso_string: An ISO date string..
Returns:
A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
"""

def convert_date(iso_string):
    from datetime import datetime
    original_date = iso_string
    new_date = datetime.strptime(original_date, "%Y-%m-%dT%H:%M:%S%z")
    new_date_string = datetime.strftime(new_date, "%A %d %B %Y")
    """ strftime returns a string representing the date, controlled by an explicit format string."""
    """ change the default view a new format """
    return(str(new_date_string))
        
pass

#################### PASSED #################### 

""" TEST THREE """

"""Converts an temperature from farenheit to celcius.
Args:
temp_in_farenheit: float representing a temperature.
Returns:
A float representing a temperature in degrees celcius, rounded to 1dp.
"""

def convert_f_to_c(temp_in_farenheit):
    c = (float(temp_in_farenheit)-32)* 5/9
    """ conversion formular """
    return round(c,1)
    """ rounding the number to a decimal point """
pass

#################### PASSED #################### 

""" TEST FOUR """

"""Calculates the mean value from a list of numbers.
input   temperatures = [49, 57, 56, 55, 53]
output   expected_result = 54
Args:
weather_data: a list of numbers.
Returns:
A float representing the mean value.
"""

def calculate_mean(weather_data):
    num = 0
    for t in weather_data:
        num = num + float(t)
    avg = num / len(weather_data)
    return (avg)

pass

#################### PASSED #################### 

""" TEST FIVE """

"""Reads a csv file and stores the data in a list.
Args:
csv_file: a string representing the file path to a csv file.
Returns:
A list of lists, where each sublist is a (non-empty) line in the csv file.
"""

import csv

def load_data_from_csv(csv_file):
    weather_data = [] # empty list 
    
    with open(csv_file, 'r') as csv_file:
        reader = csv.reader(csv_file)
        next(reader) # skip the header line
        data = list(reader) # sublist command
        # print(data) #row
        for line in data: 
                    
            if line: #check for if line is not empty then append
                #next line adds the csv data to the empty list
                weather_data.append([line[0],int(line[1]),int(line[2])])
                    
    return weather_data

pass

#################### PASSED #################### 

""" TEST SIX """

"""Calculates the minimum value in a list of numbers.
Args:
weather_data: A list of numbers.
Returns:
The minimum value and it's position in the list.
"""

def find_min(weather_data):
    val_idx = min_idx = 0
    # val & min initialised to 0 or makes sure they are both empty and ready to store the coldest temperature and its day.
    if weather_data:
        min_val = float(min(weather_data))
        # looping through to find the minimum value and converting to a float
        for i in range(len(weather_data)):
            # This loop iterates over the indices of the weather_data list using the range() function.
            if float(weather_data[i]) == min_val:
                # For each index i, the code checks if the element at that index (converted to a float) is equal to the min_val. This is done because there could be multiple occurrences of the minimum value in the list.
                min_idx = float(weather_data[i])
                #  If the element at index i is equal to the minimum value, the min_idx variable is updated to the value at that index, converted to a float. This is done to ensure that the value in min_idx is numeric, just like min_val.
                val_idx = i
                # This will keep track of the index of the last occurrence of the minimum value in the weather_data list.
        return(float(min_idx), val_idx)
                # After processing the entire list, the function returns a tuple containing two values: the minimum value (converted to a float) and the index of the last occurrence of that minimum value in the weather_data list.
    else:
        return()
pass

#################### PASSED #################### 

""" TEST SEVEN  """

"""Calculates the maximum value in a list of numbers.
Args:
    weather_data: A list of numbers.
Returns:
    The maximum value and it's position in the list.
"""

def find_max(weather_data):
    val_idx = max_idx = 0
        # val & min initialised to 0 or makes sure they are both empty and ready to store the hottest temperature and its day.
    if weather_data:
        max_val = float(max(weather_data))
        # looping through to find the minimum value and converting to a float
        for i in range(len(weather_data)):
            # This loop iterates over the indices of the weather_data list using the range() function.
            if float(weather_data[i]) == max_val:
            # For each index i, the code checks if the element at that index (converted to a float) is equal to the max_val. This is done because there could be multiple occurrences of the maximum value in the list.
                max_idx = float(weather_data[i])
                #  If the element at index i is equal to the maximum value, the max_idx variable is updated to the value at that index, converted to a float. This is done to ensure that the value in max_idx is numeric, just like max_val.
                val_idx = i
                # This will keep track of the index of the last occurrence of the max value in the weather_data list.
        return(float(max_idx), val_idx)
    else:
        return()

pass

#################### PASSED #################### 

""" TEST EIGHT  """

"""Outputs a daily summary for the given weather data.
Args:
weather_data: A list of lists, where each sublist represents a day of weather data.
Returns:
A string containing the summary information.
"""

"""Example
8 Day Overview
The lowest temperature will be 8.3°C, and will occur on Friday 19 June 2020.
The highest temperature will be 22.2°C, and will occur on Sunday 21 June 2020.
The average low this week is 11.4°C.
The average high this week is 18.8°C.
"""



def generate_summary(weather_data):
    day_count = len(weather_data)
    # This line counts the number of days in the weather_data list and stores the count in the variable day_count.

    min_lst=[]
    max_lst=[]
    # Two empty lists min_lst and max_lst are created to store the minimum and maximum temperatures of each day.

    for col in weather_data:
        # The function then goes through each day's information in the weather_data list:
        # print(item)
        
        min_lst.append(convert_f_to_c(col[1]))
        # a. It converts the Fahrenheit minimum temperature (col[1]) of each day to Celsius and adds it to the min_lst.
        max_lst.append(convert_f_to_c(col[2]))
        # b. It converts the Fahrenheit maximum temperature (col[2]) of each day to Celsius and adds it to the max_lst.
    
        # reference to the min temp list 
        low_temp = find_min(min_lst)
        # Formatted min Temp to inc °C
        formatted_low_temp = format_temperature(low_temp[0])
        # Formatting the min Date to show as this format --> Friday 02 July 2021
        formatted_low_date = convert_date(weather_data[low_temp[1]][0])
        
        # reference to the max temp list 
        hg_temp = find_max(max_lst)
        # Formatted max Temp to inc °C
        formatted_hg_temp = format_temperature(hg_temp[0])
        # Formatting the min Date to show as this format --> Friday 02 July 2021
        formatted_hg_date = convert_date(weather_data[hg_temp[1]][0])
        
        #reference to the low in the mean list 
        avg_low_temp = calculate_mean(min_lst)
        # Formatted Temp to inc °C
        formatted_avg_low_temp = format_temperature(round(avg_low_temp,1))
        
        #reference to the high in the mean list 
        avg_hg_temp = calculate_mean(max_lst)
        # Formatted Temp to inc °C
        formatted_avg_hg_temp = format_temperature(round(avg_hg_temp,1))
        
        summary=(f"{day_count} Day Overview\n  The lowest temperature will be {formatted_low_temp}, and will occur on {formatted_low_date}.\n  The highest temperature will be {formatted_hg_temp}, and will occur on {formatted_hg_date}.\n  The average low this week is {formatted_avg_low_temp}.\n  The average high this week is {formatted_avg_hg_temp}.\n")
    
#     # print(summary)
    return summary

pass

#################### PASSED #################### 

""" TEST NINE """
""" PRODUCE SUMARY IN THE FOLLOWING FORMAT """
"""
# # ---- Friday 02 July 2021 ----
# #   Minimum Temperature: 9.4°C
# #   Maximum Temperature: 19.4°C
"""

def generate_daily_summary(weather_data):
    daily_summary_data =""
    # string for the output
    for col in weather_data:
        # Formatting the Date to show as this format --> Friday 02 July 2021
        formatted_date = convert_date(col[0])
        # Formatted min Temp to inc °C
        formatted_min_temp = convert_f_to_c(col[1])
        formatted_min_temp_in_c = format_temperature(formatted_min_temp)
        # Formatted Max Temp to inc °C
        formatted_max_temp = convert_f_to_c(col[2])
        formatted_max_temp_in_c = format_temperature(formatted_max_temp)
        
        # String for the daily summary data
        single_summary_data = f"---- {formatted_date} ----\n  Minimum Temperature: {formatted_min_temp_in_c}\n  Maximum Temperature: {formatted_max_temp_in_c}\n\n"
        daily_summary_data = daily_summary_data + single_summary_data
        
    # print(daily_summary_data)
    

    return daily_summary_data
pass


