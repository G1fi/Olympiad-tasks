# Дудко Павел Иванович

start = 0
res = 0
n = ''
m = ''

for i in input().split():
    nlen = int(i[0])
    mlen = int(i[0])
    
for i in input().split():
    n += i

for i in input().split():
    m += i
    
while True:
    temp = n.find(m, start)
    if temp == -1:
        break
    else:
        res += 1
        start = temp + mlen
        
print(res)