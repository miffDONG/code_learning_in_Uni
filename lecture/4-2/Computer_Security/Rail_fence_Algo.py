def encrypt_rail_fence(text, key):
    # 암호화를 위한 레일 행렬 생성
    rail = [['\n' for i in range(len(text))] for j in range(key)]
    print("encrytion process 1 result")
    for row in rail:
        print(row)
    print("")

    dir_down = False
    row, col = 0, 0
    
    # 레일 행렬 채우기
    for i in range(len(text)):
        if (row == 0) or (row == key - 1):
            dir_down = not dir_down
        
        rail[row][col] = text[i]
        col += 1
        
        if dir_down:
            row += 1
        else:
            row -= 1
    print(f"encrytion process 2 result")
    for row in rail:
        print(row)
    print("")
    # 암호문 생성
    result = []
    for i in range(key):
        for j in range(len(text)):
            if rail[i][j] != '\n':
                result.append(rail[i][j])
    print("encrytion process 3 result")
    for row in rail:
        print(row)
    print("")
    return "".join(result)

def decrypt_rail_fence(cipher, key):
    # 복호화를 위한 레일 행렬 생성
    rail = [['\n' for i in range(len(cipher))] for j in range(key)]
    print("decrytion process 1 result")
    for row in rail:
        print(row)
    print("")
    dir_down = None
    row, col = 0, 0
    
    # 레일 행렬에 마커 표시
    for i in range(len(cipher)):
        if row == 0:
            dir_down = True
        if row == key - 1:
            dir_down = False
        
        rail[row][col] = '*'
        col += 1
        
        if dir_down:
            row += 1
        else:
            row -= 1
    print("decrytion process 2 result")
    for row in rail:
        print(row)
    print("")

    # 레일 행렬 채우기
    index = 0
    for i in range(key):
        for j in range(len(cipher)):
            if rail[i][j] == '*' and index < len(cipher):
                rail[i][j] = cipher[index]
                index += 1

    # 복호화된 텍스트 생성
    result = []
    row, col = 0, 0
    for i in range(len(cipher)):
        if row == 0:
            dir_down = True
        if row == key - 1:
            dir_down = False
        
        if rail[row][col] != '*':
            result.append(rail[row][col])
            col += 1
        
        if dir_down:
            row += 1
        else:
            row -= 1
    print("decrytion process 3 result")
    for row in rail:
        print(row)
    print("")
    return "".join(result)

# 테스트

test_ex1 = "attack at once"
enc_ex1 = encrypt_rail_fence(test_ex1, 2)
dec_ex1 = decrypt_rail_fence(enc_ex1, 2)

print(f"text : {test_ex1}")
print(f"encryted Cypher : {enc_ex1}")
print(f"decryted text : {dec_ex1}")