# Editor: Max

# Create Time: 9/18/21 23:09


N, D = input().split()

a = input().split()  # 月饼种类对应的数量
b = input().split()  # 月饼种类对应的总价
m = [[0.00 for i in range(3)] for j in range(1000)]  # 三维数组用来存储月饼的存量与总价

for i in range(int(N)):
    m[i][0] = int(a[i])
    m[i][1] = int(b[i])
    m[i][2] = float(b[i]) / float(a[i])

m = sorted(m, key=(lambda x: x[2]), reverse=True)  # 对单价进行降序排序

Total = 0
remain = int(D)

for i in range(int(N)):
    if int(D) <= int(m[0][0]):
        Total = int(D) * m[0][0]
    elif remain <= 0:
        print(Total)
    elif remain > m[i][0]:
        remain = int(D) - m[i][0]
        Total = Total + m[i][0] * m[i][2]
        continue
    elif remain <= m[i][0]:
        Total = Total + remain * m[i][2]
        break

print('%.2f' % Total)











