'''Longest (Binary) Subarray with Equal Number of 0s and 1s'''

def longest_subarray(array):
    '''Function to find the length of the longest subarray with equal number of 0s and 1s'''
    max_length = 0 # Initialize the maximum length of the subarray
    start_index = 0 # Initialize the start index of the subarray
    end_index = 0 # Initialize the end index of the subarray

    for start in range(len(array)): # Iterate through the array
        zeroes = 0 # Initialize the count of zeroes
        ones = 0 # Initialize the count of ones

        for end in range(start, len(array)): # Iterate the array starting from current start index
            if array[end] == 0:
                zeroes += 1 # Increment the count of zeroes
            else:
                ones += 1 # Increment the count of ones

            if zeroes == ones: # If the count of zeroes and ones are equal
                current_length = end - start + 1 # Calculate the length of the subarray
                if current_length > max_length: # If the current length is greater than the maximum
                    max_length = current_length # Update the maximum length
                    start_index = start # Update the start index
                    end_index = end # Update the end index

    long_subarray = array[start_index:end_index + 1] # Get subarray with equal number of 0s and 1s
    return max_length, long_subarray # Return the maximum length and the subarray

list_size = int(input("Enter the size of the list: ")) # Input the size of the list
binary_list = [] # Initialize the binary list

for i in range(list_size):
    num = int(input(f"Enter Binary Element {i + 1}: ")) # Input the binary elements
    if 1 >= num >= 0: # Check if the input is binary
        binary_list.append(num) # Append the binary element to the list
    else: # If the input is not binary
        print("Invalid input. Enter 0 or 1.") # Print an error message
        break # Exit the loop

length, subarray = longest_subarray(binary_list) # Get the length and the subarray
print(f"The longest subarray with equal number of 0s and 1s is {length} digits long.")
print(f"The subarray is: {subarray}") # Print the length and the subarray
