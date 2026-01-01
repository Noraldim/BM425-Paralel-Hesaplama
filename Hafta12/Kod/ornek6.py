from multiprocessing import Pipe, Process
import time
count = 0
def ping(pipe_conn):
    global count
    while(True):
        pong = pipe_conn.recv()
        pipe_conn.send(["Ping", time.time()])        
        print(pong)
        time.sleep(1)
        count += 1
        if count == 4:
            break
def pong(pipe_conn):
    global count
    while True:
        pipe_conn.send(["Pong", time.time()])
        ping = pipe_conn.recv()
        print(ping)
        time.sleep(1)
        count += 1
        if count == 4:
            break
        
if __name__ == "__main__":
    pipe_end_b, pipe_end_a = Pipe()
    Process(target=ping, args=(pipe_end_a, )).start()
    Process(target=pong, args=(pipe_end_b, )).start()

