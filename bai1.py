def sliding_window_max(num_list, size):
    if size <= 0 or size > len(num_list):
        return []

    result = []
    for i in range(len(num_list) - size + 1):
        window = num_list[i:i+size]
        result.append(max(window))
    return result

num_list = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
size = 3
output = sliding_window_max(num_list, size)
print(output) 
