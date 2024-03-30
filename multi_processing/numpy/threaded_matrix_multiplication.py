import numpy as np
import threading
import time

def matrix_multiplication_threaded(rows_A, cols_A, rows_B, cols_B, num_threads):
    A = np.random.rand(rows_A, cols_A)
    B = np.random.rand(rows_B, cols_B)
    
    def multiply_part(start, end, result):
        for i in range(start, end):
            result[i] = np.dot(A[i], B)
    
    result = [None] * rows_A
    thread_list = []
    chunk_size = rows_A // num_threads
    
    start_time = time.time()
    for i in range(num_threads):
        start = i * chunk_size
        end = (i + 1) * chunk_size if i < num_threads - 1 else rows_A
        thread = threading.Thread(target=multiply_part, args=(start, end, result))
        thread_list.append(thread)
        thread.start()
    
    for thread in thread_list:
        thread.join()
    
    end_time = time.time()
    total_time = end_time - start_time
    
    print("Result:")
    print(np.array(result))
    print("Total Time:", total_time)


rows_A = int(input("Enter the number of rows for matrix A: "))
cols_A = int(input("Enter the number of columns for matrix A: "))
rows_B = int(input("Enter the number of rows for matrix B: "))
cols_B = int(input("Enter the number of columns for matrix B: "))
num_threads = int(input("Enter the number of threads: "))

matrix_multiplication_threaded(rows_A, cols_A, rows_B, cols_B, num_threads)
