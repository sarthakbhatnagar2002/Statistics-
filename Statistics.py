def calculate_mean(data):
    return sum(data) / len(data) if len(data) > 0 else 0

def calculate_mode(data):
    # Count occurrences of each number
    count_dict = {}
    for num in data:
        count_dict[num] = count_dict.get(num, 0) + 1

    # Find the mode(s)
    max_count = max(count_dict.values())
    mode = [num for num, count in count_dict.items() if count == max_count]

    return mode[0] if len(mode) == 1 else mode

def calculate_median(data):
    sorted_data = sorted(data)
    n = len(sorted_data)

    if n % 2 == 0:
        # If the number of elements is even, take the average of the middle two
        middle1 = sorted_data[n // 2 - 1]
        middle2 = sorted_data[n // 2]
        return (middle1 + middle2) / 2
    else:
        # If the number of elements is odd, return the middle element
        return sorted_data[n // 2]

def calculate_variance(data, mean):
    n = len(data)
    if n <= 1:
        return 0

    sum_squared_diff = sum((x - mean) ** 2 for x in data)
    return sum_squared_diff / (n - 1)

def calculate_std_dev(variance):
    return variance ** 0.5

# Take input from the user
user_input = input("Enter a list of numbers separated by spaces: ")

# Convert the input string into a list of floats
data = [float(x) for x in user_input.split()]

# Calculate statistics
mean = calculate_mean(data)
mode = calculate_mode(data)
median = calculate_median(data)
variance = calculate_variance(data, mean)
std_dev = calculate_std_dev(variance)

# Display the results
print(f"Mean: {mean}")
print(f"Mode: {mode}")
print(f"Median: {median}")
print(f"Variance: {variance}")
print(f"Standard Deviation: {std_dev}")
