sugar = int(input())

bag = 0

while True:
    if (sugar % 5) == 0:
        bag = bag + (sugar // 5)
        print(bag)
        break

    sugar -= 3
    bag += 1
    if sugar < 0:
        print(-1)
        break