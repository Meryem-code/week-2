# Program to calculate the sum of numbers in a list

# Function to calculate sum
def calculate_sum(numbers):
    return sum(numbers)

# Ask the user for a list of numbers
print("Enter a list of numbers separated by spaces:")
user_input = input()

# Convert the input string into a list of integers
try:
    number_list = list(map(int, user_input.split()))
    total = calculate_sum(number_list)
    print(f"The sum of the numbers is: {total}")
except ValueError:
    print("Please enter valid numbers!")
