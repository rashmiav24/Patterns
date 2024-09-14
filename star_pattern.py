#. Right-Angle Triangle (Stars)
"""
*
**
***
****
*****
"""

def pattern(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print('*',end="")
        print()


n = 5
pattern(n)

print()

# pattern using while loop

def pattern_w(j):
    i=1
    while i<=j:
        print('*'*i)
        i=i+1

n=5
pattern_w(n)
