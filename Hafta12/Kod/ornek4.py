import multiprocessing
import queue
data = "selam"
def worker(q):
    while True:
        data = q.get()
        # Zehirli Hap kontrolü
        if data is None:
            print("Durdurma sinyali alındı. Çıkılıyor...")
            break 
        print(f"Veri işlendi: {data**2}")
if __name__ == "__main__":
    q = multiprocessing.Queue()
    p = multiprocessing.Process(target=worker, args=(q,))
    p.start()    
    # İşler gönderiliyor
    q.put(10)
    q.put(20)    
    # İşler bitti, Poison Pill gönderiliyor
    q.put(None) 
    p.join()
    
