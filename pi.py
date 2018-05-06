import time
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

def Pi(minStep,maxStep,numSteps,rank) :
    start = time.time()
    step = 1.0/numSteps
    sum = 0
    for i in range(minStep,maxStep):
        x = (i+0.5)*step
        sum += 4.0 / (1.0+x*x)
    pi = step * sum
    end = time.time()
    print("Rank",rank,"calculate pi from step %d to %d is %f in %f secs"%(minStep,maxStep-1,pi,end-start))
    return pi


if __name__ == '__main__':

    val = Pi((25*rank),(25*(rank+1)),100,rank)
    sum = comm.reduce(val,op=MPI.SUM,root=0)

    if rank == 0 :
        print('\nRank 0 worked out the sum of pi =', sum)