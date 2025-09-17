# n = 3
# for i in range(1, n + 1):           # 1..n
#     if i == 1:
#         print(1)
#     else:
#         print(i - 1, i)
# # 1
# 1 2
# 2 3


# Question 2 – Hidden Digit Sum

# s="a3x5b7y11"
# a=""
# for i in s:
#     if '0'<=i<="9":
#         a+=i

# print(a)
# d=0
# for j in a:
#     d+=ord(j)-ord("0")

# print(d)

# 35711
# 17

# Question 3 – Alternating Case Counter

# s="aBcDxyZ"
# c=0

# for i in range(len(s)):
#     if 'a'<=s[i]<='z' and 'A'<=s[i+1]<="Z":
#         c+=1
#         print(s[i],s[i+1])
# print(c)

# a B
# c D
# y Z
# 3


# Question 4 – Digit Rotation Check

# n1=1234
# t=n1
# n2=43216
# d=0

# while n1>0:
#     e=n1%10
#     d=d*10+e
#     n1//=10
# if d==n2:
#     print("same")
# else:
#     print("not")
# print(d)


# Question 5 – Digit Sum Persistence

# def digit_sum(n):
#     s = 0
#     while n > 0:
#         d = n % 10
#         s += d
#         n //= 10
#     return s

# def persistence(n):
#     steps = 0
#     while n >= 10:          # more than one digit
#         n = digit_sum(n)    # replace with sum of digits
#         steps += 1
#     return steps, n         # steps and the final single digit

# # Example
# num = 999
# count, final_digit = persistence(num)
# print("Iterations:", count)
# print("Final digit:", final_digit)


# Days to Next Birthday
# from datetime import date,datetime,timedelta
# dd="2003-11-07"
# t=datetime.today()
# c=datetime.strptime(dd,"%d-%m-%Y")

# by=t.year-c.year
# bm=t.month-c.month
# bd=t.day-c.day

# if bd==0:
#     print("happy birthday")
# else:
#     if(t.year%4==0 and t.year%100!=0) or (t.year%400==0):


# Question – Longest Even-Odd Alternating Subarray

# a=[3,4,5,6]
# for i in range(len(a)):
#     for j in range(i+1,len(a)):
#         s=[]
#         for k in range(i,j):
#             s+=[a[k]]
#         print(s)







# asked questions

# # happy nbrs


# def happy(n):
#     s=0
#     while n>0:
#         d=n%10
#         s+=d*d
#         n//=10

#     return s

# n=19
# r=n
# while n!=1 and n!=4:
#     n=happy(n)

# if n==1:
#     print("happy")
# else:
#     print("not")


# 2 count divisior of nbr

# n=16
# c=0
# for i in range(1,n+1):
#     if n%i==0:
#         c+=1

# print(c)

# 3 return nearest smallest nbr and if not replace larger or equal number with -1

# a=[4,5,2,10,8]
# r=[]

# for i in range(len(a)):
#     f=-1
#     j=i-1
#     while j>=0:
#         if a[j]<a[i]:
#             f=a[j]
#             break
#         j-=1

#     r.append(f)

# print(r)
# [-1, 4, -1, 2, 2]

# 4 sum of odd digits in a number

# n=1435
# s=0

# while n>0:
#     d=n%10
#     if d%2!=0:
#         s+=d

#     n=n//10
# print(s)

# 5 3 numbers n,l and r ,print yes if n is between l and r

# n=15
# l=1
# u=8

# if l<=n<=u:
#     print("yes")

# else:
#     print("no")

# 6 find min element in array
# a=[2,45,6,12,11]
# m=a[0]
# for i in a:
#     if i<m:
#         m=i

# print(m)

# 7 print true if given array is sequential order

# a=[1,12,13,14,19,3]

# for i in range(len(a)-1):
  
#     f=False
#     if a[i]<a[i+1]:
#         f=True

#     else:
#         f=False
#         break

# if f:
#     print(True)
# else:
#     print(False)

# 8 duplicates in a array

# a=[1,3,5,1,3,7,1]
# d={}
# for i in a:
#     if i in d:
#         d[i]+=1

#     else:
#         d[i]=1

# for k in d:
#     if d[k]>1:
#         print(k,d[k],end=" ")

#   9 index value equal to array value
# a=[0,1,2,38,4]

# for i in range(len(a)):
#     if i ==a[i]:
#         print(True)
#     else:
#         print(False)

# 10 binary to decimal

# b="1111"
# de=0
# p=0

# for c in b:
#     if c=="1":
#         d=1
#     else:
#         d=0
#     de=de*2+d
# print(de)

# composite number
# Composite number → more than 2 divisors.

# n=12
# c=0
# for i in range(1,n+1):
#     if n%i==0:
#         c+=1

# if c>2:
#     print("composite")

# else:
#     print("no")


# reverse a string words
# s="hello word,here"
# ns=""
# r=""
# for i in s+" ":
#     if i!=" ":
#         ns+=i

#     else:
#         r+=ns[::-1]+" "
#         ns=" "

# # print(ns)
# print(r)


s = "hello,word here now "
ns = ""
r  = ""

for ch in s:
    if ('a' <= ch <= 'z') or ('A' <= ch <= 'Z'):
        ns += ch                 # build the current word
    else:
        # reverse the letters manually
        j = len(ns) - 1
        while j >= 0:
            r += ns[j]
            j -= 1
        ns = ""                  # reset for next word
        r += ch                  # keep the separator as-is

# flush any remaining letters after the loop
# j = len(ns) - 1
# while j >= 0:
#     r += ns[j]
#     j -= 1

print(r)





        

# return last word 
# s="hello word"
# ns=""
# r=[]
# for i in s+" ":
#     if i!=" ":
#         ns+=i

#     else:
#         r+=[ns]
#         ns=" "

# # print(ns)
# print(r[-1])
        
