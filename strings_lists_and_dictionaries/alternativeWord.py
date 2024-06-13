example_string = "You have bewitched me, body and soul."

#Split the string into its component words and store in a list
split_string = example_string.split()

#Loop through each index in the list
index = 0
while index < len(split_string):
    if index % 2 == 0: #Even indexes
      split_string[index] = split_string[index].upper() #Capitalise the word
    else: #All other indexes, i.e. odd
       split_string[index] = split_string[index].lower() #Convert to lowercase
    index += 1 #Iterate through next index

#Join the words into a string and store as variable
transformed_string = " ".join(split_string)

#Get output
print(transformed_string)

