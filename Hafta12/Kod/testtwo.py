import multiprocess
import time
import queue


def bank_work(q):
    while True:
        data = q.get()
        print("data received")
        time.sleep(2)
        
        if data == 5:
            print("now the poisened pill will be activated")
            print(data)
            break


if __name__ == "__main__":
    q = multiprocess.Queue()
    p = multiprocess.Process(target=bank_work, args=(q, ))
    p.start()
    q.put(29)
    q.put(288)
    q.put(48)
    q.put(5)

    p.join()
