"""
# Summary of Answers

Part 1:
- Typing system differences between Python and Java.
- Error handling example with try-except in Python.
- Syntax differences between Python and Java.

Part 2:
- A function that reads a file and counts word occurrences.
- An enhanced version of the function that removes common stopwords before counting.

Part 3:
- An extension of the word count function that removes punctuation using regular expressions.
"""
"""
# Python and Java Comparison, Word Counting, and Stopword Handling

This exercise is designed to help you demonstrate your knowledge of Python, compare it to Java, and apply basic string processing techniques such as counting word occurrences and excluding stopwords.

## Part 1: Python vs. Java
Complete the following comparisons between Python and Java. Provide the Python code snippets where necessary.

1. **Typing System**: Describe how typing differs between Python and Java.

2. **Error Handling**: Describe how Python's error handling differs from Java's. Provide a simple try-except example in Python.

3. **Syntax Differences**: List at least two syntax differences between Python and Java.
"""

def handle_exception():
    try:
        # Trying to open a file that doesn't exist
        file = open("non_existent_file.txt", "r")
    except FileNotFoundError as e:
        print(f"Error: {e}")
    finally:
        print("Cleaning up resources...")

# Example usage:
handle_exception()

"""
## Part 2: Word Counting and Stopword Removal

You will now implement a function that reads a file, counts the occurrence of each word, and excludes common stopwords.

### Task 1: Word Count
Complete the `count_words` function to read the contents of a file and count the occurrence of each word in the text.

### Task 2: Handle Stopwords
Update your function to remove common stopwords before counting the words.
"""

from collections import Counter

def count_words(filename: str) -> dict:
    """
    Reads the content of the file and returns a dictionary with the count of each word.
    """
    with open(filename, "r") as file:
        text = file.read().lower()  # Read file and convert to lowercase
    words = text.split()  # Split text into words (whitespace-separated)
    word_count = Counter(words)  # Use Counter to count word occurrences
    return word_count

# Example usage:
# Assuming 'file.txt' contains "hello world hello"
# print(count_words("file.txt"))  # Output: {'hello': 2, 'world': 1}


def count_words_with_stopwords(filename: str) -> dict:
    """
    Reads the file, filters out stopwords, and counts the occurrences of each remaining word.
    """
    stopwords = {'the', 'and', 'is', 'in', 'at', 'of', 'a'}

    with open(filename, "r") as file:
        text = file.read().lower()  # Read file and convert to lowercase

    words = text.split()  # Split text into words

    # Filter out stopwords
    filtered_words = [word for word in words if word not in stopwords]

    word_count = Counter(filtered_words)  # Use Counter to count remaining words
    return word_count

# Example usage:
# Assuming 'file.txt' contains "the quick brown fox and the lazy dog"
# print(count_words_with_stopwords("file.txt"))  # Output: {'quick': 1, 'brown': 1, 'fox': 1, 'lazy': 1, 'dog': 1}

"""
## Part 3: Bonus Task - Regex and Punctuation Handling

Extend your `count_words_with_stopwords` function to remove punctuation marks such as periods, commas, etc., using regular expressions.

Example:
- Input: "Hello, world! Hello?"
- Output: {'hello': 2, 'world': 1}
"""

import re

def count_words_with_stopwords_and_punctuation(filename: str) -> dict:
    """
    Extends the word counting function to remove punctuation marks.
    Uses regular expressions to ensure words are correctly counted without punctuation.
    """
    stopwords = {'the', 'and', 'is', 'in', 'at', 'of', 'a'}

    with open(filename, "r") as file:
        text = file.read().lower()  # Read file and convert to lowercase

    # Use regex to remove punctuation marks
    text = re.sub(r'[^\w\s]', '', text)  # Remove anything that is not a word character or whitespace

    words = text.split()  # Split text into words

    # Filter out stopwords
    filtered_words = [word for word in words if word not in stopwords]

    word_count = Counter(filtered_words)  # Use Counter to count remaining words
    return word_count

# Example usage:
# Assuming 'file.txt' contains "Hello, world! Hello?"
# print(count_words_with_stopwords_and_punctuation("file.txt"))  # Output: {'hello': 2, 'world': 1}
