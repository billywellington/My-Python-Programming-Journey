student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#Create a dictionary in this format:
with open("nato.csv") as file:
    list = [line.strip() for line in file.readlines()]


list.pop(0)
nato_dict = {row.split(",")[0]: row.split(",")[1] for row in list}
# print(nato_dict)

#TCreate a list of the phonetic code words from a word that the user inputs.
word = input("Enter a word: ").upper()
list = [nato_dict[letter] for letter in word]



