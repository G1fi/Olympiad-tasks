# Дудко Павел Иванович

n = int(input())
listik = []
res = []
ans = ''

for i in range(n):
    temp = input().split()
    listik.append(int(temp[1]) - int(temp[0]))

for i in range(n):
    max_time = max(listik)
    if max_time != -1:
        max_index = listik.index(max(listik))
        res.append(max_index)
        listik[max_index] = -1

for i in res:
    ans += ' ' + str(i + 1)
    
print(ans.strip())