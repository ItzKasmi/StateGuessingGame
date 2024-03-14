import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240314.csv")
fur_color = data["Primary Fur Color"]

gray_fur = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_fur = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_fur = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Colors": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_fur, cinnamon_fur, black_fur]
}

new_data = pandas.DataFrame(data_dict)
new_data.to_csv("squirrel_count.csv")
