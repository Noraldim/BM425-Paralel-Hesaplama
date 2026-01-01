from multiprocessing import Process , Pipe
import multiprocessing
import time 

def banker(q):
    while True :
        txt = q.get()
        print(f"your balanc is {txt}")

def custmer(q):
    while True:
        q.put(500)

if "__main__" == __name__:
    q = multiprocessing.Queue()
    p = multiprocessing.Process(target=banker , args=(q, ))
    p = multiprocessing.Process(target=custmer , args=(q, ))

    p.start()

    p.join()

    