import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
new_data = data["Primary Fur Color"]

#Creating Separate dataFrame for each color
grey_squirrel = new_data[new_data == "Gray"]
black_squirrel = new_data[new_data == "Black"]
cinnamon_squirrel = new_data[new_data == "Cinnamon"]

#Calculating Number of squirrels in each color
#Note: This is just to showcase, to make the code shorter, len() function can be added in the previous variables directly.
num_grey_squirrel = len(grey_squirrel)
num_black_squirrel = len(black_squirrel)
num_cinnamon_squirrel = len(cinnamon_squirrel)

#Creating a new csv

data_dict = {
    "Fur Color": ["Gray","Black","Cinnamon"],
    "Count": [num_grey_squirrel,num_black_squirrel,num_cinnamon_squirrel]
}

statistics = pandas.DataFrame(data_dict)

statistics.to_csv("number_of_grey_black_cinnamon_squirrels")
