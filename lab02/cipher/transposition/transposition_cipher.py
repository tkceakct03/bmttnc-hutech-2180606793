class TranspositionCipher:

    def __init__(self):
        pass
    
    def encrypt(self, text, key):
        encrypted_text = ""
        for col in range(key):
            pointer = col
            while pointer < len(text):
                encrypted_text += text[pointer]
                pointer += key
        return encrypted_text
       
    # def decrypt(self, text, key):
    #     decrypted_text = [''] * key
    #     row, col = 0, 0
    #     for symbol in text:
    #         decrypted_text[col] += symbol
    #         col += 1
    #         if col == key or (col == key - 1 and row >= len(text) % key):
    #             col = 0
    #             row += 1
    #     return ''.join(decrypted_text)
       
    def decrypt(self, text, key):
        # Tính số hàng và số cột của ma trận
        num_rows = (len(text) + key - 1) // key
        num_cols = key
        # Tạo ma trận rỗng
        matrix = [['' for _ in range(num_cols)] for _ in range(num_rows)]
        # Điền dữ liệu từ text vào ma trận theo chiều dọc
        row, col = 0, 0
        for symbol in text:
            matrix[row][col] = symbol
            row += 1
            if row == num_rows:
                row = 0
                col += 1
        # Tạo chuỗi giải mã từ ma trận
        decrypted_text = ''
        for r in range(num_rows):
            for c in range(num_cols):
                decrypted_text += matrix[r][c]
        return decrypted_text