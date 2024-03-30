import numpy as np
import time

def matrix_multiplication(rows_A, cols_A, rows_B, cols_B):
    A = np.random.rand(rows_A, cols_A)
    B = np.random.rand(rows_B, cols_B)
    
    start_time = time.time()
    result = np.dot(A, B)
    end_time = time.time()
    
    total_time = end_time - start_time
    
    print("Result:")
    print(result)
    print("Total Time:", total_time)


rows_A = int(input("Enter the number of rows for matrix A: "))
cols_A = int(input("Enter the number of columns for matrix A: "))
rows_B = int(input("Enter the number of rows for matrix B: "))
cols_B = int(input("Enter the number of columns for matrix B: "))

matrix_multiplication(rows_A, cols_A, rows_B, cols_B)
