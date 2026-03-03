date = "03/03/2026"
print(date)

import datetime

now = datetime.datetime.now()
print(now)

tdy = datetime.datetime.today()
print(tdy)
print(type(tdy))

# date
print(tdy.date())

# year
print(tdy.year)

# month
print(tdy.month)

# day
print(tdy.day)

# hour
print(tdy.hour)

# min
print(tdy.minute)

# second
print(tdy.second)

# micro second
print(tdy.microsecond)

# formating the dates

# year
print("-----------------year------------------")
print(tdy.strftime("%y")) # 26
print(tdy.strftime("%Y")) # 2026

# month
print("-----------month---------------------")
print(tdy.strftime("%b")) #Mar
print(tdy.strftime("%B")) #March
print(tdy.strftime("%m")) #03

# day
print("-------------day-------------------")
print(tdy.strftime("%a")) # Tue
print(tdy.strftime("%A")) #Tuesday
print(tdy.strftime("%d")) # 03
print(tdy.strftime("%D")) #03/03/2026

# hour
print("-----------------hour---------------")
print(tdy.strftime("%I")) #12hr 10
print(tdy.strftime("%H")) #24hr 10
print(tdy.strftime("%h")) #Mar
print(tdy.strftime("%p")) #Am

# Minutes
print("----------minutes---------------")
print(tdy.strftime("%M")) #225
print(tdy.strftime("%m")) #Month 03

# seconds
print("-------------Seconds------------")
print(tdy.strftime("%S")) #27
# print(tdy.strftime("%s")) invalid format

# micro second
print("----------micro second------------")
print(tdy.strftime("%F")) # 2026-03-03
print(tdy.strftime("%f")) # 986207

# we format the date our own format

print(tdy.strftime("%d/%m/%Y"))
print(tdy.strftime("%d - %m - %Y"))
print(tdy.strftime("%d - %b - %y"))
print(tdy.strftime("%d - %m - %Y :%I :%M :%S :%f :%p"))

# our own date

dt = datetime.datetime(2000,3,10)
print(dt)

print(dt.strftime("%d/%m/%Y"))

dd = datetime.timedelta(days= 2)
df = dt+dd
print(df.strftime("%d-%m-%Y"))

db = dt-dd
print(db.strftime("%d-%m-%Y"))

print(tdy-dd)
print(tdy+dd)