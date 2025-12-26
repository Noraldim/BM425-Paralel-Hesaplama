# this code is totaly wrong and it asume sharign memory between the processers and this exsit only on thread not processors



from threading import Thread
from multiprocessing import Process


def one():
    sumone = 0
    for i in range(1000000):
        sumone += i**2

    print(sumone)

def two():
    sumtwo = 0
    for i in range(1000000,2000000):
        sumtwo += i**2
    print(sumtwo)

res = []

p = Process(target=one)
p2 = Process(target=two)



p.start()
p2.start()
p.join()
p2.join()



