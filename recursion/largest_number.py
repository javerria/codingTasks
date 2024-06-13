def largest_number(given_nums):
    # Base case
    if len(given_nums) == 1:
        return(given_nums[0])

    first_num = given_nums[0]
    rest_nums = given_nums[1:]

    # Recursive call
    largest_rest = largest_number(rest_nums)

    # Return the largest number
    if first_num > largest_rest:
        return first_num
    else:
        return largest_rest

example_answer = largest_number([3, 1, 6, 8, 2, 4, 5])

print("The largest number in the given list of numbers is:", example_answer)