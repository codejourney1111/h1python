
"""
Task:
Read an integer .

Without using any string methods, try to print the following: 123...N


Note that "." represents the values in between.
"""


from __future__ import print_function

def print_function(n):
    k=[]
    for z in range(1,n+1):
        k.append(str(z))

    k =''.join(k)
    print (k)

if __name__ == '__main__':
    n = int(raw_input())
    print_function(n)