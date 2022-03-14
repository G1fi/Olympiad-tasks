# Дудко Павел Иванович

m = int(input())
n = m
res = 0

pyat0 = n // 5000
pyat1 = n // 1000
pyat2 = n // 500
pyat3 = n // 200
pyat4 = n // 100

if n % 100 != 0:
    res = 0
    
else:
    for pyat00 in range(n // 5000 + 1):
        n -= 5000 * pyat00
        for pyat01 in range(n // 1000 + 1):
            n -= 1000 * pyat01
            for pyat02 in range(n // 500 + 1):
                n -= 500 * pyat02
                for pyat03 in range(n // 200 + 1):
                    n -= 200 * pyat03
                    for pyat04 in range(n // 100 + 1):
                        n = m - (5000 * pyat00 + 1000 * pyat01 + 500 * pyat02 + 200 * pyat03 + 100 * pyat04)
                        
                        print(n)
                        if n == 0:
                            res += 1
                        n = m
                            
print(res)