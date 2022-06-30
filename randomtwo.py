#this is randomtwo
#it is a python module that is similar to random, but it uses a different algorithm to generate random numbers
import time
import math as m
import random as rd
try:
    import hashlib as hl
except ImportError:
    import os
    os.system("pip3 install hashlib")
    import hashlib as hl

global seed
seed = None
global actualsd
actualsd = time.time()

def random():
    #we need a random float between 0 and 1\
    if seed == None:
        actualsd = time.time()
    else:
        actualsd = seed
    hexnum = hl.sha256(str(actualsd).encode()).hexdigest()
    #convert to base 10
    bten = int(hexnum, 16)
    #divide by 2^32-1
    new = bten / (2**256-1)
    final = new % 1
    return final

def randint(a, b):
    return round((random() * (b - a) + a)) #we use round instead of int because int always floors the number

def randrange(a, b, c):
    return round((randint(a, b) / c)) * c

def choice(l):
    return l[randint(0, len(l) - 1)]

def shuffle(l):
    for i in range(len(l)):
        j = randint(0, len(l) - 1)
        l[i], l[j] = l[j], l[i]
    return l

#also, the functions are named the same as the ones in random
#this is so that this module can be used as a drop-in replacement for random

#random sample
def sample(s, k):
    #note: the sample may be greater than the array size (ex. sample([1,3,4], 5)
    #bug: this script will run so fast that all samples will be the same
    #solution: use a different seed for each sample
    ls = shuffle(s)
    smpl = []
    for i in range(k):
        smpl.append(ls[randint(0, len(ls) - 1)])
    return smpl
    

def uniform(a, b):
    return random() * (b - a) + a #similar to randrange but works with floats

def normalvariate(mu, sigma):
    return mu + sigma * random()

def lognormvariate(mu, sigma):
    return m.exp(normalvariate(mu, sigma))

def expovariate(lambd):
    return -m.log(1 - random()) / lambd

def vonmisesvariate(mu, kappa):
    if kappa <= 1e-6:
        return normalvariate(mu, 1)
    else:
        y = normalvariate(0, 1)
        z = normalvariate(0, 1)
        r = m.sqrt((-2 * m.log(y)) ** 2)
        phi = 2 * m.pi * z
        return mu + kappa * r * m.cos(phi)

def gammavariate(alpha, beta):
    return m.exp(normalvariate(0, 1) / alpha) * beta

def betavariate(alpha, beta):
    y = random()
    return y ** (1 / (alpha + 1)) * (1 - y) ** (1 / (beta + 1))

def triangular(low, high, mode):
    u = random()
    if u < (mode - low) / (high - low):
        return low + m.sqrt(u * (high - low) * (mode - low))
    else:
        return high - m.sqrt((1 - u) * (high - low) * (high - mode))

def weibullvariate(alpha, beta):
    return alpha * (-m.log(1 - random())) ** (1 / beta)

def randbytes(n):
    if seed == None:
        actualsd = time.time()
    else:
        actualsd = seed
    return hl.sha256(str(actualsd).encode()).hexdigest()[:n]

def sample(s, k):
    ls = shuffle(s)
    smpl = []
    if seed == None:
        actualsd = time.time()
    else:
        actualsd = seed
    tempsd = actualsd
    stateone = getstate()
    for i in range(k):
        tempsd = tempsd + i
        setseed(tempsd)
        smpl.append(ls[randint(0, len(ls) - 1)])
    setstate(stateone)
    return smpl
def urandom(n):
    return os.urandom(n)

def getstate():
    return seed

def setseed(s):
    global seed
    seed = s
    return seed

def setstate(s):
    global seed
    seed = s
    return seed

def getrandbits(k):
    return random() * 2 ** k

#joke functions below

def jeff():
    print("jeff lol")

def credits():
    print("randomtwo")
    print("a python module coded by LeWolfYT")
    print("(this is my third module, also check out gfxplus and turtleplus)")
    print("github.com/LeWolfYT/randomtwo")
    print("similar to random, but uses a different agorithm")
    print("thank you for using randomtwo")
    print("i hope small things like this inspire you to do big things in the future")
    print("you can use this module for whatever you want, but i would appreciate it if you left a comment on github")
    print("again, thank you for using randomtwo")

if __name__ == "__main__":
    print("randomtwo test")
    print(str(random()) + ": random value between 0 and 1")
    print(str(randint(0, 10)) + ": random integer between 0 and 10")
    print(str(randrange(0, 10, 2)) + ": random integer between 0 and 10, but only even numbers")
    print("all list-based functions use the list: [1, 3, 4, 5]")
    print(str(choice([1, 3, 4, 5])) + ": random element from list")
    print(str(shuffle([1, 3, 4, 5])) + ": random list shuffled")
    print(str(uniform(0, 10)) + ": random float between 0 and 10")
    print(str(sum(sample([1, 3, 4, 5], 10))/10) + ": avg of random sample from list")
    print("random state: " + str(getstate()))
    print("all these functions use the same seed: " + str(setseed("12345")))
    print(str(random()) + ": random value between 0 and 1")
    print(str(randint(0, 10)) + ": random integer between 0 and 10")