import sys
input = sys.stdin.readline

T = int(input())
for i in range(T):
    a, b = map(int, input().split())
    reward = 0

    # 1회 상금계산
    if a == 0:
        pass
    elif a <= 1:
        reward += 500
    elif a <= 3:
        reward += 300
    elif a <= 6:
        reward += 200
    elif a <= 10:
        reward += 50
    elif a <= 15:
        reward += 30
    elif a <= 21:
        reward += 10

    # 2회 상금계산
    if b == 0:
        pass
    elif b <= 1:
        reward += 512
    elif b <= 3:
        reward += 256
    elif b <= 7:
        reward += 128
    elif b <= 15:
        reward += 64
    elif b <= 31:
        reward += 32

    print(reward*10000)



"""안 좋은 코드"""
# first_prize=[5000000,3000000,2000000,500000,300000,100000]
# second_prize=[5120000,2560000,1280000,640000,320000]

# def fisrt_find_prize(Rank,li):
#     num = 0
#     if Rank>21: return 0
#     elif Rank==0: return 0
#     else:
#         for i in range(1,len(li)+1):
#             if Rank-i < 0:
#                 return li[num]
#             else:
#                 Rank-=i
#                 num+=1
#         return li[num-1]
    

# def second_find_prize(Rank,li):
#     num=0
#     if Rank>31: return 0
#     elif Rank==0: return 0
#     else:
#         for i in range(len(li)):
#             if Rank-(2**i) < 0:
#                 return li[num]
#             else:
#                 Rank-=2**i
#                 num+=1
#         return li[num-1]

# def hunter(first_rank,first_prize,second_rank,second_prize):
#     first =fisrt_find_prize(first_rank,first_prize)
#     second = second_find_prize(second_rank,second_prize)
#     return first+second

# T = int(input())
# thing = []
# for _ in range(T):
#     thing.append(list(map(int,input().split())))

# for i in range(T):
#     print(hunter(thing[i][0],first_prize,thing[i][1],second_prize))