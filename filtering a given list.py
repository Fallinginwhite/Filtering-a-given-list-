temperatures = [0, 3, 5, 7, 5, 4, 2, 0, -0.2]
outofrange = []
for i in range(0,len(temperatures)):
    if temperatures[i] < 0 or temperatures[i] > 5:
        outofrange.append(temperatures[i])
print(outofrange)
    
