import itertools
from multiprocessing import Process
import multiprocessing
import os
import time
import pyzipper
ZIP_FILE = "gizli_bilgi.zip"
CHARACHTER = "0123456789"
MIN_CHAR = 4
MAX_CHAR = 4

def worker(worker_id, total_worker, q, found_flag):
    try:
        zf = pyzipper.AESZipFile(ZIP_FILE)
    except Exception as e:
        print(f"Hata var: {e}")
    # (A,B) x = A,A , A,B, B,A, B,B
    for length in range(MIN_CHAR, MAX_CHAR+1):
        gen = itertools.product(CHARACHTER, repeat=length) # ('0', '0', '0', '0') / 0000 - ('9','9','9','9')
        my_slice = itertools.islice(gen, worker_id, None, total_worker)
        for p in my_slice:
            if found_flag.is_set():
                return 
            password = "".join(p) # 0000
            try:
                zf.extractall(pwd=password.encode("utf-8"))
                found_flag.set()
                q.put(password)
            except:
                continue

if __name__ == "__main__":
    baslangic_zamani = time.time()
    if not os.path.exists(ZIP_FILE):
        print("Dosya yok!")
    processes = []
    num_workers = 1
    q = multiprocessing.Queue()
    found_flag = multiprocessing.Event()
    for i in range(num_workers):
        p = Process(target=worker, args=(i, num_workers, q, found_flag))
        processes.append(p)
    for j in processes:
        j.start()
    for j in processes:
        j.join()
    if not q.empty():
        pwd = q.get()
        print(f"Parola bulundu: {pwd}")
    print(f"Gecen sure: {time.time()-baslangic_zamani}")


