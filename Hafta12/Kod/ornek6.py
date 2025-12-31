from multiprocessing import Pipe, Process
import time
def ping(pipe_conn):
    while(True):
        pong = pipe_conn.recv()
        pipe_conn.send(["Ping", time.time()])        
        print(pong)
        time.sleep(1)
def pong(pipe_conn):
    while True:
        ping = pipe_conn.recv()
        print(ping)
        time.sleep(1)
        pipe_conn.send(["Pong", time.time()])
if __name__ == "__main__":
    pipe_end_b, pipe_end_a = Pipe()
    Process(target=ping, args=(pipe_end_a, )).start()
    Process(target=pong, args=(pipe_end_b, )).start()

