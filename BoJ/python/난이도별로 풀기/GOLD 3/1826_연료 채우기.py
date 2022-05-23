# https://www.acmicpc.net/problem/1826
import sys ,heapq
input = sys.stdin.readline

n = int(input())
# 거리별 우선순위  큐
distance = []
for i in range(n):
    # 거리, 채울 수 있는 연료
    a, b = map(int, input().split())
    heapq.heappush(distance, [a, b])

# 마을 까지의 거리, 원래 있던 연료 양
destination, fuel = map(int, input().split())

# 채울 수 있는 연료 별 우선순위 큐
gas = []
count = 0
while fuel < destination:
    # 도달 할 수 있는 거리 까지만 pop
    while distance and fuel >= distance[0][0]:
        d, f = heapq.heappop(distance)
        # 우선순위 큐에 채울 수 있는 연료별로 추가
        heapq.heappush(gas, [-f, d])

    # 우선순위 큐가 비면 도착할 수 없다는 의미
    if len(gas) == 0:
        print(-1)
        break

    f, d = heapq.heappop(gas)
    # f 는 음수이므로 더해주기 위해 -= 
    fuel -= f
    count += 1

else:
    print(count)