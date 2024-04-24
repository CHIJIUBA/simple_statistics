data = [10, 20, 30, 40, 50]

def calculate_mean(data):
    """
    Calculate the mean of a dataset
    """
    n = len(data)
    mean = sum(data) / n
    return mean

def calculate_mode(data):
    """
    Calculate the mode of a dataset.
    """
    # Create a dictionary to store the frequency of each element
    freq_dict = {}
    for item in data:
        if item in freq_dict:
            freq_dict[item] += 1
        else:
            freq_dict[item] = 1
    
    # Find the mode(s) by finding the maximum frequency
    max_freq = max(freq_dict.values())
    mode = [key for key, value in freq_dict.items() if value == max_freq]
    
    return mode

def calculate_median(data):
    """
    Calculate the median of a dataset.
    """
    sorted_data = sorted(data)
    n = len(sorted_data)
    
    if n % 2 == 0:
        # If the number of elements is even, average the middle two elements
        mid_index1 = n // 2 - 1
        mid_index2 = n // 2
        median = (sorted_data[mid_index1] + sorted_data[mid_index2]) / 2
    else:
        # If the number of elements is odd, take the middle element
        mid_index = n // 2
        median = sorted_data[mid_index]
    
    return median

def calculate_std_dev(data):
    """
    Calculate the standard deviation of a dataset
    """
    n = len(data)
    mean = sum(data) / n
    squared_diff_sum = sum((x - mean) ** 2 for x in data)
    variance = squared_diff_sum / n
    std_dev = variance ** 0.5
    return std_dev


print("The mean is", calculate_mean(data))
print("The mode is", calculate_mode(data))
print("The median is", calculate_median(data))
print("The standard deviation is", calculate_std_dev(data))

