import threading
import time 
import random
sem = threading.Semaphore(3)
def student(t):
    print(f"student {t} will enter  to the manager office")
    with sem:
        print(f"student {t} entered to meet the manger")
        time.sleep(random.randint(1,4))
        print(f"student {t} finished the meeting ")

thlist = []
for i in range(10):
    t = threading.Thread(target=student ,args=(i, ))
    thlist.append(t)
    t.start()

for i in thlist:
    i.join()
