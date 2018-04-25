import time
import string
from mpi4py import MPI
import sys
import _md5

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

chars = list(string.printable)[10:36]
chars.insert(0,'a')
base = len(chars)

crackthis = open(sys.argv[1]).read()

def numberToBase(n, b):
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    return digits[::-1]

if __name__ == '__main__':

    if rank == 0:
        solved = False

        process = 1
        while process < size :
            n = [(process-1)*1000000,process*1000000]
            comm.send(n,dest=process,tag=1)
            print('Sending job to process',process)
            process += 1

        start = time.time()

        stopped_process = 0
        while stopped_process < size-1 :
            solved = comm.recv(source=MPI.ANY_SOURCE,tag=1)
            if solved :
                password = comm.recv(source=MPI.ANY_SOURCE,tag=2)
                process_rank = comm.recv(source=MPI.ANY_SOURCE,tag=3)
                print('Password cracked by process ',process_rank)
                print('Password \t:',password)
                print('Time \t\t:',time.time()-start,'second')
                break
            stopped_process += 1

        if not solved :
            print('Password crack failed, not enough process.')

        print('Waiting for processes to detach...')
        sys.exit()

    else:
        n = comm.recv(source=0,tag=1)
        solved = False

        for i in range(n[0],n[1]) :
            lst = numberToBase(i, base)
            word = ''
            for x in lst:
                word += str(chars[x])
            if crackthis == _md5.md5(word.encode('utf8')).hexdigest():
                solved = True
                comm.send(solved,dest=0,tag=1)
                comm.send(word,dest=0,tag=2)
                comm.send(rank,dest=0,tag=3)
                break

        comm.send(solved,dest=0,tag=1)