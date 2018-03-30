# Challenge Title: Maximum Pairwise Product

# Challenge: Find the maximum product of two distinct numbers in a sequence of non-negative integers.
# Input: The number of distinct numbers is on the first line. The sequence of non-negative integers is on the second line.
# Output: The maximum value that can be obtained by multiplying two different elements from the sequence, also known as the maximum pairwise product.
# Constraints: n could be equal to or betwwen 2 and 2*10^5. the individual values could be equal to or between 0 and 2*10^5.

n = int(input())
a = [int(x) for x in input().split()]

a.sort(reverse=True)

print(a[0] * a[1])
