from fractions import Fraction
import time,random


def factorial(n):                #펙토리얼 계산 함수 O(n)
    mul=1
    if n!=1:                     # n = 1인 경우는 1을 return 아닌 경우는 1~n까지 곱셈 후 return
        for i in range(1,n+1):
            mul=mul*i
    return mul

def computer_e_ver1(n):          # 오일러 수 구하는 함수 1
    sum = 1/1                    # n = 0인 경우는 고려하지 않음. 
    for i in range(1,n):         # 1~n까지 반복. O(n)
        number= 1/factorial(i)   # factorial 함수 호출 O(n^2)
        sum = sum + number
    return sum


def computer_e_ver2(n):         # 오일러 수 구하는 함수 2
    sum = 1/1                   # n = 0인 경우 고려하지 않음.
    factorial = 1/1             # factorial 선언 후, n번째 항 = (n-1)항 * 1/n 방식 사용.
    if n!=1:
        for i in range(1,n):    # O(n)
            factorial = factorial * 1/i
            sum = sum + factorial
    return sum


# print(computer_e_ver1(5))
# before1 = time.process_time()
# test1=computer_e_ver1(5000)
# after1 = time.process_time()
# print("version1")
# print(test1)
# print(after1 - before1)

# before2 = time.process_time()
# test2=computer_e_ver2(5000)
# after2 = time.process_time()
# print("version2")
# print(test2)
# print(after2 - before2)


# #####################          1000          ###########################
# before1 = time.process_time()
# test1=computer_e_ver1(1000)
# after1 = time.process_time()
# print("1000 version1")
# print(test1)
# print(after1 - before1)

# before2 = time.process_time()
# test2=computer_e_ver2(1000)
# after2 = time.process_time()
# print("1000 version2")
# print(test2)
# print(after2 - before2)

# #####################          2500         ###########################
# before1 = time.process_time()
# test1=computer_e_ver1(2500)
# after1 = time.process_time()
# print("2500 version1")
# print(test1)
# print(after1 - before1)

# before2 = time.process_time()
# test2=computer_e_ver2(2500)
# after2 = time.process_time()
# print("2500 version2")
# print(test2)
# print(after2 - before2)
# #####################           7500       #############################
# before1 = time.process_time()
# test1=computer_e_ver1(7500)
# after1 = time.process_time()
# print("7500 version1")
# print(test1)
# print(after1 - before1)

#########################          ver2 test       ###################
# # #####################          100000          ###########################
# before2 = time.process_time()
# test2=computer_e_ver2(100000)
# after2 = time.process_time()
# print("100000 version2")
# print(test2)
# print(after2 - before2)

# # #####################          200000          ###########################
# before2 = time.process_time()
# test2=computer_e_ver2(200000)
# after2 = time.process_time()
# print("200000 version2")
# print(test2)
# print(after2 - before2)

# # #####################          300000          ###########################
# before2 = time.process_time()
# test2=computer_e_ver2(300000)
# after2 = time.process_time()
# print("300000 version2")
# print(test2)
# print(after2 - before2)

# # #####################          400000          ###########################
# before2 = time.process_time()
# test2=computer_e_ver2(400000)
# after2 = time.process_time()
# print("400000 version2")
# print(test2)
# print(after2 - before2)

# # #####################          500000          ###########################
# before2 = time.process_time()
# test2=computer_e_ver2(500000)
# after2 = time.process_time()
# print("500000 version2")
# print(test2)
# print(after2 - before2)

#####################       ver1 test     ##################
#####################           1000       #############################
before1 = time.process_time()
test1=computer_e_ver1(10000)
after1 = time.process_time()
print("1000 version1")
print(test1)
print(after1 - before1)

# #####################           2000       #############################
# before1 = time.process_time()
# test1=computer_e_ver1(2000)
# after1 = time.process_time()
# print("2000 version1")
# print(test1)
# print(after1 - before1)

# #####################           3000       #############################
# before1 = time.process_time()
# test1=computer_e_ver1(3000)
# after1 = time.process_time()
# print("3000 version1")
# print(test1)
# print(after1 - before1)

# #####################           4000       #############################
# before1 = time.process_time()
# test1=computer_e_ver1(4000)
# after1 = time.process_time()
# print("4000 version1")
# print(test1)
# print(after1 - before1)

# #####################           5000       #############################
# before1 = time.process_time()
# test1=computer_e_ver1(5000)
# after1 = time.process_time()
# print("5000 version1")
# print(test1)
# print(after1 - before1)

# #####################           6000       #############################
# before1 = time.process_time()
# test1=computer_e_ver1(6000)
# after1 = time.process_time()
# print("6000 version1")
# print(test1)
# print(after1 - before1)

# #####################           7000       #############################
# before1 = time.process_time()
# test1=computer_e_ver1(7000)
# after1 = time.process_time()
# print("7000 version1")
# print(test1)
# print(after1 - before1)

# #####################           8000       #############################
# before1 = time.process_time()
# test1=computer_e_ver1(8000)
# after1 = time.process_time()
# print("8000 version1")
# print(test1)
# print(after1 - before1)

# #####################           9000       #############################
# before1 = time.process_time()
# test1=computer_e_ver1(9000)
# after1 = time.process_time()
# print("9000 version1")
# print(test1)
# print(after1 - before1)