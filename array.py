# 1 largest elemet in array

# arr=[1,211,34,56,78,100]
# max=0
# for c in arr:
#     if c>max:
#         max=c
# print(max)

# 2 Find Second Smallest Element in an Array

# arr=[1,5,10,2,1,]
# s=arr[0]
# ss= arr[1]
# if s>ss:
#     s,ss=ss,s
# for i in range(2,len(arr)):
#     if arr[i]<s:
#         s=arr[i]
#         ss=s
#     elif arr[i]<ss and arr[i]!=s:
#         ss=arr[i]
# print(ss)


# 3 reverse an array

# arr=[1,2,3,4,5]
# s=0
# e=4
# while s<e:
#     arr[s],arr[e]=arr[e],arr[s]
#     s+=1
#     e-=1
# print(arr)


# 4 Find second largest number in a list

# arr=[12,61,15,13,20,61]
# c=0
# for _ in arr:
#     c+=1
# l=arr[0]
# sl=arr[1]
# if l>sl:
#     l,sl=sl,l
# for i in range(1,c):
#     if arr[i]>l:
#         sl=l
#         l=arr[i]
        
#     elif arr[i]>sl and arr[i]!=l:
#         sl=arr[i]

# print(sl)
# print(l)


# 29/
# 5 selection,asc,dec

# arr=[2,5,6,1,3]
# for i in range(len(arr)-1):
#     m=i
#     for j in range(m+1,len(arr)):
#         if arr[m]<arr[j]:
#             m=j
#     arr[m],arr[i]=arr[i],arr[m]
# print(arr)

# 6 asc,des
# a=[2,3,56,1]
# c=0
# for i in a:
#     c+=1

# h=c//2
# l=a[:h+1]

# r=arr[h+1:]

# 7 freq elements

# arr=[10,2,3,5,10,5,5]
# d={}
# for i in arr:
#     if i in d:
#         d[i]+=1
#     else:
#         d[i]=1

# for k in d:
#     print(k,d[k])


# 30 palindrome array

# 8 repeating elemet in array

# arr=[1,3,4,1,5,3,5,9,7]
# f={}
# for i in arr:
#     if i in f:
#         f[i]+=1
#     else:
#         f[i]=1

# for j in f:
#     if f[j]<=1:
#         print(j)

# 9 remove duplicates from array

# arr=[2,1,4,6,1,4]
# u=[]
# for i in arr:
#     if i in u:
#         break
#     else:
#         u+=[i]
# print(u)

# 31
# 10 count even and odd elements in array
# arr = [11, 20, 35, 40, 53]
# e=0
# o=0
# for i in arr:
#     if i%2==0:
#         e+=1
#     else:
#         o+=1
# print(e,o)

# 11 symetric pairs in array

# arr=[(1, 2), (3, 4), (2, 1), (5, 6), (4, 3),]
# r=[]
# c=0
# for i in arr:
#     c+=1

# for j in range(c):
#     a,b=arr[j]
#     for k in range(j+1,c):
#         cc,d=arr[k]
#         if a==d and b==cc:
#             r+=[(a,b)]
# print(r)


# 12 maximum product in a given array

# arr=[ 1, -2, -3, 0, 7, -8, -2 ]
# mp=0
# c=0
# for i in arr:
#     c+=1

# for j in range(c):
#     d=arr[j]
#     for k in range(j+1,c):
#         e=arr[k]
#         p=d*e
#         if p>mp:
#             mp=p
# print(mp)

# 13 rotation of array

# left
# arr=[1,2,3,4,5]
# r=3

# for i in range(r):
#     t=arr[0]
#     for j in range(1,len(arr)):
#         arr[j-1]=arr[j]

#     arr[-1]=t
# print(arr)

# right
# arr=[1,2,3,4,5]
# r=3

# for i in range(r):
#     t=arr[-1]
#     for j in range((len(arr)-1),0,-1):
#         arr[j]=arr[j-1]
#     arr[0]=t
# print(arr)



# 14 repeated nbr indiies
# arr=[2,2,3,2,2,3]
# c=0
# for i in arr:
#     c+=1

# h=c//2
# p=[]

# for i in range(c):
#     num=arr[i]
#     if num in p:
#         continue

#     cc=0
#     for j in range(c):
#         if num==arr[j]:
#             cc+=1

        
#     if cc>h:
#         print(num,end=" ")
#         for k in range(c):
#             if arr[k]==num:
#                 print(k,end="")

#     p+=[num]

# 15 3rd largest element
# arr=[2,3,5,1,4]
# for i in range(len(arr)):
#     p=i
#     for j in range(i+1,len(arr)):
#         if arr[j]<arr[p]:
#             p=j

#     arr[i],arr[p]=arr[p],arr[i]

# print(arr)
# print(arr[-3])



# 16 palindrome in list


# l=[121,34,67,87,153,9474]
# for num in l:
#     temp=num

#     c=0
#     while temp>0:
#         c+=1
#         temp=temp//10

#     temp=num
#     s=0
#     while temp>0:
#         d=temp%10
#         s+=d**c
#         temp=temp//10

#     if s==num:
#         print("palindrome")


# # 17 7.	Average of positive and negative numbers separately.

# l=[1,3,-3,4,-8]
# pl=[]
# nl=[]

# for i in l:
#     if i >=0:
#         pl+=[i]

#     else:
#         nl+=[i]

# plen=0

# for j in pl:
#     plen+=1

# nlen=0

# for k in nl:
#     nlen+=1
# ps=0
# for l in pl:
#     ps+=l

# ns=0

# for p in nl:
#     ns+=p

# print(ps//plen,ns//nlen)


# 18 amicable pairs

# def divi(n):
#     if n <= 1:
#         return 0
#     ds = 1
#     for i in range(2, n):
#         if n % i == 0:
#             ds += i
#     return ds

# def amicable(num):
#     p = []
#     n = len(num)

#     for i in range(n):
#         for j in range(i+1, n):
#             a = num[i]
#             b = num[j]

#             if a == b:
#                 continue

#             sa = divi(a)
#             sb = divi(b)

#             if sa == b and sb == a:
#                 p += [(a, b)]
#     return p

# numbers = [220, 284, 1184, 1210, 300, 400]
# print("Amicable pairs:", amicable(numbers))


# 19 Reverse the list without using another array (in-place swap).


# arr=[1,2,3,4,5]
# s=0
# e=len(arr)-1
# while s<e:
#     arr[s],arr[e]=arr[e],arr[s]
#     s+=1
#     e-=1
# print(arr)

# 20 remove duplicates 

# l=[2,5,1,2,5]
# nl=[]

# for i in l:
#     if i not in nl:
#         nl+=[i]    
# print(nl)

# 21 3.	Find 2nd maximum number in an array.

# arr=[2,13,56,4]
# l=arr[0]
# sl=arr[1]

# if sl>l:
#     l,sl=sl,l

# for i in range(2,len(arr)):
#     if arr[i]>l:
#         sl=l
#         l=arr[i]
#     elif arr[i]>sl and arr[i]!=l:
#         sl=arr[i]

# print(sl)



# 22 Add two lists element-wise and handle digit-split if sum ≥ 10.

# list1 = [2, 5, 1, 8,9]
# list2 = [3, 6, 2, 4]
# r=[]
# if len(list1)>len(list2):
#     ml=len(list1)
# else:
#     ml=len(list2)

# for i in range(ml):
#     if i<len(list1):

#         n1=list1[i]

#     else:
#         n1=0

#     if i<len(list2):
#         n2=list2[i]

#     else:
#         n2=0

#     t=n1+n2

#     if t<10:
#         r+=[t]

#     else:
#         d=t%10
#         ld=t//10

#         r+=[ld]
#         r+=[d]

# print(r)

# 23 7.	Sorting by considering the first element as “size” and sorting the rest.

# arr=[5,8,75,6,3,2,1]
# op=[5, 2, 3, 6, 8, 75, 1]
# n=arr[0]
# d=arr[1:1+n]
# print(d)
# for p in range(len(d)):
#     m=p
#     for j in range(p+1,len(d)):
#         if d[m]>d[j]:
#             m=j

#     d[p],d[m]=d[m],d[p]

# r=[n]+d+arr[1+n:]
# print(r) 

# 24 subbarys problems,sum

# arr=[1,2,4]

# n=len(arr)
# sub=[]
# for i in range(n):
#     for j in range(i,n):
#         cs=[]
#         s=0
#         for k in range(i,j+1):
#             cs+=[arr[k]]
#         for l in cs:
#             s+=l
            
#         # print(s)

#         print(cs,s)


# 25 max sum of consequative number

# a=[1,2,3,1,4,6]
# ms=0
# s=[]
# for i in range(len(a)-1):
#     if a[i]+a[i+1]>ms:
#         ms=a[i]+a[i+1]
#         s+=[a[i],a[i+1]]


# print(ms)
# print(s)



#26 the given n elements in the n number of elemnts in the print the consecutive numbers in maximum of 2

# nums = [5,5,5,2,2,3,3,3,3,4]
# c=0
# p=None
# r=[]
# for x in nums:
#     if x==p:
#         c+=1
#     else:
#         c=1
#         p=x
#     if c<=2:
#         r+=[x]
# print(r)


# a=[10,20,30,40,50]
# s=0
# s2=len(a)-1
# while s<s2:
#     a[s],a[s2]=a[s2],a[s]
#     s+=1
#     s2-=1

# print(a)

a = [1, 2, 3, 4, 5,6,7,8,9,10]
k = 5

for i in range(k):
    t=a[0]
    for j in range(1,len(a)):
        a[j-1]=a[j]

    a[-1]=t
print(a)




# n=[4,4,5,1,2,5,1]
# r=[]
# for i in range(len(n)):
#     p=False
#     for j in range(i+1,len(n)):
#         if n[i]==n[j]:
#             p=True
#             break

#     if not p:
#         r+=[n[i]]

# print(r)


# a = [3, 4, 1, 2, 7, 8, 9, 3, 2]
# s=a[0]
# rest=a[1:]
# c=[]
# i=0
# while i <len(rest):
#     ch=[]
#     for j in range(s):
#         if i+j<len(rest):
#             ch+=[rest[i+j]]

#     c+=[ch]
#     i+=s

# print(c)

# arr = [1, 2, 3]
# s=[]
# for i in range(len(arr)):
#     for j in range(i,len(arr)):
#         su=[]
#         for k in range(i,j+1):
#             su+=[arr[k]]

#         s+=[su]

# print(s)
