def convertTo24(h, m, s, am):
    if not am: #PM
        if h == 12: 
            return h, m, s
        else:
            return h+12, m, s
    else: #AM
        if h == 12:
            return 0, m, s
        else:
            return h, m, s

time = input().strip(' ')
am = ""
am += time[-2]
am += time[-1]
time = time[:-2]
time = list(map(int, time.split(':')))
in24 = convertTo24(time[0], time[1], time[2], am == "AM")
print("%.2d"%in24[0] + ':' + "%.2d"%in24[1] + ':' + "%.2d"%in24[2])