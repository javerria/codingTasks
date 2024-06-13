def adding_up_to(given_list, given_index):
    # Base case
    if given_index <= 0:
        return given_list[0]
    
    # Recursive call
    return adding_up_to(given_list, given_index - 1) + given_list[given_index]

answer = adding_up_to([1, 4, 5, 3, 12, 16], 4) 
print(answer)

