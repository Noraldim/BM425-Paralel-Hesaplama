import multiprocessing
from queue import Queue
from threading import Thread
import time
def consumer(q):
    while True:
        txt = q.get()
        print(txt)
        time.sleep(1)
def producer(q):
    while True:
        q.put("Merhaba")
        print("Mesaj gonderildi")
        #time.sleep(1)
if __name__ == "__main__":
    q = multiprocessing.Queue(maxsize=10)
    t1 = multiprocessing.Process(target=consumer, args=(q, ))
    t2 = multiprocessing.Process(target=producer, args=(q, ))
    t1.start()
    t2.start()
