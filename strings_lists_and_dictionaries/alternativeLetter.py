example_string = "You have bewitched me, body and soul."

#Store the string as a list where each letter is an element
split_string = list(example_string)

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

