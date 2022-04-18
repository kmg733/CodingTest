# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AV5QLkdKAz4DFAUq&categoryId=AV5QLkdKAz4DFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=1&pageSize=30&pageIndex=1
import datetime

# t = int(input())
# for i in range(1, t + 1):
#     ymd = int(input())
#     y = int(ymd // 10000)
#     m = int(ymd % 10000 // 100)
#     d = int(ymd % 100)
#     try:
#         day = datetime.datetime(y, m, d)
#         print(f'#{i} {day.strftime("%Y/%m/%d")}')
#     except:
#         print(f"#{i} -1")

T = int(input())
days = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
for test_case in range(1, T + 1):
   case = str(input())
   year = case[0:4]
   month = case[4:6]
   day = case[6:8]
   
   answer = ''
   if 0 < int(month) < 13 and 0 < int(day) <= days[int(month)]:
       answer = year + '/' + month + '/' + day
   else:
       answer += '-1'

   print("#" + str(test_case) + " " + answer)