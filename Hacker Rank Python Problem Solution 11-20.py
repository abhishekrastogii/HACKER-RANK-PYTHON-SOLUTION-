#!/usr/bin/env python
# coding: utf-8

# In[1]:


# QUESTION 11:The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students.
#             Print the average of the marks array for the student name provided, showing 2 places after the decimal.

# ANSWER 11:
n = int(input())
d= {}
for i in range(n):
    name, *num = input().split()
    s = list(map(float, num))
    d[name] = s
q= input()
b=d[q]
a=len(b)
sum=0
for i in range(a):
    sum=sum+b[i]
avg=sum/a
print(f"{avg:.2f}")


# In[ ]:


# QUESTION 12:Consider a list (list = []). You can perform the following commands:
#             insert i e: Insert integer e at position i.
#             print: Print the list.
#             remove e: Delete the first occurrence of integer e.
#             append e: Insert integer e at the end of the list.
#             sort: Sort the list.
#             pop: Pop the last element from the list.
#             reverse: Reverse the list.

# ANSWER 12:
    
N = int(input())
L=[]
for i in range(0,N):
    c=input().split();
    if c[0] == "insert":
        L.insert(int(c[1]),int(c[2]))
    elif c[0] == "append":
        L.append(int(c[1]))
    elif c[0] == "pop":
        L.pop();
    elif c[0] == "print":
        print(L)
    elif c[0] == "remove":
        L.remove(int(c[1]))
    elif c[0] == "sort":
        L.sort();
    else:
        L.reverse();


# In[4]:


# QUESTION 13:You are given a string and your task is to swap cases. In other words, convert all lowercase letters to 
#             uppercase letters and vice versa.
# ANSWER 13: 

s=input()
print(s.swapcase())


# In[ ]:


# QUESTION 14:You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.
# ANSWER 14: 
def split_and_join(line):
    line = line.split()
    line = "-".join(line)
    return line

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)


# In[ ]:


# QUESTION 15:You are given the firstname and lastname of a person on two different lines.
#         Your task is to read them and print the following:
#         Hello firstname lastname! You just delved into python.
# ANSWER 15:   

def print_full_name(x,y):
    print(f"Hello {x} {y}! You just delved into python.")
if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)


# In[ ]:


# QUESTION 16:We have seen that lists are mutable (they can be changed),
#             and tuples are immutable (they cannot be changed).
#             Let's try to understand this with an example.
#             You are given an immutable string, and you want to make changes to it.

# ANSWER 16:  

def mutate_string(string, position, character):
    string = string[:position] + character + string[(position+1):]
    return string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)


# In[ ]:


# QUESTION 17:In this challenge, the user enters a string and a substring.
#             You have to print the number of times that the substring occurs in the given string.
#             String traversal will take place from left to right, not from right to left.
# NOTE: String letters are case-sensitive.
   
# ANSWER 17:  
def count_substring(s,t):
    count=0
    a=len(s)
    b=len(t)
    for i in range(a):
        if s[i:i+b]==t:
            count+=1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)


# In[ ]:


# QUESTION 18:You are given a string S .
#             Your task is to find out if the string  contains: alphanumeric characters,
#             alphabetical characters, digits, lowercase and uppercase characters.
# ANSWER 18:

if __name__ == '__main__':
    s = input()
    print(any(map(str.isalnum, s)))
    print(any(map(str.isalpha, s)))
    print(any(map(str.isdigit, s)))
    print(any(map(str.islower, s)))
    print(any(map(str.isupper, s)))


# In[ ]:


"""QUESTION 19:Sample Input

5
Sample Output

    H    
   HHH   
  HHHHH  
 HHHHHHH 
HHHHHHHHH
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHHHHHHHHHHHHHHHHHHHHHH   
  HHHHHHHHHHHHHHHHHHHHHHHHH   
  HHHHHHHHHHHHHHHHHHHHHHHHH   
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
                    HHHHHHHHH 
                     HHHHHHH  
                      HHHHH   
                       HHH    
                        H 

ANSWER 19: """

#Replace all ______ with rjust, ljust or center. 

thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))

    


# In[ ]:


"""QUESTION 20:Sample Input

9 27
Sample Output

------------.|.------------
---------.|..|..|.---------
------.|..|..|..|..|.------
---.|..|..|..|..|..|..|.---
----------WELCOME----------
---.|..|..|..|..|..|..|.---
------.|..|..|..|..|.------
---------.|..|..|.---------
------------.|.------------

ANSWER 20: """

x,y = map(int,input().split())
items = list(range(1,x+1,2))
items = items+items[::-1][1:]
for i in items:
    text= "WELCOME" if i == x else '.|.'*i
    print (text.center(y,'-'))

