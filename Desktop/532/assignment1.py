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
