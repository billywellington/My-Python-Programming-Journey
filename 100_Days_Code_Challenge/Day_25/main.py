
# The code uses the pandas library to read the data from a csv file and to create a new csv file
# with the squirrel count data

import pandas

data = pandas.read_csv("squirel_original.csv")

gray_squirrels = data[data["Primary Fur Color"] == "Gray"]
gray_squirrels_count = len(gray_squirrels)

cinnamon_squirrels = data[data["Primary Fur Color"] == "Cinnamon"]
cinnamon_squirrels_count = len(cinnamon_squirrels)

red_squirrels = data[data["Primary Fur Color"] == "Cinnamon"]
red_squirrels_count = len(red_squirrels)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Red"],
    "Count": [gray_squirrels_count, cinnamon_squirrels_count, red_squirrels_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")
