# # 1 Python Program for checking a character is a vowel or consonant

# manually reverse ns without built-in slicing
        # rev = ""
        # j = len(ns) - 1
        # while j >= 0:
        #     rev += ns[j]
        #     j -= 1

# def check_char(c):
#     vowels = ['a','e','i','o','u','A','E','I','O','U']
#     if c in vowels:
#         print("Vowels")
#     else:
#         print("consonants")

# check_char("a")


# def check_vowel_or_consonant(ch):
#     # Convert uppercase to lowercase manually
#     if ch >= 'A' and ch <= 'Z': 
#         ch = chr(ord(ch) + 32)   # Example: 'A'(65) -> 'a'(97)

    
#     if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
#         return "Vowel"
#     else:
#         return "Consonant"


# ch = input("Enter a character: ")


# # 2 Check if a character is an alphabet or not

# def alp(c):
#     if c>="A" and c<="Z":
#         return "Alpha"
#     elif c>="a" and c<="z":
#         return "alpha"
#     else:
#         return "Not "
    
# #3 Length of the string without using strlen() function 

# def lens(s):
#     c=0
#     for i in s:
#         c+=1
#     return c


# 4 program to toggle each character in a string


# s="d4eepa"
# r=""
# for i in s:
#     if i>="A" and i<="Z":
#         r+=chr(ord(i)+32)

#     elif i>="a" and i<="z":
#         r+=chr(ord(i)-32)

# print(r)

# 5 Remove the vowels from a String 

# s="Deepa"
# llc=""
# for c in s:
#  lc=""
#  if c>="A" and c<="Z":
#   lc+=chr(ord(c)+32)
#  else:
#   lc+=c
#  if not(lc=="a"or lc=="e"or lc=="i" or lc=="o" or lc=="u"):
#   llc+=lc
# print(llc)

# 6 palindome

# s='eaiae'
# l=0
# c=0
# for i in s:
#     #  print(i)
#      c+=1
# print(c)
# r=c-1
# p=True
# while l<r:
#      if s[l]!=s[r]:
#           p=False
#           break
#      l+=1
#      r-=1

#      p=True
# if p:
#      print("yes")
# else:
#      print("no")



# 30

# 7 reverse string

# s="hello world"
# r=""
# c=0
# for i in s:
#      c+=1

# for i in range(0,c):
#      r+=s[c-i-1]

# print(r)

# 8 remove other char

# s="sdeepa0711@gmail.com"
# n=""

# for i in s:
#     if (ord(i)>=65 and ord(i)>=95) or( ord(i)>=97 and ord(i)<=122):
#         n+=i
# print(n)

# 9 1st and last uppper in string word

# s="Deepa selvakumar"
# c=0
# r=""
# w=""
# for i in s:
#     c+=1

# i=0
# while i<c:
#     if s[i]!=" ":
#         w+=s[i]

#     else:
#         wl=0
#         for i in w:
#             wl+=1

#         for j in range(wl):
#             if j==0 or j==wl-1:
#                 if w[j]>="a" and w[j]<="z":
#                     r+=chr(ord(w[j])-1)
#                 else:
#                     r+=w[j]
#             else:
#                 r+=w[j]
#         r+=" "
#         word=""
# i+=1
# print(r)

# 10 anagram check
# s1 = "silent"
# s2 = "listen"

# # Step 1: Check length
# if len(s1) != len(s2):
#     print("Not an anagram")
# else:
#     # Step 2: Make frequency counters
#     freq1 = {}
#     freq2 = {}

#     # Count frequency of each character in s1
#     for ch in s1:
#         if ch in freq1:
#             freq1[ch] += 1
#         else:
#             freq1[ch] = 1
    
#     # Count frequency of each character in s2
#     for ch in s2:
#         if ch in freq2:
#             freq2[ch] += 1
#         else:
#             freq2[ch] = 1
    
#     # Step 3: Compare frequencies
#     if freq1 == freq2:
#         print("Anagram")
#     else:
#         print("Not an anagram")


#11 replace string 
# s="pythonlon"
# f="on"
# r="hen"
# op=""

# fc=0
# for i in f:
#     fc+=1

# sl=0
# for j in s:
#     sl+=1

# ii=0
# while ii<sl:

#     if s[ii:ii+fc]==f:
#         op+=r
#         ii+=fc
#     else:
#         op+=s[ii]
#         ii+=1
# print(op)



# 12 replace word
# s="i love"
# r="jesus"
# o="i"

# w=[]
# ww=""

# for c in s:
#     if c!=" ":
#         ww+=c
#     else:
#         w+=[ww]
#         ww=""
# w+=[ww]

# for i in range(len(w)):
#     if w[i] == o:
#         w[i]=r
# print(len(w))
# r=''
# for j in range(len(w)):
#     r+=w[j]
#     if j !=len(w)-1:
#         r+=" "

# print(r)


# 13 expand the characters

# s="cat"
# ns="c"
# for i in range(1,len(s)):
#     ns+=((i+1)*s[i])

# print(ns)


# s="a2b3c4"
# r=""
# i=0
# n=0
# for j in (s):
#     n+=1

# while i<n:
#     ch=s[i]
#     i+=1
#     c=0
#     while i<n and "0"<=s[i]<="9":
#         c=c*10+(ord(s[i])-ord("0"))
#         i+=1
#     print(c)
#     if c==0:
#         c=1

#     for k in range(c):
#         r+=ch

# print(r)


# 14 rotate words

# w="hello"
# t=2
# l=len(w)
# ch=[]

# for i in range(l):
#     ch+=[w[i]]

# # for j in range(t):
# last=ch[l-1]
# for k in range(l-1,0,-1):
#     ch[k]=ch[k-1]
# ch[0]=last

# r=""
# for rr in range(l):
#      r+=ch[rr]
# print(r)
     


# 15 plaindrome in a string

# s="madam is level racecar fast"
# ns=""
# l=len(ns)
# for c in s+" ":
#     if c!=" ":
#         ns+=c
#     else:
#         i=0
#         j=l-1
#         p=True
#         while i<j:
#             if ns[i]!=ns[j]:
#                 p=False
#                 break

#             i+=1
#             j-=1
    
#         if p and ns!="":
#             print(ns,end=" ")
#         ns=""

        


# 16 6.	Print word with consecutive vowels.

# s = "I am seing a queue in cpoe"

# w=""
# v='aeiouAEIOU'
# for i in s+" ":
#     if i !=" ":
#         w+=i
#     else:
#         vv=False
#         for j in range(len(w)-1):
#             if w[j]  in v and w[j+1] in v:
#                 vv=True
#                 break

#         if vv:
#             print(w)

#         w=""

# 17 7.	"s='hello good morning'", search "ni" → 'morning'".


# s='helilon goonid morning'
# search="ni"
# w=""
# for i in s+" ":
#     if i !=" ":
#         w+=i

#     else:
#         if search in w:
#             print(w)
#         w=" "


# 18 8.	Remove duplicates from a string/list.

# s="Deepaa"
# ss=""

# for i in s:
#     if i not in ss:
#         ss+=i

# print(ss)

# 19 9.	A=1, B=2, ...Z=26 mapping program.

# a="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# s="aab"
# cc=""
# for c in s:
#         if ord(c)>=97 and ord(c)<=122:
#             cc+=chr(ord(c)-32)
#         else:
#              cc+=c

# for i in cc:
#         p=0
#         for j in range(len(a)):
#             if i == a[j]:
#                 p=j+1
#                 break
#         print(i,p)

# 20 From {syncfusion}, given chars s,f remove them → output ycn.

# s="syncfusion"
# c="f"
# c2="s"
# ns=""

# i=0
# n=len(s)

# while i <n:
#     if s[i]!=c and s[i]!=c2:
#         ns+=s[i]
#     i+=1

# print(ns)


# # 21 remove ch from a string
#Remove character in case-sensitive manner →
# ip: syncfusion, S
# op: yncfuhion


# 22 print successive repeated letters in words of a sentence.

# s="Hello success"
# ns=""

# for i in s+" ":
#     if i!=" ":
#         ns+=i

#     else:
#         for j in range(len(ns)-1):
#             if ns[j]==ns[j+1]:
#                 print(ns[j])

#         ns=""


# 23 Generate all substrings from a given string.

# s="abc"

# for i in range(len(s)):
#     for j in range(i,len(s)):
#         ss=""
#         for k in range(i,j+1):
#             ss+=s[k]
#         print(ss)


# 24 how to convert string words into list without any builtin methods

# s="A geek in need is a geek indeed"
# sub="geek"
# ns=""
# l=[]

# for i in s+" ":
#     if i !=" ":
#         ns+=i
#     else:
#         l+=[ns]
#         ns=""

# print(l)


# 25 validate codes,in a phonr nbr


# old_code = "+91"
# new_code = "+44"
# phone = "+91-9876543210"

# p=""
# i=0
# while i < len(phone) and phone[i]!="-":
#     p+=phone[i]
#     i+=1
# print(p)
# print(i)
# if p==old_code:
#     # i+=1
#     r=new_code
#     while i<len(phone):
#         r+=phone[i]
#         i+=1
#     print(r)
# else:
#     print("Invalid or different code. No change.")



# 24 snake to pascalcase

# s = "hello_word_example"
# result = ""

# i = 0
# while i < len(s):
#     ch = s[i]
#     if i == 0:
#         # First letter uppercase
#         result += chr(ord(ch) - 32) if 'a' <= ch <= 'z' else ch
#     elif ch == "_":
#         if i + 1 < len(s) and 'a' <= s[i + 1] <= 'z':
#             result += chr(ord(s[i + 1]) - 32)
#             i += 1      # skip the next character, already processed
#     else:
#         result += ch
#     i += 1

# print(result)   # HelloWordExample



# 1 manual lenth
# s="Deepa selvakumar"
# l=0
# for i in s:
#     l+=1

# print(l)

# 2 vowels and consonatns
# v="aeiouAEIOU"
# vc=0
# cc=0

# for i in s:
#     if i in v:
#         vc+=1
#     else:
#         cc+=1

# print(vc,cc)


# 3 reverse string 
# ns=""
# l=0
# for i in s:
#     l+=1
# for i in range(l-1,-1,-1):
#     ns+=s[i]

# print(ns)

# arr = [1, 2, 3,4]

# for i in range(len(arr)):
    
#     for j in range(i,len(arr)):
#         s=[]
#         for k in range(i,j+1):
#             s+=[arr[k]]
#         print(s)
#     print(i,"iteration")

