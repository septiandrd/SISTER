import string
import time

def numberToBase(n, b):
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    return digits[::-1]


chars = list(string.printable)[10:36]
chars.insert(0,'a')
base = len(chars)

print(chars)

n = [9999900,10000000]

crackthis = 'medan'

start = time.time()

for i in range(n[0], n[1]):
    lst = numberToBase(i, base)
    word = ''
    for x in lst:
        word += str(chars[x])
    # print(word)
    if crackthis == word:
        solved = True
        break

print('Password :',word)
print('finished in',time.time()-start)