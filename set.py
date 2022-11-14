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
    list_of_numbers = (float(weather_data))
    min_number = min(list_of_numbers)
    for i in range(len(list_of_numbers)):
            if list_of_numbers[i] == min_number:
                min_index = i
                
                print(min_index)
                print(min_number)


#     t = weather_data
#     min_val = t[0]
#     min_idx = 0
#     for i in range(len(t)):
#         if t < min_val:
#             min_val = t[i]
#             min_idx = i 
            
#     print(min_val)
#     print(min_idx)
###########################################################################
    # min_val = weather_data[0]
    # min_idx = 0
    # for i in  range (1, len(weather_data)):
    #     if weather_data[i] < min_val:
    #         min_val = weather_data[i]
    #         min_idx = i      
    # # return (float(min_val), min_idx)
    # print(float(min_val))
    # print(min_idx)
###########################################################################
    # num = weather_data[0]
    # min_index = 0
    # min_num = min[weather_data]
    # for i in range(len(weather_data)):
    #     if num[i] == min_num:
    #         min_index = i
    # return(float(num, min_index))
###########################################################################
    # min_val = weather_data[0]
    # min_idx = 0
    # for i in  range (1, len(weather_data)):
    #     if weather_data[i] < min_val:
    #         min_val = weather_data[i]
            
    # for i in  range (1, len(weather_data)):
    #     if weather_data[i] < min_val:
    #         min_idx == i
            
    # return (float(min_val), min_idx)

    # minimum = weather_data[0]
    # for i in  range (1, len(weather_data)):
    #     if weather_data[i] < minimum:
    #         minimum = weather_data[i]
            
    # print(minimum, weather_data)
    
###########################################################################
# 
    # """Calculates the minimum value in a list of numbers.

    # Args:
    #     weather_data: A list of numbers.
    # Returns:
    #     The minium value and it's position in the list.
    # """
    # pass

# print(minimum)

    



