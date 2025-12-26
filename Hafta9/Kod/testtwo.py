import threading
import time
import random


Bounded = threading.BoundedSemaphore(3)


def lib(t):
    with Bounded:
        print(f"student {t} want to take the book")
        
        time.sleep(random.randint(1,3))
        
        print(f"student{t} readed the book")

def confiuse(t):
    try:
        Bounded.release()
    except ValueError as e:
        print(f"some error just hapend {e}")


x = threading.Thread(target=confiuse, args=(1, ))
x.start()
x.join()


tlist = []
for i in range(3):
    t = threading.Thread(target=lib , args=(i, ))
    tlist.append(t)
    t.start()

for i in tlist:
    i.join()