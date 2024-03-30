import random
import time

def generate_matrix(rows, cols):
    return [[random.random() for _ in range(cols)] for _ in range(rows)]

def matrix_multiply(A, B):
    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
    return result

# Örnek matris boyutları (küçük boyutlarla başlayarak test edelim)
rows_A, cols_A = 2, 3  # A Matrisi için satır ve sütun sayısı
rows_B, cols_B = 3, 2  # B Matrisi için satır ve sütun sayısı

# Matrisleri Oluştur
A = generate_matrix(rows_A, cols_A)
B = generate_matrix(rows_B, cols_B)

# Matris Çarpımı ve Süre Ölçümü
start_time = time.time()
result_matrix = matrix_multiply(A, B)
end_time = time.time()

# Süre ve sonuç matrisinin boyutu (test amaçlı)
total_time = end_time - start_time
result_matrix_size = (len(result_matrix), len(result_matrix[0])) if result_matrix else (0, 0)

total_time, result_matrix_size
