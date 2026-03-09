import random

questions = [
    "Print each character of a string with its index.",
    "Count vowels in a string.",
    "Reverse a string without using slicing.",
    "Check if a string contains only digits.",
    "Check if a string contains only digits without using isdigit().",
    "Remove all spaces from a string.",
    "Remove all spaces from a string without using replace().",
    "Check if a string is a palindrome.",
    "Check if a string is a palindrome without using slicing.",
    "Count character frequency in a string.",
    "Find the first non-repeating character in a string.",
    "Remove duplicate characters from a string.",
    "Capitalize the first letter of each word in a string.",
    "Check if two strings are anagrams.",
    "Check if two strings are anagrams without using sorted().",
    "Find the longest word in a sentence.",
    "Perform string compression (e.g., aaabbcaaa -> a3b2c1a3).",
    "Reverse words in a sentence without using split() and join()."
]

random_question = random.choice(questions)
print(f"Question: {random_question}")
