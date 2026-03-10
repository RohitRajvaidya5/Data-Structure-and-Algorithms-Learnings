# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.

def isPalindrome(s):
    left, right = 0, len(s) - 1

    while left < right:
        while not s[left].isalnum():
            left += 1
        while not s[right].isalnum():
            right -= 1

        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True


s = "A man, a plan, a canal: Panama"
print(isPalindrome(s))
