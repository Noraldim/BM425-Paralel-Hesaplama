from threading import Barrier, Condition, Thread
import time 



def bigbr():
    print("all the student had entered to the class")

signal = False
bry = Barrier(3, action=bigbr)
cv = Condition()

def student(t):
    global signal
    print(f"my student id is {t} ")
    with cv :
        print("witing and enterd passive mode")
        while not signal:
            cv.wait()
    print(f"student{t}strting the exam")

def supervisor():
    global signal
    print("supervisor check all the student")
    time.sleep(5)
    with cv :
        signal = True
        cv.notify_all()  
    print("To all student start the exam ..")


t1 = Thread(target=student , args=(1,))
t2 = Thread(target=student , args=(2,))
t3 = Thread(target=student , args=(3,))
s1 = Thread(target=supervisor )

t1.start()
t2.start()
t3.start()
s1.start()

t1.join()
t2.join()
t3.join()
s1.join()


    



