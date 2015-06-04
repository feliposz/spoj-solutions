"""SPOJ Problem Set (classical)

5. The Next Palindrome

Problem code: PALIN

A positive integer is called a palindrome if its representation in the decimal system is the same when read from left to right and from right to left. For a given positive integer K of not more than 1000000 digits, write the value of the smallest palindrome larger than K to output. Numbers are always displayed without leading zeros.

Input

The first line contains integer t, the number of test cases. Integers K are given in the next t lines.

Output

For each K, output the smallest palindrome larger than K.

Example

Input:
2
808
2133

Output:
818
2222

Warning: large Input/Output data, be careful with certain languages
"""

def reverse(s):
    return s[::-1]

def isPalindrome(s):
    return s == s[::-1]

def reverseCompare(s, r):
    i = -1
    for c in s:
        if c < r[i]:
            return -1
        if c > r[i]:
            return 1
        i -= 1
    return 0

def nextPalindromeNEW(s):
    size = len(s)
    mid = size // 2
    if size % 2 == 1:
        start = s[0:mid]
        middle = s[mid]
        end = s[mid + 1:]
    else:
        start = s[0:mid]
        middle = ""
        end = s[mid:]
    end = reverse(end) # not really an improvement
    if start < end:
        if middle == "":
            start = str(int(start) + 1)
        elif middle == "9":
            middle = "0"
            start = str(int(start) + 1)
        else:
            middle = str(int(middle) + 1)
    elif start == end:
        return nextPalindrome(str(int(s) + 1))
    return start + middle + reverse(start)

def nextPalindromeOLD(s):
    size = len(s)
    mid = size // 2
    if size % 2 == 1:
        start = s[0:mid]
        middle = s[mid]
        end = s[mid + 1:]
    else:
        start = s[0:mid]
        middle = ""
        end = s[mid:]
    end = end[::-1]
    if start < end:
        if middle == "":
            start = str(int(start) + 1)
        elif middle == "9":
            middle = "0"
            start = str(int(start) + 1)
        else:
            middle = str(int(middle) + 1)
    elif start == end:
        return nextPalindrome(str(int(s) + 1))
    return start + middle + start[::-1]

def nextPalindrome(n):
    n += 1
    while True:
        s = str(n)
        if s == s[::-1]:
            return s
        n += 1

def main():
    tests = int(input())
    for _ in range(tests):
        s = input()
        print(nextPalindromeOLD(s))
