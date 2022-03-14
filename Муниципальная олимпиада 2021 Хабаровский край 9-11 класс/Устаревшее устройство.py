# Дудко Павел Иванович

import sys

listik = []
res = "YES"
blok1_start = 0
blok2_start = 0
blok2_end = 0
while True:
    text = sys.stdin.readline().rstrip()
    if text == "":
        break
    listik.append(text)

if listik[0] != '12':
    res = "NO"

if listik[-1] != '21' or listik[-2] != '  09' or listik[-3] != '    21':
    res = "NO"
    
try:
    blok1_start = listik.index('  90')
    if blok1_start == -1:
        res = "NO"    
except:
    pass

try: 
    blok2_start = listik.index('    12')
    if blok2_start == -1:
        res = "NO"   
except:
    pass

try: 
    blok2_end = listik.index('    21')
    if blok2_end == -1:
        res = "NO"
except:
    pass

if blok1_start > 2:
    for index_elem in range(1, blok1_start-1):
        if listik[index_elem].rfind('###', -3) == -1 or listik[index_elem].rfind('  ', 0, 2) == -1:
            res = "NO"
            
if blok2_start-1 > blok1_start+1:
    for index_elem in range(blok1_start+1, blok2_start-1):
        if listik[index_elem].rfind('###', -3) == -1 or listik[index_elem].rfind('    ', 0, 4) == -1:
            res = "NO"
            
if blok2_end-1 > blok2_start+1:
    for index_elem in range(blok2_start+1, blok2_end-1):
        if listik[index_elem].rfind('###', -3) == -1 or listik[index_elem].rfind('      ', 0, 6) == -1:
            res = "NO"
                
print(res)
