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

#pattern using while loop:

n=1
a=5
while  n<=5:
    print('*'*n)
    n+=1