from multiprocessing import Process, Pipe

def player(conn, name):
    msg = conn.recv() # Mesaj bekle
    print(f"{name} aldı: {msg}")
    conn.send("Pong") # Cevap ver
    conn.close()

if __name__ == "__main__":
    parent_conn, child_conn = Pipe()
    p = Process(target=player, args=(child_conn, "Oyuncu B"))
    p.start()
    
    parent_conn.send("Ping")
    response = parent_conn.recv()
    print(f"Ana Process cevabı aldı: {response}")
    p.join()
