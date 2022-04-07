# https://www.acmicpc.net/problem/3020
import sys
input = sys.stdin.readline

# 만나는 장애물 개수 세기
def binary(obstacle, h, start, end):
    if start > end:
        return len(obstacle) - (end + 1)
    
    mid = (start + end) // 2
    if obstacle[mid] <= h:
        return binary(obstacle, h, mid + 1, end)
    else:
        return binary(obstacle, h, start, mid - 1)

n, h = map(int, input().split())
# 종유석
top = []
# 석순
bottom = []

for i in range(n):
    obstacle = int(input())
    # 석순
    if i % 2 == 0:
        bottom.append(obstacle)
    # 종유석
    else:
        top.append(obstacle)

bottom.sort()
top.sort()

result = n
count = 0
# 1번 구간부터 h번 구간까지 확인
for i in range(1, h + 1):
    # 파괴한 석순의 개수
    bottomNum = binary(bottom, i - 1, 0, len(bottom) - 1)
    # 파괴한 종유석의 개수
    topNum = binary(top, h - i, 0, len(top) - 1)
    # 총 파괴한 장애물 개수
    curNum = bottomNum + topNum
    if curNum < result:
        result = curNum
        count = 1
    elif curNum == result:
        count += 1

print(result, count)

# 참고: https://blog.naver.com/PostView.nhn?blogId=crm06217&logNo=222023706440&categoryNo=23&parentCategoryNo=0&viewDate=&currentPage=1&postListTopCurrentPage=1&from=postView

# 이진 탐색