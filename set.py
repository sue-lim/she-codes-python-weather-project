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


###########################################################################

# from csv import reader
import csv 
def load_data_from_csv(csv_file):
    
    weather_data = []
    with open(csv_file, 'r') as csv_file:
                reader = csv.reader(csv_file)
                next(reader)
                # data = list(reader)

                for line in reader:
                    weather_data.append(line)
                # for data in weather_data:
            
                    print(weather_data)
    return weather_data
# import csv 
# def load_data_from_csv(csv_file):
    
#     weather_data = []
#     with open(csv_file, 'r') as csv_file:
#                 reader = csv.reader(csv_file)
#                 next(reader)
#                 w_data = list(reader)
#                 # for line in reader:
#                 #     weather_data.append(line)
            
#                 print(w_data)
# load_data_from_csv("tests\data\example_one.csv")  
# load_data_from_csv("tests\data\example_two.csv")  
# load_data_from_csv("tests\data\example_three.csv") 
    #     print(weather_data)
        
    # print(w_data)
    



