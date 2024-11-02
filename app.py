'''Longest (Binary) Subarray with Equal Number of 0s and 1s'''

def longest_subarray(array):
    '''Function to find the length of the longest subarray with equal number of 0s and 1s'''
    max_length = 0

    for start in range(len(array)):
        zeroes = 0
        ones = 0

        for end in range(start, len(array)):
            if array[end] == 0:
                zeroes += 1
            else:
                ones += 1

            if zeroes == ones:
                max_length = max(max_length, end - start + 1)

    return max_length


