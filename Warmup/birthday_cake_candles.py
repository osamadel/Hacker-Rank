def countTallest(candles):
    tallest = max(candles)
    count = candles.count(tallest)
    return count

n = input()
height = [int(height_temp) for height_temp in input().strip(' ').split()]
print(countTallest(height))