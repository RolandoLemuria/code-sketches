"""
Bubble Sort Algorithm Sketch
A simple implementation of bubble sort to practice sorting algorithms.

Bubble sort works by repeatedly comparing adjacent elements and swapping them
if they're in the wrong order. Like bubbles rising to the surface, larger
numbers "bubble up" to the end of the list.
"""

def bubble_sort(arr):
    """Sort array using bubble sort algorithm."""
    # Get the length of the array
    n = len(arr)
    
    # We need to go through the array multiple times
    # Each pass moves the largest unsorted element to its correct position
    for i in range(n):
        # Flag to track if any swaps happened in this pass
        # If no swaps occur, the array is already sorted
        swapped = False
        
        # Compare adjacent elements
        # We don't need to check the last 'i' elements because they're already sorted
        for j in range(0, n - i - 1):
            # If current element is greater than the next one, swap them
            if arr[j] > arr[j + 1]:
                # Swap using Python's tuple unpacking
                # This swaps the values at positions j and j+1
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True  # Mark that we made a swap
        
        # If no swaps happened, the array is sorted, so we can stop early
        if not swapped:
            break
    
    return arr

# Quick test
# This block only runs when the file is executed directly (not imported)
if __name__ == "__main__":
    # Create a list of unsorted numbers
    numbers = [64, 34, 25, 12, 22, 11, 90]
    print(f"Original: {numbers}")
    
    # Sort a copy of the list (so we keep the original unchanged)
    sorted_numbers = bubble_sort(numbers.copy())
    print(f"Sorted: {sorted_numbers}")