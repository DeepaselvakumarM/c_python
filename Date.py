# 1 leap year

# y=2023
# if y%4==0:
#     if y%100==0:
#         if y%400==0:
#             print("leap year")

#         else:
#             print("not")
#     else:
#         print("leap")
# else:
#     print("not")


# 2 beginner to date & time in Python

# from datetime import datetime,date,timedelta
# d=datetime.now()
# t=date.today()
# l=t-timedelta(days=10)

# d1=date(2025, 9, 1)
# d2=date(2025, 8, 28)

# print(d)
# print((t).strftime("%A"))
# print((t).strftime("%B"))
# print(l)
# print((d1-d2).days)

# 3 number of days in a given month

# m=2
# y=2003
# if m in[1,3,5,7,8,10,12]:
#     print(31)
# elif m in[4,6,9,11]:
#     print(30)
# elif m==2 and (y%4==0 and y%100!=0) or y%400==0:
#     print(29)
# else:
#     print(28)

# 4 previous day 

# d=11
# m=1
# y=2003

# d-=1
# if d==0:
#     m-=1
#     if m==0:
#         m=12
#         y-=1
    

# print(m,y,d)


# 5 string to datime

# from datetime import datetime

# date_string = "28-08-2025 14:35:20"
# date_obj = datetime.strptime(date_string, "%d-%m-%Y %H:%M:%S")

# print(date_obj)


# 6 Write a Python program to subtract five days from the current date.

# from datetime import datetime,timedelta
# d="30-08-2025 14:35:20"
# cd=datetime.now()
# dd=cd-timedelta(days=5)

# print(cd)
# print(dd)


# 7 Write a Python program to convert the date to datetime (midnight of the date) in Python.

# import datetime

# t=datetime.datetime.today()
# print(datetime.datetime.combine(t,datetime.datetime.min.time()))

# 8 Write a Python program to print the next 5 days starting today.

from datetime import date,datetime,timedelta,time
import calendar

from dateutil.relativedelta import relativedelta

# d=date.today()
# for i in range(0,5):
#     print(d+timedelta(days=i))


# 9 Write a Python program to add 5 seconds to the current time.

# d=datetime.now()

# x=d+timedelta(0,5)

# print(d,x)

# 10 Write a Python program to convert Year/Month/Day to Day of Year in Python.

# d=date.today()
# dd=d.timetuple().tm_yday

# print(dd)


# 11Write a Python program to get the week number.
# print(date(2025,9,1).isocalendar()[1])

# 12 first monday 

# dd="2025-09-11"
# da=datetime.strptime(dd,"%Y-%m-%d").date()
# ds=da.weekday()
# print(da-timedelta(days=ds))
# print(ds)
# print(da)


# 13 1.	Calculate Age in years/months/days.

# bd=date(2003,11,7)
# t=datetime.today()

# years=t.year-bd.year
# months=t.month-bd.month
# days=t.day-bd.day

# if days<0:
#     months-=1
#     if t.month>1:
#         pm=t.month-1
#         py=t.year
#     else:
#         pm=12
#         py=t.year-1
#     dm=(date(py,pm%12+1,1)-date(py,pm,1)).days
#     days+=dm

# if months<0:
#     years-=1
#     months+=12

# print(years,months,days)







# 14 round time

# original = datetime.now()

# r=original+timedelta(minutes=30)

# rr=r.replace(minute=0,second=0,microsecond=0)

# print(rr)



# 15 3.	 Print minutes and every 5th minute print "interval".

# for minute in range(60):
#     if minute % 5 == 0:
#         print(f"{minute}: interval")
#     else:
#         print(minute)

# while True:
#     n=datetime.now()
#     m=n.minute
#     s=n.second

#     if s==0:
#         if m%5==0:
#             print(f"{n.strftime('%H:%M:%S')}-INTERVEL")

#         else:
#          print("hhhh")
#     time.sleep(1)


# 16 1.	Calculate age from DOB till today (consider leap years).


#  similar
# t=datetime.today()
# bd=date(2003,11,7)

# years=t.year-bd.year
# months=t.month-bd.month
# days=t.day-bd.day
# print(years,months,days)


# 17

# Days → 1 day = 24 * 60 * 60 = 86400 seconds

# Hours → 1 hour = 60 * 60 = 3600 seconds

# Minutes → 1 minute = 60 seconds

# Remaining → seconds

# Converting 100000 seconds:
# ========================================
# Days: 100000 // 86400 = 1
# Remaining: 13600 seconds
# Hours: 13600 // 3600 = 3
# Remaining: 2800 seconds
# Minutes: 2800 // 60 = 46
# Seconds: 40

# Final result: (1, 3, 46, 40)


# def convert_seconds_detailed(total_seconds):
#     print(f"Converting {total_seconds} seconds:")
#     print("=" * 40)
    
#     # Days
#     seconds_per_day = 24 * 60 * 60
#     days = total_seconds // seconds_per_day
#     remaining = total_seconds % seconds_per_day
#     print(f"Days: {total_seconds} // {seconds_per_day} = {days}")
#     print(f"Remaining: {remaining} seconds")
    
#     # Hours
#     seconds_per_hour = 60 * 60
#     hours = remaining // seconds_per_hour
#     remaining %= seconds_per_hour
#     print(f"Hours: {remaining} // {seconds_per_hour} = {hours}")
#     print(f"Remaining: {remaining} seconds")
    
#     # Minutes
#     seconds_per_minute = 60
#     minutes = remaining // seconds_per_minute
#     seconds = remaining % seconds_per_minute
#     print(f"Minutes: {remaining} // {seconds_per_minute} = {minutes}")
#     print(f"Seconds: {seconds}")
    
#     return days, hours, minutes, seconds

# # Test
# result = convert_seconds_detailed(100000)
# print(f"\nFinal result: {result}")



# 18 Salary per day calculation (month days considered).

# s=30000
# m=4
# if m==2:
#     y=int(input("enter the year"))
#     if (y%4==0 and y%100!=0) or (y%400==0):
#         d=29
#     else:
#         d=28

# elif m in [4,6,9,11]:
#     d=30
# else:
#     d=31

# pd=s//d

# print(pd)

# 19 Calculate Age from Birthdate

# b=date(2003,8,7)
# t=datetime.today()
# c=t.year-b.year
# if t.month<b.month:
#     c-=1
# print(b)


# 20 Find difference between two given dates (in days, months, years).
# 👉 Input: 2023-05-01 to 2025-09-06 → Output: 2 years, 4 months, 5 d

# import calendar

# y=2025
# m=2

# d=calendar.monthrange(y,m)[1]
# print(d)
# s=0

# for day in range(1,d+1):
#     if calendar.weekday(y,m,day)==6:
#         s+=1

# print(s)

# 21 Add/Subtract days, months, years from a date.

# s=date(2025,9,9)
# # print(s)
# r=s+timedelta(days=10)
# print(s+relativedelta(months=1))
# print(s+relativedelta(years=1))
# print(r)

# d1 = date(2023, 5, 1)
# d2 = date(2025, 9, 6)
# print((d2 - d1)) 


# 22 weekday name
# dd="2025-09-11"
# c=datetime.strptime(dd,"%Y-%m-%d").strftime("%A")
# print(c)

# 23 Next Occurrence of a Weekday

# i=datetime(2025,9,12)
# t=4

# d=(t-i.weekday())%7
# print(d)
# if d==0:
#     d=7

# r=i+timedelta(days=d)
# print(r)


#Days Between Two Dates

#Total number of days between two given dates, leap years included.

# d1=date(2025,9,14)
# d2=date(2025,9,19)
# print(d2-d1)

# day of week finder

# d=date(2025,9,14)
# print(calendar.day_name[d.weekday()])

# Given a text string and a pattern string, return the starting index of the first occurrence of the pattern in the text, or -1 if it is not present.



t="hello"
p="lo"

n=0
for i in t:
    n+=1

m=0
for j in p:
    m+=1

i=0
l=0
while i<n:
    
    if t[i:i+m]==p:
        l=i
    else:
        i+=1
        
print(l)

