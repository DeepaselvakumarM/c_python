# 1 hcf/gcd
# HCF(a, b) = HCF(b, a % b) is a property from number theory.

# It reduces the problem size in each step → very efficient.

# a=10
# b=24

# while b!=0:
#     t=a%b
#     a=b
#     b=t
# print(a)

# 2 lcm
# LCM(a,b)=HCF(a,b)a×b​

# def hcf(a, b):
#     while b != 0:
#         temp = a % b
#         a = b
#         b = temp
#     return a

# Function to find LCM using HCF
# def lcm(a, b):
#     return (a * b) // hcf(a, b)

# 3 For the number of handshakes to be maximum, every person should handshake with every other person in the room i.e. all persons present should shake hands.


# Person 1 shakes hands with 4 others (people 2,3,4,5)

# Person 2 shakes hands with 3 others (people 3,4,5) - already shook with person 1

# Person 3 shakes hands with 2 others (people 4,5)

# Person 4 shakes hands with 1 other (person 5)

# Person 5 shakes hands with 0 others (all already shook hands)

# n=5
# t=0
# for i in range(1,n):
#     t+=i
# print(t)


# 4 replace 1 in place 0

# i=1080300
# r=0
# p=1
# while i>0:
#     e=i%10
#     if e==0:
#         e=1
#     r+=(e*p)
#     p=p*10
#     i=i//10
# print(r)


# profit,loss
# 5 adittion fraction

# 30



#6 prime nbr bw 1 to 100
# for i in range(2,100+1):
#     for j in range(2,i):
#         if(i%j)==0:
#             break
#     else:
#         print(i)


# for n in range(2,101):
#     p=True
#     # r=n**0.5
#     # i=r%10
#     i=n//2

#     for j in range(2,i+1):
#         if n%j==0:
#             p=False
#             break
#     if p:
#         print(n,end="")

# for n in range(2, 101):   # numbers from 2 to 100
#     p = True

#     # Step 1: Find integer square root manually (without int(), sqrt(), etc.)
#     k = 1
#     while k * k <= n:   # keep increasing until square exceeds n
#         k += 1
#     k -= 1              # adjust back to last valid value

#     # Step 2: Check divisibility up to k
#     j = 2
#     while j <= k:
#         if n % j == 0:   # divisible -> not prime
#             p = False
#             break
#         j += 1

#     # Step 3: Print if prime
#     if p:
#         print(n, end=" ")


# 7 Calculate the number of digits in an integer

# i=12654845
# c=0
# while i>0:
#     i=i//10
#     c+=1
# print(c)

# 31

# 8 nbr days in a month

# m=2
# y=2004

# if m in [1,3,5,7,8,10,12]:
#     print(31)
# elif m in [5,9,11]:
#     print(30)

# if (m==2 and y%4==0) or (y%100==0 and y%400==0):
#     print(29)
# else:
#     print(28)


# 9  automorphic nbr

# n=76
# t=n
# nl=0
# while n>0:
#     nl+=1
#     n=n//10
    
# s=t**2
# r=0
# e=s%(10**nl)
# print(e)
# print(s)
# if e==t:
#     print("automorphic")


# 10 fibonacci series 

# n=7
# a=0
# b=1
# print(a,b, end=" ")

# for i in range(2,n):
#     c=a+b
#     print(c,end=" ")
#     a=b
#     b=c

# 11 fraction add,div


# def gcd(a,b):
#     while b!=0:
#         t=b
#         b=a%b
#         a=t
#     return a

# def lcm(a,b):
#     r=(a*b)//gcd(a,b)
#     return r


# def add(n1,d1,n2,d2):
#     cd=lcm(d1,d2)

#     f1=cd//d1
#     num1=n1*f1

#     f2=cd//d2
#     num2=n2*f2

#     print(f"{num1}/{cd} + {n2}/{cd}")

#     r=num1+num2

#     print(f"{r}/{cd}")

#     cg=gcd(r,cd)
#     r=r//cg
#     rd=cd//cg

#     return r,rd


# c=add(1,2,3,4)
# print(c)


# 13 hyperfactorial

# H(4) = 1¹ × 2² × 3³ × 4⁴ = 1 × 4 × 27 × 256 = 27,648
# n=4
# h=1
# for i in range(1,n+1):
#     h*=i**i
# print(h)


# 14 jumpled nbr

# n=122
# # t=121
# c=0
# j=[]
# while n>0:
#     d=n%10
#     j+=[d]
#     n=n//10
# r=j[::-1]
# v=True
# for i in range(len(j)-1):
   
#     a=j[i]
#     b=j[i+1]
#     if a >b:
#         diff=a-b
#     else:

#         diff=b-a

#     if diff!=1:
#        v=False
# if v:
#     print("valid nbr")
# else:
#     print("not valid")
    

# 15 factor nbr

# n=12

# for i in range(1,n+1):
#     if n%i==0:
#         print(i,end=" ")



# 16 sum of subarray

# 17 harshed nbr
# Definition: A Harshad number (or Niven number) is a number that is divisible by the sum of its digits.

# n=18
# t=n
# s=0
# while n>0:
#     d=n%10
#     s+=d
#     n=n//10
# if t%s==0:
#     print("harshed nbr")
# else:
#     print("no")


# 18 armstrong nbr

# n=12
# t=n

# l=0
# while n>0:
#     l+=1
#     n=n//10
# i=t
# s=0
# while i>0:
#     d=i%10
#     s+=d**l
#     i=i//10

# if s==t:
#     print("Armstrong nbr")
# else:
#     print("not")


# 19 sum of consqetive subarray

# arr=[1,2,3]

# for i in range(len(arr)):
#     s=0
#     for j in range (i,len(arr)):
#         s+=arr[j]
#         print(s)

# 20 perfect square root range
# Instead of checking every number between 10 and 50,
# look for the integers whose squares land inside the range.

# r1=10
# r2=20

# s=1
# while s*s<r1:
#     s+=1

# e=1
# while e*e<=r2:
#     e+=1
# e-=1

# print(e-s+1)

# nbr
# n=25
# i=1
# while i*i<=n:
#     if i*i==n:
#         print(i)
#     i+=1



# 21 Special square split check:
# ip: 55
# 55^2 = 3025 → split as 30 and 25 → 30+25 = 55 → true

# num=55
# t=num
# c=0
# while num>0:
#     c+=1
#     num=num//10
#     # print(num)

# p=t**c
# print(p)


# d=10**c
# rp=p%d
# lp=p//d

# s=rp+lp

# if s==t:
#     print(True)
# else:
#     print(False)


# 22 factorial


# n=7
# r=1
# if n<0:
#     print("not be zero")
# else:
#     for i in range(1,n+1):
#         r*=i

# print(r)
# Factorial → count of trailing zeros (ignore other zeros, replace negative with 1).
# A trailing zero is produced every time the product has a factor of 10.

# 10 = 2 × 5.
# 5’s limits how many 10’s we can form.

# Zeros come from 10 = 2×5.

# Count factors of 5 across 1..n.

# n=6
# if n<0:
#     print(1)

# fact=1
# for i in range(1,n+1):
#     fact*=i

# c=0
# while n>=5:
#     n//=5
#     c+=n

# print(fact,c)






# 23 coprime
# Two numbers are coprime (or relatively prime) if their Greatest Common Divisor (GCD) is 1. This means they have no common prime factors.


# def gcd(a,b):
#     while b!=0:
#         t=b
#         b=a%b
#         a=t

#     return a 

# def coprime(a,b):
#     g=gcd(a,b)

#     if g>1:
#         print("no coprime")

#     else:
#         print("coprime")
# num=8
# b=15
# coprime(num,b)


# 24 happy brs

# A number is called happy if, after repeatedly replacing it with the sum of the squares of its digits, we eventually reach 1. If we enter an infinite loop that doesn't include 1, the number is unhappy.



# def sumof(n):
#     t=0
#     while n>0:
#         d=n%10
#         t=t+d*d
#         n=n//10
#     return t

# n=13
# res=n
# while res!=1 and res!=4:
#     res=sumof(res)
# if res==1:
#     print("happy nbr")
# else:
#     print("not happy")
   

# 25 integer to roman

# def integer(n):
#     values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
#     symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
#     roman=""
#     i=0

#     while n>0:
#         d=n//values[i]
#         n=n%values[i]
#         while d:
#             roman=roman+symbols[i]
#             d=d-1

#         i=i+1
#     return roman

# n=14
# print(integer(n))


# 26 simple interest
# a=10000
# y=2
# i=3

# si=a*y*i/100
# print(si)
# t=si+a
# print(t)

# 27 compount interest

# a=10000
# y=2
# i=10
# ci=a*((1+i/100)**y-1)
# print(ci)


# perfect square range

# l=10
# h=30
# c=0
# n=1
# sq=[]
# while True:
#     s=n*n
#     if s>h:
#         break
#     elif s>=l:
#         sq+=[s]
#         c+=1
#     n+=1

# print(c)
# print(sq)


# 28 expand the number

n=425
p=1
r=[]
while n>0:
    d=n%10
    r+=[d*p]
    p=p*10
    n=n//10

for i in range(len(r)-1,-1,-1):
    end = " + " if i != 0 else "\n"
    print(r[i],end=end)

print(r)

