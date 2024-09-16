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

print()


#2. Inverted Right-Angle Triangle (Stars)
""""
* * * * * 
* * * * 
* * * 
* * 
* 

"""
# 1st method

def inverted_right_triangle(a):
    for i in range(a,0,-1):
        for j in range(i):
            print('*',end="")
        print()

inverted_right_triangle(5)

print()

#second method
def inverted_right_triangle(a):
    a1=a
    a2=0
    while a>0:
        print('*'*a)
        a=a-1

inverted_right_triangle(5)

print()


# Diamond Star Pattern
""""
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * * 
* * * * 
* * * 
* * 
* 
"""

def diamond_pattern(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print('*',end=" ")
        print()
def diamond_reverse_pattern(n) :       
    for k in range(n,0,-1):
            for l in range(k):
                print('*',end=" ")
            print()
        
def combined_function(n):
    diamond_pattern(n)
    diamond_reverse_pattern(n)
combined_function(5)