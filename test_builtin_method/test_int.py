

print(20 // 8) # 2
print(20 / 6) # 3.333333


# 纸币大小为6种[500, 200, 100, 50, 20, 10],传一个数量，求出需要纸币数量
def no_notes(amount):
    Q = [500, 200, 100, 50, 20, 10]
    x = 0
    for i in range(6):
       x += int(amount / Q[i])
       amount = int(amount % Q[i])
    if amount > 0:
        x = -1
    return x


print(no_notes(777))
