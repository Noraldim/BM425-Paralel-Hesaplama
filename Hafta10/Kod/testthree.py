# to know the current name of the thread == threading.current_thread().name
# to create threads pool                 == ThreadPoolExcuter()
# to submit function to the pool         ==  x.submit(fun_name)
import threading
import time 
from concurrent.futures import ThreadPoolExecutor



def work(worker, shift , work_no):
    name = threading.current_thread().name
    print(f"named {name} will be done by {worker} at shift no {shift} in the work number {work_no}")
    time.sleep(3)


def sayHello():
    print("helloooo")


with ThreadPoolExecutor(max_workers=3) as pool:
    pool.map(work ,[1,2,3,4,5],  [1,2,3,4,5], [6,7,8,9,10])
    pool.submit(sayHello)


print("the work is done")