from threading import Lock, Thread
import time
def kirmizi_robot(kilit1, kilit2):
    while True:
        print("Kirmizi kilit1'e erisiyor...")
        kilit1.acquire()
        print("Kirmizi kilit2'ye erisiyor...")
        erisim_varmi = kilit2.acquire(timeout=3)
        if erisim_varmi:
            try:
                print("Kirmizi tum kilitlere eristi")
            finally:
                kilit1.release()
                kilit2.release()
                print("Kirmizi tum kilitleri serbest birakti!")
        else:
            print("Kirmizi kilit2'ye erisemedi, kilit1'de serbest birakiliyor...")
            kilit1.release()
            #kilit2.release()
        time.sleep(0.5)
def mavi_robot(kilit1, kilit2):
    while True:
        print("Mavi kilit2'ye erisiyor...")
        kilit2.acquire()
        print("Mavi kilit1'e erisiyor...")
        kilit1.acquire()
        print("Mavi tum kilitlere eristi")
        kilit1.release()
        kilit2.release()
        print("Mavi tum kilitleri serbest birakti!")
        time.sleep(0.5)
mutex1 = Lock()
mutex2 = Lock()
kirmizi = Thread(target=kirmizi_robot, args=(mutex1, mutex2))
mavi = Thread(target=mavi_robot, args=(mutex1, mutex2))
kirmizi.start()
mavi.start()
