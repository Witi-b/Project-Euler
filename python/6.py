n = 100
k = 0
y = 0
for i in range(1,n+1):
    k += i*i
for i in range(1,n+1):
    y += i
y = y**2
print(int(y-k))