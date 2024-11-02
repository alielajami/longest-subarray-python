'''Longest (Binary) Subarray with Equal Number of 0s and 1s'''

def longest_subarray(array):
    '''Function to find the length of the longest subarray with equal number of 0s and 1s'''
    max_length = 0
    start_index = 0
    end_index = 0

    for start in range(len(array)):
        zeroes = 0
        ones = 0

        for end in range(start, len(array)):
            if array[end] == 0:
                zeroes += 1
            else:
                ones += 1

            if zeroes == ones:
                current_length = end - start + 1
                if current_length > max_length:
                    max_length = current_length
                    start_index = start
                    end_index = end

    long_subarray = array[start_index:end_index + 1]
    return max_length, long_subarray

list_size = int(input("Enter the size of the list: "))
binary_list = []

for i in range(list_size):
    num = int(input(f"Enter Binary Element {i + 1}: "))
    if 1 >= num >= 0:
        binary_list.append(num)
    else:
        print("Invalid input. Enter 0 or 1.")
        break

length, subarray = longest_subarray(binary_list)
print(f"The longest subarray with equal number of 0s and 1s is {length} digits long.")
print(f"The subarray is: {subarray}")
