import multiprocessing
import time

def consumer(q):
    while True:
        item = q.get()
        print(f"İşleniyor: {item}")
        time.sleep(1) # İşlem simülasyonu
        # İşin bittiğini sisteme bildiriyoruz
        q.task_done()

if __name__ == "__main__":
    # JoinableQueue tanımlıyoruz
    jq = multiprocessing.JoinableQueue()
    
    # Consumer process başlatılıyor (Daemon olarak)
    p = multiprocessing.Process(target=consumer, args=(jq,))
    p.daemon = False # Ana program bitince bu da bitsin
    p.start()
# Producer (Ana process) işleri kuyruğa ekliyor
    tasks = ["Dosya1", "Dosya2", "Dosya3"]
    
    for task in tasks:
        jq.put(task)
        print(f"Kuyruğa eklendi: {task}")
        
    print("Tüm işlerin bitmesi bekleniyor...")
    # Kuyruktaki tüm işler için task_done() gelene kadar bekle
    #jq.join()
    
    print("Tüm işler tamamlandı! Program kapanıyor.")
