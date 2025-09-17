# n=15
# for i in range(2,15):
#     p=True
#     if n%i==0:
#         p=False
#         break

# if p:
#     print("prime")
# else:
#     print("not")

# prime in range

# for i in range(2,15):
#     for j in range(2,i):
#         if i%j==0:
#             break
#     else:
#         print(i,end=" ")

# plaindrome in a list

# def palindrome(n):
#     r=0
#     while n>0:
#         d=n%10
#         r=r*10+d #Shift the existing digits one place to the left (that’s multiplying by 10).
#         n//=10
#     return r

# def check(l):
#     for i in l:
#         p=palindrome(i)
#         # print(p)
#         if p==i:
#             print(i)


# l=[12,343,56,121]
# check(l)

# mirror number

# n=153
# t=n
# r=0
# p=1

# while t>0:
#     d=t%10
#     r+=d*p
#     print(r)
#     p*=10
#     r+=(d*p)
#     print(r)
#     p*=10
#     t//=10

# b=2
# p=3
# print(b**p)

# mirror letters
# s="abcxyz"
# r=""
# for c in s:
#     if 'a'<=c<='z':
#         off=ord(c)-ord('a')
#         m=chr(ord('z')-off)
#         r+=m
#     else:
#         r+=c

# print(r)

# Balanced Letters

# s="abcded"
# n=0
# for i in s:
#     n+=1

# m=n//2
# l=0
# r=0

# for i in range(n):
#     if i<m:
#         l+=1
#     elif i>m:
#         r+=1

# print(l==r)

# isogram test
# s="machine"
# ns=""

# for i in s:
#     if i >='a' and i<='z':
#         m=chr(ord(i)-32)
#         ns+=m
#     else:
#         ns+=i

# r=""
# for j in ns:
#     rr=False
#     if j not in r:
#         rr=True


# Rotate Until Palindrome
# def rotate_until_palindrome(s):
#     n = len(s)
#     for i in range(n):
#         rot = s[i:] + s[:i]
#         # manual palindrome check
#         left, right = 0, n - 1
#         is_pal = True
#         while left < right:
#             if rot[left] != rot[right]:
#                 is_pal = False
#                 break
#             left += 1
#             right -= 1
#         if is_pal:
#             return True
#     return False

# print(rotate_until_palindrome("aab"))   # True ("aba")
# print(rotate_until_palindrome("abc"))   # False


# Count how many times two consecutive even numbers occur.

# n = [2, 4, 5, 6, 8, 10, 3]
# r=[]
# for i in range(len(n)):
#     if n[i]%2==0 and n[i+1]%2==0:
#         r+=[[n[i],n[i+1]]]

# print(r)

# Count Increasing Pairs
# n = [1, 3, 2, 1, 5,6]
# c=0
# for i in range(len(n)-1):
#     if n[i]<n[i+1]:
#         c+=1

# print(c)


# moves zeroes to end

# a=[0,3,4,0,2,0,1]
# p=0
# for i in range(len(a)):
#     if a[i]!=0:
#         a[p]=a[i]
#         p+=1
# print(p)
# while p<len(a):
#     a[p]=0
#     p+=1
# print(a)

# strong number

# n=145

# def fact(n):
#     f=1
#     for i in range(1,n+1):
#         f*=i

#     return f

# def strong(num):
#     s=0
#     t=num
#     while t>0:
#         d=t%10
#         fac=fact(d)
#         s+=fac
#         t//=10
#     if s==num:
#         print("strong")

#     else:
#         print("not")

# strong(n)

# perfect number
# n=28
# f=0
# for i in range(1,n):
#     if n%i==0:
#         f+=i

# if n==f:
#     print("perfect number")
# else:
#     print("not")

# # 
# n=9
# i=1
# while i*i<=n:
#     p=False
#     if i*i==n:
#         p=True
#     i+=1

# if p:
#     print(True)

# else:
#     print(False)