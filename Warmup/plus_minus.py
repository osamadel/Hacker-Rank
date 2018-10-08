def calcFraction(n, arr):
    pve = 0
    nve = 0
    zeros = 0
    for i in arr:
        if i > 0:
            pve += 1
        elif i < 0:
            nve += 1
        else:
            zeros += 1
    return (pve/n, nve/n, zeros/n)

n = int(input())
nums = list(map(int, input().split()))
result = calcFraction(n, nums)

print("%.6f"%result[0])
print("%.6f"%result[1])
print("%.6f"%result[2])