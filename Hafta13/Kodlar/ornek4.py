import threading
import time
oda_kilidi = threading.Lock()
kidem = 0
kidem_limit = 3
def patron_robot():
    while True:
        if kidem >= kidem_limit:
            print("Stajyer gelisti, musaade ediliyor....")
            time.sleep(3)
        oda_kilidi.acquire()
        print("PATRON: Odaya girdi, Uzun bir toplantı yapacak")
        time.sleep(2)         
        print("PATRON: İşim bitti, çıkıyorum(Ama hemen döneceğim)")
        oda_kilidi.release()        
        #time.sleep(0.5) 

def stajyer_robot():
    global kidem
    while True:
        print("STAJYER: Kapıyı kontrol ediyor...")        
        basari = oda_kilidi.acquire(blocking=False)
        if basari:
            print("STAJYER: İNANILMAZ! SONUNDA ODAYA GİRDİM!\n")
            oda_kilidi.release()
            break
        else:
            kidem += 1
            print("STAJYER: Kapı yine duvar! Patron içeride...")        
        time.sleep(0.5)
t1 = threading.Thread(target=patron_robot)
t2 = threading.Thread(target=stajyer_robot)
time.sleep(1)
t1.start()
t2.start()
