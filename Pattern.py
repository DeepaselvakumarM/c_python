
# star,number,floyrs,pascals


# 1 hollow square

# n=5
# for r in range(1,n+1):
#     for c in range(1,n+1):
#         if r==1 or r==n or c==1 or c==n:
#             print("*",end="")

#         else:
#             print(" ",end="")

#     print()

# 2 Rhombus Star Pattern

# n=5
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(" ",end="")    
#     for k in range(1,n+1):
#         print("*",end="")
    

#     print()


# 3 pyrmid 
# n=5
# for i in range(0,n):
#     for j in range(n-i):
#         print(" ",end="")    
#     for k in range(2*i-1):
#         print("*",end="")
    

#     print()


# 4 Basic Square 1 Pattern

# n=4
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(1,end="")
#     print()

# 5 floyds

# rows = 4   # number of rows you want
# num = 1    # starting number

# for i in range(1, rows + 1):
#     for j in range(i):
#         print(num, end="")  # print number in same line
#         num += 1            # increment number
#     print()  # new line after each row

# 1
# 23
# 456
# 78910


# 6 string
# s="python"
# for i in range(len(s)):
#     for j in range(i+1):
#         print(s[j] ,end="")

#     print()


# 7 numberrs

# n=5
# r=1
# for i in range(1,n+1):
#     for j in range (n):
#         print(n,end="")
#     n-=1
  
#     print()


# 8 binary triangle

# n=5

# for i in range(1,n+1):
#     for j in range(1,i+1):
#         if (i+j)%2==0:
#             print(1,end=" ")
#         else:
#             print(0,end=" ")

#     print()


# for i in range(1,n+1):
#     for j in range(n-i):
#         print(" ",end="")

#     for k in range(2*i-1):
#         if i%2==0:
#             print(1,end="")
#         else:
#             print(0,end="")

#     print()

# 1
# 01
# 101
# 0101
# 10101


# 9 Simple quiz program (MCQs, score tracking).

# print("quiz program")
# s=0
# print("1) python is a ___ language")
# print("option")
# print("a.Interpreted")
# print("b.compailer")
# a=input("enter options only")

# if a=="b":
#     print("correct")
#     s=s+1

# else:
#     print("wrong")

# print("2) What is 2 + 2 ?")
# print("a) 3")
# print("b) 4")
# print("c) 5")
# answer = input("Your answer: ")

# if answer=="b":
#      print("correct")
#      s=s+1

# else:
#     print("wrong")

# print(s)


# 10 pascals traingle

n=5
r=[[1]]
for i in range(n-1):
    p=r[-1]
    t=[0]+p+[0]
    tr=[]

    for j in range(len(t)-1):
        tr+=[t[j]+t[j+1]]
    r+=[tr]
    
for k in range(len(r)):
    for s in range(n-k):
        print(" ",end=" ")

    for num in r[k]:
        print(num,end=" ")

    print()
    
print(r)


# 11 hollow triangle

# n=5

# for i in range(1,n+1):
#     for j in range(1,i+1):
#         if j==1 or j==i or i==n:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")

#     print()

# 12 inverted traingle

# n=5

# for i in range(n,0,-1):
#     print("*"*i)
 

# 12 inverted pyrmid

# n=4

# for i in range(0,n):

#     for j in range(i):
#         print(" ",end=" ")
   
#     for k in range(2*(n-i)-1):
#         print("*",end=" ")
    

#     print()


# 13 diamond  
# n=4

# for i in range(1,n+1):
   
#     for j in range(n-i):
#         print(" ",end="")
#     for k in range(2*(i)-1):
#         print("*",end="")

    
#     print()

# for i in range(n-1,0,-1):
#     for j in range(n-i):
#         print(" ",end="")

#     for k in range(2*i-1):
#         print("*",end=""
#               )
        
#     print()


# n=4
# k=1
# for i in range(1,n+1):
#     for j in range(1,n+1):    
#         print(k,end=" ")
#         k+=1
#     print()




# n=9875
# while n>10:
#     s=0
#     t=n
#     while t>0:
#         s+=t%10
#         t=t//10 
#     n=s
# print(n)


# n1=100
# n2=999

# for n in range(n1,n2+1):  
#     t=n  
#     c=0
#     while n>0:
#         c+=1
#         n//=10
#     tt=t
#     a=0
#     while tt>0:
#         d=tt%10
#         a+=d**c
#         tt//=10

#     if  a==t:
#         print(t)

