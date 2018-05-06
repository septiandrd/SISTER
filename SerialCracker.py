import string
import time
import _md5
import sys

def numberToBase(n, b):
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    return digits[::-1]


chars = list(string.printable)[10:36]
chars.insert(0,'a')
base = len(chars)

crackthis = open(sys.argv[1]).read()

start = time.time()

print('Cracking password...')

for i in range(0, 15000000):
    lst = numberToBase(i, base)
    word = ''
    for x in lst:
        word += str(chars[x])
    if crackthis == _md5.md5(word.encode('utf8')).hexdigest():
        solved = True
        break

print('Password \t:',word)
print('Time \t\t:',time.time()-start,'second')


