import multiprocessing
import time
import random

def writer_process(balance, lock):
    while True:
        with lock:
            balance.value -= 100
            print(f"[Writer process]: Current balance={balance.value + 100}, Decreased by 10%. New balance={balance.value}")
        time.sleep(random.uniform(0, 5))

def reader_process(balance, lock, id):
    while True:
        with lock:
            print(f"[Reader process {id}]: Current balance={balance.value}")
        time.sleep(random.uniform(0, 5))

if __name__ == "__main__":
    balance = multiprocessing.Value('i', 1000)
    lock = multiprocessing.Lock()

    writer1 = multiprocessing.Process(target=writer_process, args=(balance, lock))
    writer2 = multiprocessing.Process(target=writer_process, args=(balance, lock))
    reader_processes = [multiprocessing.Process(target=reader_process, args=(balance, lock, i)) for i in range(1, 5)]

    writer1.start()
    writer2.start()
    for reader in reader_processes:
        reader.start()

    writer1.join()
    writer2.join()
    for reader in reader_processes:
        reader.join()
