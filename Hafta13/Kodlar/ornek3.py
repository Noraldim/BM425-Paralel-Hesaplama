import threading
import time
bariyer_basla = threading.Barrier(2)
bariyer_sonuc = threading.Barrier(2)
bariyer_reset = threading.Barrier(2)
kilit1 = threading.Lock()
kilit2 = threading.Lock()
def agir_cekim_robot(kendi_kilidi, diger_kilit, isim):
    tur_sayisi = 1
    while True:
        print(f"\n--- {isim} (Tur: {tur_sayisi}) ---")
        kendi_kilidi.acquire()
        print(f"{isim}: Kendi kilidini aldı. Diğerini bekliyor...")        
        time.sleep(0.5)         
        bariyer_basla.wait()        
        print(f"{isim}: Diğer kilide hamle yapıyor!")
        basari = diger_kilit.acquire(blocking=False)        
        bariyer_sonuc.wait()        
        if basari:
            print(f"!!! {isim} BAŞARDI !!!")
            diger_kilit.release()
            kendi_kilidi.release()
            break
        else:
            print(f"{isim}: ÇAKIŞTI! Kilidi alamadı.")
            time.sleep(0.5) # Okumak için bekleme            
            print(f"{isim}: Mecburen elindekini bırakıyor...")
            kendi_kilidi.release()            
            bariyer_reset.wait()            
            time.sleep(1) 
            tur_sayisi += 1
t1 = threading.Thread(target=agir_cekim_robot, args=(kilit1, kilit2, "Robot-A"))
t2 = threading.Thread(target=agir_cekim_robot, args=(kilit2, kilit1, "Robot-B"))
time.sleep(1)
t1.start()
t2.start()
