# Read input and convert it to a list of integers
numbers = list(map(int, input().split()))

# Filter out negative numbers and sort them in descending order
negative_numbers = sorted([num for num in numbers if num < 0], reverse=True)

# Print the negative numbers in descending order, separated by spaces
for num in negative_numbers:
    print(num, end=' ')