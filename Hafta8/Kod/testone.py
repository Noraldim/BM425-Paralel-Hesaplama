from threading import Barrier, Thread
import time

# Create a barrier that waits for 3 threads
barrier = Barrier(3)

def worker(thread_id):
    print(f"Thread {thread_id} is doing some work...")
    time.sleep(1 + thread_id)  # simulate different work duration

    print(f"Thread {thread_id} reached the barrier.")
    barrier.wait()  # Wait for other threads

    print(f"Thread {thread_id} passed the barrier and continues working.")

threads = []
for i in range(3):
    t = Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()
