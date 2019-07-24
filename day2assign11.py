c = ["PKM","ALN","GLN","NVR","PVR","KM","VP","CS","MCS"]

f = ["PKM","ALN","RMZ","CS","MCS"]

b = ["PKM","ALN","NV","KM","RMV"]

print("\nPlayer Plays All games are :\n")
for i in c:
    if i in f and i in b:
        print(i)

print("\nPlayer Plays only one game :\n")

l = []

l.extend(c)
l.extend(f)
l.extend(b)

di = {}

for i in l:
    if not i in di:
        di[i] = 1
    else:
        di[i] += 1

for key in di:
    if di[key] == 1:
        print(key)
    

