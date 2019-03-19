"""
Task

You are given a string .
Your task is to find out if the string  contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.

Input Format

A single line containing a string .

Output:

In the first line, print True if  has any alphanumeric characters. Otherwise, print False.
In the second line, print True if  has any alphabetical characters. Otherwise, print False.
In the third line, print True if  has any digits. Otherwise, print False.
In the fourth line, print True if  has any lowercase characters. Otherwise, print False.
In the fifth line, print True if  has any uppercase characters. Otherwise, print False.

"""

if __name__ == '__main__':
    s = raw_input()
    list(s)
    call = False
    for x in range(0, len(s)):
        if s[x].isalnum() == True:
            call = True
    print (call)
    call = False

    for x in range(0, len(s)):
        if s[x].isalpha() == True:
            call = True
    print (call)

    call = False
    for x in range(0, len(s)):
        if s[x].isdigit() == True:
            call = True
    print (call)
    call = False
    for x in range(0, len(s)):
        if s[x].islower() == True:
            call = True
    print (call)
    call = False
    for x in range(0, len(s)):
        if s[x].isupper() == True:
            call = True
    print (call)
