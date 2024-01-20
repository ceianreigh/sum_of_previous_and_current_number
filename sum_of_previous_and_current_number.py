# Write a program to iterate the first 10 numbers, and in each iteration, print the sum of the current and previous number.

# pseudocode

# add a starting message
print("Printing current and previous number sum in a range(10)")

# create a variable called previous_number and set it to 0
previous_number = 0

# create a for loop that iterates 10 times
for i in range(10):
    # create a variable called current_number and set it to i
    current_number = i

    # create a variable called sum_of_previous_and_current_number and set it to previous_number + current_number
    sum_of_previous_and_current_number = previous_number + current_number

    # print the current, previous, and sum of previous and current number
    print(
        "The current number is",
        current_number,
        "while, the previous number is",
        previous_number,
        "and the sum of them is",
        sum_of_previous_and_current_number,
    )

    # update previous_number to current_number
    previous_number = current_number
