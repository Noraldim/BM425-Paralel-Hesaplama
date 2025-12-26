from multiprocessing import Process, Manager
import time
def test_one(res):
    topla = 0
    for i in range(100000000):
        topla += i**2
    res.append(topla)

def test_two(res):
    topla = 0 
    for i in range(100000000,200000000):
        topla += i**2
    res.append(topla)




if __name__ == "__main__":
    
    with Manager() as manager:
        startx = time.time()
        res = manager.list()
        process_list = []

        for i in range(1):
            p = Process(target=test_one, args=(res,))
            process_list.append(p)
            p.start()

        for i in range(1):
            p = Process(target=test_two, args=(res,))
            process_list.append(p)
            p.start()

        for p in process_list:
            p.join()
        endx = time.time()
        print("The total time is :" , endx-startx)
        print("Result sum:", sum(res))

""""
to change between python when using requeist we need to use py -0p to show how many version 
we have 
and also when we chose some verison we type venv -m vesrion venvName ]

""""



