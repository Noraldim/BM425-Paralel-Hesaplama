from concurrent.futures import ThreadPoolExecutor
import time
import threading



def work(work_num):
    name = threading.current_thread().name
    print(f"the {name} is now doing {work_num} job")
    time.sleep(2)
    print(f"{name} finished")


with ThreadPoolExecutor(max_workers= 1) as pool:

    pool.map(work , range(2,8))


print("All done:")