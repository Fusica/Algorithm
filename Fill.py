# Editor: Max

# Create Time: 10/3/21 18:23


flag, Total = 0, 0
S = [[40000 for i in range(2)] for j in range(500)]
C, D, Da, N = input().split()
Distance = int(C) * int(Da)  # 满箱油可以跑多远
for i in range(int(N)):
    temp1, temp2 = input().split()
    S[i][0], S[i][1] = float(temp1), float(temp2)
S[int(N)][0], S[int(N)][1] = 0, int(D)
S = sorted(S, key=(lambda x: x[1]))

if S[0][1] > 0:
    print('The maximum travel distance = 0.00')
else:
    flag = 1
    current_gas = 0
    for i in range(int(N)):
        if S[i+1][1] - S[i][1] > Distance:
            flag = 0
            print('The maximum travel distance = ' + str('%.2f' % (S[i][1] + Distance)))
            break
        else:
            index = i
            min_price = S[i][0]
            for j in range(i+1, int(N)+1):
                if S[j][1] - S[i][1] <= current_gas * int(Da):
                    if S[j][0] < min_price:
                        index = j
                        min_price = S[j][0]
                else:
                    continue

            if index != i:
                current_gas -= (S[index][1] - S[i][1]) / int(Da)
                i = index
                continue

            index = i
            for j in range(i + 1, int(N) + 1):
                if S[j][1] - S[i][1] <= Distance:
                    if S[j][0] < min_price:
                        index = j
                        break
                else:
                    continue

            if index != i:
                Total += ((S[index][1] - S[i][1]) / int(Da) - current_gas) * S[i][0]
                current_gas = 0
                i = index
                continue

            index = i
            min_price = 40000
            for j in range(i + 1, int(N) + 1):
                if S[j][1] - S[i][1] <= Distance:
                    if S[j][0] < min_price:
                        index = j
                        min_price = S[j][0]
                else:
                    continue
            Total += (int(C) - current_gas) * S[i][0]
            current_gas = int(C) - (S[index][1] - S[i][1]) / int(Da)
            i = index
if flag:
    print('%.2f' % Total)
