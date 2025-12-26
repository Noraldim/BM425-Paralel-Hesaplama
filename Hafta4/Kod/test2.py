from threading import Thread
import time 


def multi_one():
    total1 = 0
    for i in range(100010000):
        total1 +=i**2
    res.append(total1)

def multi_two():
    total2 = 0
    for i in range(10000,20000):
        total2 +=i**2
    res.append(total2) 


res = []
startx = time.time()
t1 = Thread(target=multi_one , args=())
t2 = Thread(target=multi_two , args=())


t1.start()
t2.start()
t1.join()
t2.join()

endx = time.time()
result = sum(res)
print(res[0])
print(res[1])
print(result)
print(endx - startx)
