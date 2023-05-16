#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Problem 1
# Print Hello, World! to stdout.

print("Hello, World!")


# In[2]:


# Problem 2
# Given an integer,n, perform the following conditional actions:

# If n is odd, print Weird
# If n is even and in the inclusive range of 2 to 5, print Not Weird
# If n is even and in the inclusive range of 6 to 20, print Weird
# If n is even and greater than 20, print Not Weird

n=int(input())
if(n%2==0):
    if(n>=2 and n<=5):
        print("Not Weird")
    if(n>=6 and n<=20):
        print("Weird")
    else:
        print("Not Weird")
else:
    print("Weird")


# In[5]:


# Problem 3
# Task
# The provided code stub reads two integers from STDIN, a and b. Add code to print three lines where:
# 1. The first line contains the sum of the two numbers.
# 2. The second line contains the difference of the two numbers (first - second).
# 3. The third line contains the product of the two numbers.

a=int(input())
b=int(input())
print(a+b)
print(a-b)
print(a*b)


# In[6]:


# Problem 4
# Task
# The provided code stub reads two integers, a and b, from STDIN.
# Add logic to print two lines. The first line should contain the result of integer division,  // . The second line should contain the result of float division,  / .
# No rounding or formatting is necessary.

a=int(input())
b=int(input())
print(a//b)
print(a/b)


# In[7]:


# Problem 5
# Task
# The provided code stub reads and integer,n, from STDIN. For all non-negative integers i<n, print i^2.
 
n=int(input())
for i in range(n):
    print(i**2)


# In[9]:


# Problem 6
# Given a year, determine whether it is a leap year. If it is a leap year, return the Boolean True, otherwise return False.
# Note that the code stub provided reads from STDIN and passes arguments to the is_leap function. It is only necessary to 
# complete the is_leap function.

def is_leap(year):
    leap = False
    if(year%4==0):
        leap=True
    elif(year%100==0):
        leap=False
    elif(year%400==0):
        leap=True
    else:
        leap=False
    return leap

year = int(input())
print(is_leap(year))


# In[12]:


# Problem 7
# The included code stub will read an integer,n, from STDIN.
# Without using any string methods, try to print the following:
# 123...n

n=int(input())
for i in range(1,n+1):
    print(i,end="")


# In[14]:


# Problem 8
# Input Format
# Four integers x,y,z and n, each on a separate line.
# Print the list in lexicographic increasing order.

# Sample Input
# 1
# 1
# 1
# 2
# Sample Output
# [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]


if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    list = [];
    abc = [];
    for X in range(x+1):
        for Y in range(y+1):
            for Z in range(z+1):
                if X+Y+Z != n:
                    abc = [X,Y,Z];
                    list.append(abc);
print(list);    


# In[ ]:


# Problem 9
# Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score.
# You are given n scores. Store them in a list and find the score of the runner-up.

n = int(input())
a = list(map(int, input().split()))
a.sort()
b=set(a)
c=list(b)
c.sort()
print(c[-2])


# In[ ]:


# Problem 10
# Given the names and grades for each student in a class of N students, store them in a nested list and print the name(s) of 
# any student(s) having the second lowest grade.
# Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name 
# on a new line.

Result =[]
scorelist = []

if __name__ == '__main__':
    for i in range(int(input())):
        name = input()
        score = eval(input())
        Result+=[[name,score]]
        scorelist+=[score]
    b=sorted(list(set(scorelist)))[1] 

    for a,c in sorted(Result):
        if c==b:
            print(a)


# In[ ]:




