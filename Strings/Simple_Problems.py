string_variable = "Captain America"

# Print each character of a string with its index.
def print_characters_with_index(string_variable):
    for index, character in enumerate(string_variable):
        print(f"Index: {index}, Character: '{character}'")

print_characters_with_index(string_variable)
print("")

# Count vowels in a string.
def count_vowels(string_variable):
    count = 0
    vowels = "AEIOUaeiou"
    for char in string_variable:
        if char in vowels:
            count += 1
    return (f"The number of vowels in '{string_variable}' is: {count}")

print(count_vowels(string_variable))
print("")


# Reverse a string without using [::-1].
def reverse_string(string_variable):
    reversed_string = ""
    for char in string_variable:
        reversed_string = char + reversed_string
    return (f"The reversed string of '{string_variable}' is: '{reversed_string}'")

print(reverse_string(string_variable))
print("")

# Check if a string contains only digits.
def is_digits_only(string_variable):
    if string_variable.isdigit():
        return (f"The string '{string_variable}' contains only digits.")
    else:
        return (f"The string '{string_variable}' does not contain only digits.")
    
print(is_digits_only(string_variable))
print("")


# Check if a string contains only digits without isdigit() method.
def is_digits_only_manual(string_variable):
    for char in string_variable:
        if char < '0' or char > '9':
            return (f"The string '{string_variable}' does not contain any digits.")
    return (f"The string '{string_variable}' contains only digits.")

print(is_digits_only_manual(string_variable))
print("")

# Remove all spaces from a string.
def remove_spaces(string_variable):
    no_space_string = string_variable.replace(" ", "")
    return (f"The string '{string_variable}' without spaces is: '{no_space_string}'")

print(remove_spaces(string_variable))
print("")

# Another approach to remove spaces from a string.
def remove_spaces_manual(string_variable):
    no_space_string = ""
    for char in string_variable:
        if char != " ":
            no_space_string += char
    return (f"The string '{string_variable}' without spaces is: '{no_space_string}'")

print(remove_spaces_manual(string_variable))
print("")


# Check if a string is a palindrome.
def is_palindrome(string_variable):
    cleaned_string = string_variable.replace(" ", "").lower()
    reversed_string = cleaned_string[::-1]
    if cleaned_string == reversed_string:
        return (f"The string '{string_variable}' is a palindrome.")
    else:
        return (f"The string '{string_variable}' is not a palindrome.")
    
print(is_palindrome(string_variable))
print("")

# Another approach to check if a string is a palindrome without using [::-1].
def is_palindrome_manual(string_variable):
    cleaned_string = string_variable.replace(" ", "").lower()
    left, right = 0, len(cleaned_string) - 1
    while left < right:
        if cleaned_string[left] != cleaned_string[right]:
            return (f"The string '{string_variable}' is not a palindrome.")
        left += 1
        right -= 1
    return (f"The string '{string_variable}' is a palindrome.")


# Count Character Frequency
def count_character_frequency(string_variable):
    cleaned_string = string_variable.replace(" ", "").lower()
    frequency = {}
    for char in cleaned_string:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return (f"Character frequency in '{string_variable}': {frequency}")

print(count_character_frequency(string_variable))
print("")

# First Non-Repeating Character
def first_non_repeating_character(string_variable):
    cleaned_string = string_variable.replace(" ", "").lower()
    frequency = {}
    for char in cleaned_string:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    for char in cleaned_string:
        if frequency[char] == 1:
            return (f"The first non-repeating character in '{string_variable}' is: '{char}'")
    return (f"There are no non-repeating characters in '{string_variable}'.")

print(first_non_repeating_character(string_variable))
print("")


# Remove Duplicate Characters
def remove_duplicate_characters(string_variable):
    cleaned_string = string_variable.replace(" ", "").lower()
    unique_characters = ""
    for char in cleaned_string:
        if char not in unique_characters:
            unique_characters += char
    return (f"The string '{string_variable}' with duplicate characters removed is: '{unique_characters}'")

print(remove_duplicate_characters(string_variable))
print("")


# Capitalize First Letter of Each Word
def capitalize_first_letter(string_variable):
    cleaned_string = string_variable.split(" ")
    for i in range(len(cleaned_string)):
        cleaned_string[i] = cleaned_string[i].capitalize()
    result = " ".join(cleaned_string)
    return (f"The string '{string_variable}' with capitalized first letters is: '{result}'")

print(capitalize_first_letter(string_variable))
print("")


# Anagram Check
def are_anagrams(string1, string2):
    cleaned_string1 = string1.replace(" ", "").lower()
    cleaned_string2 = string2.replace(" ", "").lower()
    if sorted(cleaned_string1) == sorted(cleaned_string2):
        return (f"The strings '{string1}' and '{string2}' are anagrams.")
    else:
        return (f"The strings '{string1}' and '{string2}' are not anagrams.")

print(are_anagrams(string_variable, string_variable))  # Test with the same string
print("")

print(are_anagrams(string_variable, "listen"))  # Test with a known anagram
print("")

# Another approach to check if two strings are anagrams without using sorted() function.
def are_anagrams_manual(string1, string2):
    cleaned_string1 = string1.replace(" ", "").lower()
    cleaned_string2 = string2.replace(" ", "").lower()
    
    frequency1 = {}
    frequency2 = {}
    
    for char in cleaned_string1:
        if char in frequency1:
            frequency1[char] += 1
        else:
            frequency1[char] = 1
            
    for char in cleaned_string2:
        if char in frequency2:
            frequency2[char] += 1
        else:
            frequency2[char] = 1
            
    if frequency1 == frequency2:
        return (f"The strings '{string1}' and '{string2}' are anagrams.")
    else:
        return (f"The strings '{string1}' and '{string2}' are not anagrams.")
    
print(are_anagrams_manual("Silent", "Listen"))  # Test with the same string
print("")

# Longest Word in a Sentence
def longest_word(string_variable):
    words = string_variable.split(" ")
    longest = ""
    for word in words:
        if len(word) > len(longest):
            longest = word
    return (f"The longest word in '{string_variable}' is: '{longest}'")

print(longest_word(string_variable))
print("")

# String Compression
def compress_string(string_variable):
    if not string_variable:
        return (f"The compressed string of '{string_variable}' is: ''")
    
    compressed = ""
    count = 1
    
    for i in range(1, len(string_variable)):
        if string_variable[i] == string_variable[i - 1]:
            count += 1
        else:
            compressed += string_variable[i - 1] + str(count)
            count = 1
            
    compressed += string_variable[-1] + str(count)  # Add the last character and its count
    
    return (f"The compressed string of '{string_variable}' is: '{compressed}'")

print(compress_string("aaabbcaaa"))
print("")


# Reverse Words in Sentence withour using split() and join() methods.
def reverse_words(string_variable):
    reversed_sentence = ""
    word = ""
    
    for char in string_variable:
        if char != " ":
            word += char
        else:
            reversed_sentence = word + " " + reversed_sentence
            word = ""
    
    # Add the last word to the reversed sentence
    reversed_sentence = word + " " + reversed_sentence
    
    return (f"The string '{string_variable}' with reversed words is: '{reversed_sentence.strip()}'")

print(reverse_words(string_variable))
print("")