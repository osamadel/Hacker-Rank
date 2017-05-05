def compare(a, b):
    scoreA = 0
    scoreB = 0
    for i in range(len(a)):
        if a[i] > b[i]:
            scoreA += 1
        elif a[i] < b[i]:
            scoreB += 1
    return (scoreA, scoreB)

a = list(map(int, input().split()))
b = list(map(int, input().split()))
scoreA, scoreB = compare(a,b)
print(scoreA, scoreB)