import time

def Pi(numSteps) :
    start = time.time()
    step = 1.0/numSteps
    sum = 0
    for i in range(numSteps):
        x = (i+0.5)*step
        sum += 4.0 / (1.0+x*x)
    pi = step * sum
    end = time.time()
    print("Pi with %d steps is %f in %f secs"%(numSteps,pi,end-start))

if __name__ == '__main__':
    Pi(100)
