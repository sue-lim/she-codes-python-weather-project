# print('convert_f_to_c(temp_in_farenheit):')
# def convert_f_to_c(temp_in_farenheit):
#     celcius = ((temp_in_farenheit-32)* 5/9)

#     return round(celcius,1)
# n = float(input("Enter Farenheit to convert: "))
# f_output = str(convert_f_to_c(n)) ##enter farenheit##
# print("The result is:") 
# print(f_output)

#################################COMPLETED#################################

# def convert_f_to_c(temp_in_farenheit): 
#     c = (float(temp_in_farenheit)-32)* 5/9
#     return round(c,1)

###########################################################################


############################################################



#################################COMPLETED#################################

# def calculate_mean(weather_data):
#     num = 0
#     for t in weather_data:
#         num = num + float(t)

#     avg = num / len(weather_data)
#     return (avg)

#################################COMPLETED#################################
# def convert_date(iso_string):
#     from datetime import datetime
#     original_date = iso_string
#     new_date = datetime.strptime(original_date, "%Y-%m-%dT%H:%M:%S%z")
#     new_date_string = datetime.strftime(new_date, "%A %d %B %Y")
#     return(str(new_date_string))



#################################COMPLETED#################################
# # from csv import reader
# import csv 
# def load_data_from_csv(csv_file):
    
#     weather_data = []
#     with open(csv_file, 'r') as csv_file:
#         reader = csv.reader(csv_file)
#         next(reader) #skip the header line
#         data = list(reader) #sublist command
#         print(data) #row
#         for line in data: 
                    
#             if line: ##check for if line is not empty then append##
#                 weather_data.append([line[0],int(line[1]),int(line[2])])
                    
#     return weather_data

# load_data_from_csv("tests\data\example_one.csv")  
# load_data_from_csv("tests\data\example_two.csv")  
# load_data_from_csv("tests\data\example_three.csv") 
    #     print(weather_data)
        
###########################################################################
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
    
# def find_min(weather_data):
#     min_idx = None
#     min_val = weather_data
#     min_num = min(min_val, default=0)
#     for i in range(len(min_val)):
#             if min_val [i] == min_num:
#                 min_idx = i
#                 # print(min_num, min_idx)


#     return(((float(min_num)),min_idx))



###########################################################################
# 
    # """Calculates the minimum value in a list of numbers.

    # Args:
    #     weather_data: A list of numbers.
    # Returns:
    #     The minium value and it's position in the list.
    # """
    # pass


# def find_max(weather_data):
#     max_idx = None
#     max_val = weather_data
#     max_num = max(max_val, default=0)
#     for i in range(len(max_val)):
#         if max_val [i] == max_num:
#             max_idx = i

#     # print (f'({max_num}, {max_idx})')


#     return(((float(max_num)),max_idx))  


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

#     return weather_data

# generate_daily_summary("C:\GIT\my-portfolio\she-codes-python-weather-project-sue-lim\tests\expected_output\example_one_daily_summary.txt")  
# generate_daily_summary("C:\GIT\my-portfolio\she-codes-python-weather-project-sue-lim\tests\expected_output\example_two_daily_summary.txt")  
# generate_daily_summary("C:\GIT\my-portfolio\she-codes-python-weather-project-sue-lim\tests\expected_output\example_three_daily_summary.txt") 
        # print(weather_data)
    # """Outputs a daily summary for the given weather data.

    # Args:
    #     weather_data: A list of lists, where each sublist represents a day of weather data.
    # Returns:
    #     A string containing the summary information.
    # """
pass
