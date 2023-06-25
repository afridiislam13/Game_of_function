def sum_numbers():
    num_list = input("Enter a list of numbers (space-separated): ").split()

    num_list = [int(num) for num in num_list]

    total_sum = sum(num_list)

    return total_sum
