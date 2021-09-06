raw_date = input("enter the date in \"dd-mm-yyyy\" format")

raw_date = raw_date.split("-")

raw_date =list(map(int,raw_date))

date = raw_date[0]

month = raw_date[1]

century_head = raw_date[2] // 100

century_tail = raw_date[2] - century_head*100

month_code = [1,4,4,0,2,5,0,3,6,1,4,6]

century_code = {15:0 , 16:6 , 17:4 , 18 : 2 , 19:0 , 20:6}

day = ["SATURDAY","SUNDAY","MONDAY","TUESDAY","WEDNESDAY","THURSDAY","FRIDAY"]

sol = date+month_code[month-1]+century_code[century_head]+century_tail+(century_tail//4)

sol = sol%7

print(day[sol])
