"""
Timer Decorator Sketch
Measure execution time of functions.

A decorator is a function that wraps another function to add extra functionality.
This timer decorator measures how long a function takes to run - useful for
performance testing and optimization.
"""

import time
from functools import wraps

def timer(func):
    """
    Decorator to measure function execution time.
    
    A decorator takes a function and returns a modified version of it.
    This one adds timing functionality without changing the original function.
    
    Args:
        func: The function to be timed
        
    Returns:
        A wrapped version of the function that includes timing
    """
    # @wraps preserves the original function's name and documentation
    @wraps(func)
    def wrapper(*args, **kwargs):
        """
        The wrapper function that actually does the timing.
        
        *args and **kwargs allow the wrapper to accept any arguments
        and pass them to the original function.
        """
        # Record the start time (in seconds since epoch)
        start = time.time()
        
        # Call the original function and save its result
        result = func(*args, **kwargs)
        
        # Record the end time
        end = time.time()
        
        # Calculate and print the elapsed time
        print(f"{func.__name__} took {end - start:.4f} seconds")
        
        # Return the original function's result
        return result
    
    return wrapper

# Example usage: Apply the @timer decorator to a function
@timer
def slow_function():
    """
    Example slow function that takes 1 second to run.
    
    The @timer decorator above means this function will automatically
    report its execution time when called.
    """
    # Sleep for 1 second to simulate a slow operation
    time.sleep(1)
    return "Done!"

@timer
def fast_function():
    """Example fast function."""
    # This function completes almost instantly
    return sum(range(1000))

# Quick test
# This block only runs when the file is executed directly
if __name__ == "__main__":
    # Call the slow function - it will print its execution time
    result1 = slow_function()
    print(result1)
    
    print()  # Empty line for readability
    
    # Call the fast function - it will also print its execution time
    result2 = fast_function()
    print(f"Sum result: {result2}")
