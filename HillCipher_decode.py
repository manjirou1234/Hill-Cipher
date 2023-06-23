import numpy as np

# Nhập ma trận khóa K
K = np.array([[8, 3, 2], [2, 18, 8], [8, 1, 5]])

# Chuỗi ciphertext
ciphertext = 'WQZQZMYLKV'

# Chuyển các ký tự trong chuỗi ciphertext thành các giá trị tương ứng trong bảng chữ cái Alphabet
ciphertext_nums = [ord(c) - 65 for c in ciphertext]

# Thêm các giá trị 0 vào cuối chuỗi ciphertext
while len(ciphertext_nums) % 3 != 0:
    ciphertext_nums.append(0)

# Chia chuỗi ciphertext thành các khối
ciphertext_blocks = [ciphertext_nums[i:i+3] for i in range(0, len(ciphertext_nums), 3)]

# Tìm các khối plaintext bằng cách áp dụng phép nhân ma trận giữa ma trận khóa K và các khối ciphertext
plaintext_blocks = [np.matmul(np.linalg.inv(K), np.array(block).reshape(3,1)).round().astype(int) % 26 for block in ciphertext_blocks]

# Chuyển các giá trị trong các khối plaintext thành các ký tự tương ứng trong bảng chữ cái Alphabet
plaintext_nums = [int(num) for block in plaintext_blocks for num in block]
plaintext = ''.join([chr(num + 65) for num in plaintext_nums])

print('Ma trận khóa K:\n', K)
print('Ciphertext:', ciphertext)
print('Plaintext:', plaintext)