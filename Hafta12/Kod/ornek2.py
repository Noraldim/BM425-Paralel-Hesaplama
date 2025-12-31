import multiprocessing
import queue # queue.Empty hatası için gerekli
import time

def worker(q):
    try:
        # 3 saniye veri bekle, gelmezse hata ver
        data = q.get(timeout=3)
        print(f"Worker veriyi aldı: {data}")
    except queue.Empty:
        print("Kuyruk boş! Süre doldu, worker kapanıyor.")
    except Exception as e:
        print(e)
def queue_add(q):
    time.sleep(5)
    q.put("Deneme")

if __name__ == "__main__":
    q = multiprocessing.Queue()
    p = multiprocessing.Process(target=worker, args=(q,))
    p1 = multiprocessing.Process(target=queue_add, args=(q, ))
    p.start()
    p1.start()
    #q.put("Selam")
    # Ana process hiçbir şey göndermiyor...
    # Worker 3 saniye bekleyip kapanacak.
    p.join()
