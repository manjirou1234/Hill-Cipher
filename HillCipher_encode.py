import numpy as np

# Khởi tạo ma trận khóa K
K = np.random.randint(0, 26, size=(3,3))

# Chuỗi plaintext
plaintext = 'JUSTFORFUN'

# Chuyển plaintext thành dạng số
plaintext_nums = [ord(c) - 65 for c in plaintext]

# Thêm các giá trị 0 vào cuối chuỗi plaintext
while len(plaintext_nums) % 3 != 0:
    plaintext_nums.append(0)

# Chia plaintext thành các khối
plaintext_blocks = [plaintext_nums[i:i+3] for i in range(0, len(plaintext_nums), 3)]

# Áp dụng phép nhân ma trận giữa K và các khối plaintext
cipher_blocks = [np.matmul(K, np.array(block).reshape(3,1)) % 26 for block in plaintext_blocks]

# Chuyển các giá trị trong ma trận kết quả thành các ký tự tương ứng trong bảng chữ cái Alphabet
cipher_nums = [int(num) for block in cipher_blocks for num in block]
ciphertext = ''.join([chr(num + 65) for num in cipher_nums])

print('Ma trận khóa K:\n', K)
print('Plaintext:', plaintext)
print('Ciphertext:', ciphertext)