from concurrent.futures import ThreadPoolExecutor
import time
import threading

def gorev_yap(is_no):
    # Hangi Thread'in çalıştığını görelim
    thread_adi = threading.current_thread().name
    print(f"[{thread_adi}] Görev {is_no} başladı...")
    time.sleep(1) # İşlem simülasyonu
    return f"Görev {is_no} Bitti"

# Havuz oluşturuluyor (Maksimum 2 İşçi)
print("--- Havuz Açılıyor (Sadece 2 İşçi Var) ---")
with ThreadPoolExecutor(max_workers=2) as havuz:
    # 5 adet görevi havuza gönderiyoruz
    # map fonksiyonu, for döngüsü gibi çalışır ve işleri dağıtır
    sonuclar = havuz.map(gorev_yap, range(1, 6))

print("--- Tüm İşler Tamamlandı ---")