import threading
import time

def generate_matrix(rows, cols):
    import random
    return [[random.random() for _ in range(cols)] for _ in range(rows)]

def matrix_multiply_section(A, B, result, row_range, cols_B):
    for row in row_range:
        for col in range(cols_B):
            result[row][col] = sum(A[row][i] * B[i][col] for i in range(len(B)))

def threaded_matrix_multiply(A, B, thread_count):
    rows_A, cols_A = len(A), len(A[0])
    rows_B, cols_B = len(B), len(B[0])
    assert cols_A == rows_B
    
    result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]
    threads = []
    rows_per_thread = rows_A // thread_count
    for i in range(thread_count):
        start_row = i * rows_per_thread

        end_row = (i + 1) * rows_per_thread if i != thread_count - 1 else rows_A
        thread = threading.Thread(target=matrix_multiply_section, args=(A, B, result, range(start_row, end_row), cols_B))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()
    
    return result


rows_A, cols_A = 100, 100
rows_B, cols_B = 100, 100
A = generate_matrix(rows_A, cols_A)
B = generate_matrix(rows_B, cols_B)
thread_count = 4 

start_time = time.time()
result_matrix = threaded_matrix_multiply(A, B, thread_count)
end_time = time.time()


hw2_q2_content = f"""
import threading
import random
import time

def generate_matrix(rows, cols):
    return [[random.random() for _ in range(cols)] for _ in range(rows)]

def matrix_multiply_section(A, B, result, row_range, cols_B):
    for row in row_range:
        for col in range(cols_B):
            result[row][col] = sum(A[row][i] * B[i][col] for i in range(len(B)))

def threaded_matrix_multiply(A, B, thread_count):
    rows_A, cols_A = len(A), len(A[0])
    rows_B, cols_B = len(B), len(B[0])
    assert cols_A == rows_B, "Matrisler çarpılabilir olmalıdır."
    
    result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]
    threads = []
    rows_per_thread = rows_A // thread_count
    for i in range(thread_count):
        start_row = i * rows_per_thread
        end_row = (i + 1) * rows_per_thread if i != thread_count - 1 else rows_A
        thread = threading.Thread(target=matrix_multiply_section, args=(A, B, result, range(start_row, end_row), cols_B))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()
    
    return result

rows_A, cols_A = 100, 100
rows_B, cols_B = 100, 100
A = generate_matrix(rows_A, cols_A)
B = generate_matrix(rows_B, cols_B)
thread_count = 4

start_time = time.time()
result_matrix = threaded_matrix_multiply(A, B, thread_count)
end_time = time.time()

print(f"Çarpma işleminin süresi: {end_time - start_time} saniye.")
"""


file_path_2 = '/Users/senakurtak/Repo/operating-systems/hw2_q2.py'
with open(file_path_2, 'w') as file:
    file.write(hw2_q2_content)

file_path_2, end_time - start_time
