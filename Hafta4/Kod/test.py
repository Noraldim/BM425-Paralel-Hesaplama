from multiprocessing import Process
from threading import Thread
import time


def example_one():
    for i in range(10000):
        sum += i**2


def example_two():
    for i in range(10000,20000):
        sum += i**2




t = Process(target=example_one, args=())
t_tow = Process(target=example_two, args=())


## create two processer one is sum of (1 to 10000 )**2 and the other is sum of (10000 to 20000)**2  and return the sum of both processer
