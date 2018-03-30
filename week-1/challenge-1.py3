# Challenge Title: Sum of Two Digits

# Challenge: Compute the sum of two single digit numbers.
# Input: Two single digit numbers on the same line separated by a space.
# Output: The sum of these numbers.
# Constraints: These two numbers are both equal to or between 0 and 9.

user_input = input()
num1, num2 = user_input.split()
print(int(num1) + int(num2))
