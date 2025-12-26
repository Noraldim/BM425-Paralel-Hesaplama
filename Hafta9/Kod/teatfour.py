import threading
import time

th = threading.Event()


def worker():
    while not th.is_set():
        print("the worker is doing best job ever")
        time.sleep(1)


t = threading.Thread(target=worker)
t.start()
time.sleep(5)

print("will finish")
th.set()