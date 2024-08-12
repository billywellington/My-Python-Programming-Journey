# Day 25.: Reading CSV data using pandas

# Method 1: Without using pandas

# import csv
#
# with open("weather_data.csv") as file:
#     data = csv.reader(file)
#
#     temperature = []
#     for item in data:
#             if item[1] != "temp":
#                 temperature.append(int(item[1]))
#
# print(temperature)
#

# Method 2: Using pandas
import pandas
file = pandas.read_csv("weather_data.csv")
# print(file["temp"])

# #using data frame methods
# data_dict = file.to_dict()
# print(data_dict)
#
# #using series methods
# temp_list = file["temp"].to_list()
# print(temp_list)
#
# #calculate the average temperature : method 1
# sum = i = 0
# for i in range(len(temp_list)):
#     if i < len(temp_list):
#         sum += temp_list[i]
#         i += 1
#
# average_temp = sum/i
# print(f"Average temperature: {average_temp}")
#
# #method 2: using the series mean method
#
# average_temp = file["temp"].mean()
# print(f"Average temperature: {average_temp}")
#
#
# #calculate the maximum temperature
# max_temp = file["temp"].max()
# print(f"Maximum temperature: {max_temp}")
#
# #Getting the data in columns
# print(file["condition"])
# print(file.condition)

# Getting the data in rows
# print(file[file.day == "Monday"])
# print(file[file["day"] == "Monday"]) #same as above

# Getting the row with the maximum temperature
# print(file[file.temp == file.temp.max()])

# monday = file[file.day == "Monday"]
# # print(monday.condition)
#
# #calculate the temp for Monday in celcius degrees using the formula (temp_c = (temp_f - 32) * 5/9)
# monday_temp = int(monday.temp) # gives error, but it does work: Use int(ser.iloc[0]) instead
#
# monday_temp = int(monday["temp"].iloc[0])
# # monday_temp = monday.temp.iloc[0] #this also works
# # monday_temp = monday.temp[0] #this also works
#
# monday_temp_c = (monday_temp - 32) * 5/9
# print(f"Temperature in degrees celcius is {monday_temp_c:.2f}")
#

# create a dict called data_dict with student names and score
# Creating a dictionary with two keys: 'student_names' and 'student_scores'
data_dict = {
    "student_names": ["Alice", "Bob", "Charlie", "Diana"],
    "student_scores": [88, 76, 93, 85]
}

# Creating a pandas DataFrame from the dictionary
data_frame = pandas.DataFrame(data_dict)
print(data_frame)

# Creating a new CSV file from the DataFrame
data_frame.to_csv("new_data.csv")
