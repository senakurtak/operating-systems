
def generate_matrix(rows, cols):

    import random
    return [[random.random() for _ in range(cols)] for _ in range(rows)]

def matrix_multiply(A, B):
    result = [[sum(a*b for a, b in zip(A_row, B_col)) for B_col in zip(*B)] for A_row in A]
    return result


import time


rows_A, cols_A = 100, 100
rows_B, cols_B = 100, 100


A = generate_matrix(rows_A, cols_A)
B = generate_matrix(rows_B, cols_B)


start_time = time.time()
result_matrix = matrix_multiply(A, B)
end_time = time.time()

total_time = end_time - start_time


hw1_q1_content = f"""
import random
import time

def generate_matrix(rows, cols):
    return [[random.random() for _ in range(cols)] for _ in range(rows)]

def matrix_multiply(A, B):
    result = [[sum(a*b for a, b in zip(A_row, B_col)) for B_col in zip(*B)] for A_row in A]
    return result

rows_A, cols_A = 100, 100
rows_B, cols_B = 100, 100

A = generate_matrix(rows_A, cols_A)
B = generate_matrix(rows_B, cols_B)

start_time = time.time()
result_matrix = matrix_multiply(A, B)
end_time = time.time()

print(f"Çarpma işleminin süresi: {end_time - start_time} saniye.")
"""


file_path = '/Users/senakurtak/Repo/operating-systems/hw1_q1.py'
with open(file_path, 'w') as file:
    file.write(hw1_q1_content)

file_path, total_time
