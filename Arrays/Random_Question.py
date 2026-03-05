import random
from datetime import date

array_questions = [
    "1. Print all elements of an array",
    "2. Find the sum of all elements",
    "3. Find the average of elements",
    "4. Find the maximum element",
    "5. Find the minimum element",
    "6. Count even numbers in an array",
    "7. Count odd numbers in an array",
    "8. Search for a given element (linear search)",
    "9. Check if an element exists in the array",
    "10. Reverse an array",
    "11. Copy one array into another",
    "12. Find the second largest element",
    "13. Check if the array is sorted",
    "14. Count how many times a number appears",
    "15. Find the index of a given element",
    "16. Remove duplicates (basic way)",
    "17. Move all zeros to the end",
    "18. Find the difference between max and min",
    "19. Find the largest and smallest in one traversal",
    "20. Replace negative numbers with 0",
    "21. Find the first repeating element",
    "22. Find the first non-repeating element",
    "23. Check if two arrays are equal"
]

today = date.today()
random.seed(today.toordinal())

daily_question = random.choice(array_questions)

print("Today's Array Practice Question:")
print(daily_question)