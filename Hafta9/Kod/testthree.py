import threading
import time
import random


def worker():
    while True:
        print("ther worker are working hard")
        time.sleep(0.5)

t = threading.Thread(target=worker, daemon=True)
t.start()
time.sleep(3)