import random
import time

def generate_matrix(rows, cols):
    # Generate a matrix filled with random numbers between 0 and 1
    return [[random.randint(0, 1) for _ in range(cols)] for _ in range(rows)]

def matrix_multiplication(A, B):
    # Matrix multiplication logic
    result = [[sum(a*b for a, b in zip(A_row, B_col)) for B_col in zip(*B)] for A_row in A]
    return result

# Example matrix sizes (Can be replaced with user input)
rows_A, cols_A = 100, 100  # Dimensions for matrix A
rows_B, cols_B = 100, 100  # Dimensions for matrix B (cols_A must be equal to rows_B for multiplication)

# Generate matrices A and B
A = generate_matrix(rows_A, cols_A)
B = generate_matrix(rows_B, cols_B)

# Measure the time taken to multiply the matrices
start_time = time.time()
result_matrix = matrix_multiplication(A, B)
end_time = time.time()

# Calculate the duration of the multiplication
duration = end_time - start_time

# Output the duration of the operation
duration
print(duration)
