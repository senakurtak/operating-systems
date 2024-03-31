from multiprocessing import Process, Value, Lock
import time
import random

def increase_balance(balance, lock):
    with lock:
        current_balance = balance.value
        time.sleep(random.uniform(0, 0.5))
        balance.value += 50
        print(f"[Yazıcı proses {increase_balance.__name__}]: Mevcut bakiye={current_balance}, 50 arttırıldı. Yeni bakiye={balance.value}")

def decrease_balance(balance, lock):
    with lock:
        current_balance = balance.value
        time.sleep(random.uniform(0, 0.5))
        balance.value = int(balance.value * 0.9)
        print(f"[Yazıcı proses {decrease_balance.__name__}]: Mevcut bakiye={current_balance}, %10 azaltıldı. Yeni bakiye={balance.value}")

def read_balance(balance, lock, process_id):
    with lock:
        time.sleep(random.uniform(0, 0.5))
        print(f"[Okuyucu proses {process_id}]: Mevcut bakiye={balance.value}")

def main():
    balance = Value('i', 1000)
    lock = Lock()
    processes = []

    processes.append(Process(target=increase_balance, args=(balance, lock)))
    processes.append(Process(target=decrease_balance, args=(balance, lock)))

    n = int(input("Okuyucu proses sayısı n: "))

    for i in range(1, n + 1):
        processes.append(Process(target=read_balance, args=(balance, lock, i)))

    for p in processes:
        p.start()

    for p in processes:
        p.join()

if __name__ == "__main__":
    main()
