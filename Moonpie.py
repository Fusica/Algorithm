# Editor: Max

# Create Time: 9/18/21 23:09


n, d = input().split()
n = int(n)
d = int(d)  # 需求总量

k = 1000
price = 0
a = input().split()  # 月饼种类对应的数量
b = input().split()  # 月饼种类对应的总价
length = len(a)
for l in range(length - 1):
    a[l] = float(a[l])
    b[l] = float(b[l])

price = [0] * length
priceU = [0] * length
for i in range(length):
    price[i] = float(b[i]) / float(a[i])

price.sort(reverse=True)  # 对单价进行降序排序
for i in range(length):
    priceU[i] = price[i]

for i in range(length):
    price[i] = float(b[i]) / float(a[i])

for i in range(length):
    for j in range(length):
        if price[i] == priceU[j]:
            Big = i
remain = d - float(a[Big])







