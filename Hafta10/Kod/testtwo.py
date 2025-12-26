import threading
import time

#TOTAL THREAD NUMBER == active_count()
#CHEACK IF LIVE      == is_live()
#NAME OF THREAD      == threadAlias.name

def work():
    print("start")
    time.sleep(2)
    print("finish")


t1 = threading.Thread(target=work)
t2 = threading.Thread(target=work)
t3 = threading.Thread(target=work, name="nor")
t1.start()
t2.start()
t3.start()

print(f"The totla amount of thread are : {threading.active_count()}")


for x in threading.enumerate():
    print(f"name : {x.name} and he is {x.is_alive()}")


t1.join()
t2.join()
t3.join()


