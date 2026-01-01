import time
import multiprocessing


def bank_work(q):
    while True:
        text = q.get()
        print(f"{text} has just taken and start")
        time.sleep(1)
        q.task_done()


if __name__ == "__main__":
    gq = multiprocessing.JoinableQueue()

    p = multiprocessing.Process(target=bank_work ,args=(gq, ))
    p.daemon = False
    p.start()
    
    tasks = ["taskone", "taskTwo", "taskThree"]

    for task in tasks:
        gq.put(task)
        print(f"{task} added to queue")

    print("all task was added")
   
    p.join()
    print("every thing is done")
