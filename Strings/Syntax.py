chai = "Masala Chai"

# Slicing to get the first character, first word, last character, and last word
first_char = chai[0]
first_word = chai[0:6]
last_char = chai[-1]
last_word = chai.split()[-1]

# Print the results
print("First character:", first_char)
print("First word:", first_word)
print("Last character:", last_char)
print("Last word:", last_word)
print("")


# convert to lowercase and uppercase
lowercase_chai = chai.lower()
uppercase_chai = chai.upper()

print("Lowercase:", lowercase_chai)
print("Uppercase:", uppercase_chai)
print("")


new_chai = "    Lemon Tea    "

# Remove leading and trailing whitespace
trimmed_chai = new_chai.strip()
print("Original string:", repr(new_chai))
print("Trimmed string:", repr(trimmed_chai))
print("")


# Replace "Masala" with "Lemon"
replaced_chai = chai.replace("Masala", "Lemon")
print("Original string:", chai)
print("Replaced string:", replaced_chai)
print("")

chai = "Lemon, Masala, Green, Black"

# Split the string into a list of teas
tea_list = chai.split(", ")
print("Original string:", chai)
print("List of teas:", tea_list)
print("")

# Find the index of "Chai" in the string
chai = "Masala Chai"
chai_index= chai.find("Chai")
print("Original string:", chai)
print("Index of 'Chai':", chai_index)
print("")


# count the occurrences of "Chai" in the string
chai = "Masala Chai Chai Chai"
quantity = 2
order = "I ordered {} cups of {} chai"
chai_count = chai.count("Chai")
print("Original string:", chai)
print("Count of 'Chai':", chai_count)
print("")

# Format the string to include the quantity and type of chai
print(order.format(quantity, chai))


# List to string conversion
tea_list = ["Lemon", "Masala", "Green", "Black"]
tea_string = ", ".join(tea_list)
tea_dash_string = " - ".join(tea_list)

print("List of teas:", tea_list)
print("String of teas:", tea_string)
print("Dash-separated string:", tea_dash_string)
print("")

# Check length of the string
chai = "Masala Chai"
length_of_chai = len(chai)
print("Original string:", chai)
print("Length of the string:", length_of_chai)
print("")


# use loop to iterate through each character in the string
chai = "Masala Chai"
print("Characters in the string:")
for char in chai:
    print(char)
print("")

# use escape characters to include quotes in the string
dialogue = "Be the \"change\" that you wish to see in the world"
print("Dialogue:", dialogue)
print("")


# raw string to ignore escape characters
chai = r"masala\nchai"
print("Raw string:", chai)
print("")

# raw string to include backslashes in the file path
raw_path= r"R:\Data Structures And Algorithms\Strings\Syntax.py"
print("Raw file path:", raw_path)
print("")


# if word present in the string
chai = "Masala Chai"
word_to_check = "Masala"
if word_to_check in chai:
    print(f"'{word_to_check}' is present in the string.")
else:
    print(f"'{word_to_check}' is not present in the string.")
print("")