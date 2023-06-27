def sum_numbers(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

my_list = list(map(int, input("Enter a list of numbers (space-separated): ").split()))
result = sum_numbers(my_list)
print(result)

