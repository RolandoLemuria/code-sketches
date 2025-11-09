"""
Word Counter Sketch
Count words in a text file or string.

This sketch demonstrates how to count word frequencies using Python's
built-in Counter class, which makes counting easy and efficient.
"""

from collections import Counter

def count_words(text):
    """
    Count word frequency in text.
    
    Args:
        text: A string containing the text to analyze
        
    Returns:
        A Counter object with word frequencies (like a dictionary)
    """
    # Convert text to lowercase so "Python" and "python" are counted as the same word
    # Then split the text into individual words using spaces as separators
    words = text.lower().split()
    
    # Counter automatically counts how many times each word appears
    # It returns a special dictionary-like object
    return Counter(words)

# Quick test
# This block only runs when the file is executed directly
if __name__ == "__main__":
    # Sample text with repeated words
    sample = "Python is awesome Python is powerful Python is fun"
    
    # Count the words
    result = count_words(sample)
    
    # Print all word frequencies
    print(f"Word frequencies: {result}")
    
    # Print the 3 most common words
    # most_common(n) returns a list of the n most frequent words and their counts
    print(f"Most common: {result.most_common(3)}")
