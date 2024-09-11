"""
# Python and Java Comparison, Word Counting, and Stopword Handling

This exercise is designed to help you demonstrate your knowledge of Python, compare it to Java, and apply basic string processing techniques such as counting word occurrences and excluding stopwords.

## Part 1: Python vs. Java
Complete the following comparisons between Python and Java. Provide the Python code snippets where necessary.

1. **Typing System**: Describe how typing differs between Python and Java.

2. **Error Handling**: Describe how Python's error handling differs from Java's. Provide a simple try-except example in Python.

3. **Syntax Differences**: List at least two syntax differences between Python and Java.
"""

# TODO: Part 1 - Typing System
# Describe the difference in typing between Python and Java:
# (Answer in a comment here)

# TODO: Part 1 - Error Handling
# Provide a Python example for handling exceptions in a try-except block:
def handle_exception():
    """
    This function should handle an exception in Python and print a message.
    For example, open a file that doesn't exist, and handle the error properly.
    """
    # Your code goes here:
    pass

# TODO: Part 1 - Syntax Differences
# List at least two syntax differences between Python and Java here (as comments):


"""
## Part 2: Word Counting and Stopword Removal

You will now implement a function that reads a file, counts the occurrence of each word, and excludes common stopwords.

### Task 1: Word Count
Complete the `count_words` function to read the contents of a file and count the occurrence of each word in the text.

### Task 2: Handle Stopwords
Update your function to remove common stopwords before counting the words.
"""

from collections import Counter

# TODO: Task 1 - Word Count
def count_words(filename: str) -> dict:
    """
    Reads the content of the file and returns a dictionary with the count of each word.

    Example:
    - Input: 'file.txt' (with content "hello world hello")
    - Output: {'hello': 2, 'world': 1}
    """
    # Your code here: Read the file and count word occurrences
    pass


# TODO: Task 2 - Handle Stopwords
def count_words_with_stopwords(filename: str) -> dict:
    """
    Reads the file, filters out stopwords, and counts the occurrences of each remaining word.

    Example:
    - Input: 'file.txt' (with content "the quick brown fox and the lazy dog")
    - Output: {'quick': 1, 'brown': 1, 'fox': 1, 'lazy': 1, 'dog': 1}

    Stopwords to exclude: ['the', 'and', 'is', 'in', 'at', 'of', 'a']
    """
    stopwords = {'the', 'and', 'is', 'in', 'at', 'of', 'a'}
    # Your code here: Read file, filter out stopwords, and count occurrences
    pass


"""
## Part 3: Bonus Task - Regex and Punctuation Handling

Extend your `count_words_with_stopwords` function to remove punctuation marks such as periods, commas, etc., using regular expressions.

Example:
- Input: "Hello, world! Hello?"
- Output: {'hello': 2, 'world': 1}
"""

# TODO: Task 3 - Regex and Punctuation Handling
import re

def count_words_with_stopwords_and_punctuation(filename: str) -> dict:
    """
    Extends the word counting function to remove punctuation marks.
    Uses regular expressions to ensure words are correctly counted without punctuation.
    """
    stopwords = {'the', 'and', 'is', 'in', 'at', 'of', 'a'}
    # Your code here: Use regex to remove punctuation and filter stopwords
    pass
