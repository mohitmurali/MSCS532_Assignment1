# Insertion Sort Algo
# MSCS 532 Assigment - 1

# Insertion Sort algorithm to sort an array in monotonically decreasing order
def insertion_sort_descending(arr):
    # Get the length of the array
    n = len(arr)
    
    # Iterate through the array starting from the second element (index 1)
    for i in range(1, n):
        # Store the current element as the key to be inserted
        key = arr[i]
        
        # Initialize j as the index of the last element in the sorted portion
        j = i - 1
        
        # Move elements of the sorted portion that are less than key
        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]  # Shift the smaller element to the right
            j -= 1  # Move to the next element in the sorted portion
        
        # Place the key in its correct position
        arr[j + 1] = key
    
    # Return the sorted array
    return arr

# Test the algorithm with various cases
if __name__ == "__main__":
    # Define test cases to verify the algorithm
    test_cases = [
        [5, 2, 4, 6, 1, 3],  # Random array
        [1, 2, 3, 4, 5],     # Already sorted in increasing order
        [5, 4, 3, 2, 1],     # Already sorted in decreasing order
        [1, 1, 1, 1],        # Array with duplicates
        [],                   # Empty array
        [1]                   # Single-element array
    ]
    
    # Iterate through each test case
    for arr in test_cases:
        print("Original array:", arr)
        # Use a copy to preserve the original array
        sorted_arr = insertion_sort_descending(arr.copy())
        print("Sorted array in decreasing order:", sorted_arr)
        print()

# Output
# mohitgokul@Mohits-Yoga:/mnt/c/Users/mohit/Desktop/532$ python3 assignment1.py 
# Original array: [5, 2, 4, 6, 1, 3]
# Sorted array in decreasing order: [6, 5, 4, 3, 2, 1]

# Original array: [1, 2, 3, 4, 5]
# Sorted array in decreasing order: [5, 4, 3, 2, 1]

# Original array: [5, 4, 3, 2, 1]
# Sorted array in decreasing order: [5, 4, 3, 2, 1]

# Original array: [1, 1, 1, 1]
# Sorted array in decreasing order: [1, 1, 1, 1]   

# Original array: []
# Sorted array in decreasing order: []

# Original array: [1]
# Sorted array in decreasing order: [1]
