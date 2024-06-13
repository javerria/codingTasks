# Available items on the menu

menu_list = ["chicken", "fish", "lamb", "beef"]

 

# Available stock for each item

dict_stock = {"chicken":5, "fish":8, "lamb": 12, "beef":3}

 

# Price for each item

dict_price = {"chicken":15, "fish":18, "lamb":25, "beef":25}

 

# Define variable to hold total value

total_stock = 0

 

# Iterate over each menu item

for i in menu_list:

    item_worth = dict_price[i]*dict_stock[i]

    total_stock += item_worth

   

print("The total stock currently in the cafe is worth £"+str(total_stock))