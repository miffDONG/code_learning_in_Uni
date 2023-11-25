import sys
input = sys.stdin.readline
import copy
friends_jisu= {}
friends_give_take={}
friends_name = []


import sys
input = sys.stdin.readline

def solution(friends, gifts):
    friends_jisu= {}
    friends_give_take={}

    for i in friends:
        friends_jisu[i] = 0
        friends_give_take[i] = {}

    info = {name : 0 for name in friends}
    
    print(friends_jisu)

    # 선물 내역 저장
    for key, _ in friends_give_take.items():
        friends_give_take[key] = copy.deepcopy(info)
    
    for i in gifts:
        ing , ed = i.split(' ')
        friends_jisu[ing] +=1
        friends_jisu[ed] -=1

        friends_give_take[ing][ed] +=1

    print(friends_give_take)

    n_n = [[0 for _ in range(len(friends))] for _ in range(len(friends))] # 둘 사이 확인 기록
    num_take = [0 for _ in range(len(friends))]
    for i in range(len(friends)):
        for j in range(i+1,len(friends)):
            if n_n[i][j] == 0 and n_n[j][i] == 0: # 아직 둘 사이를 안 봤으면
                fr1 = friends_give_take[friends[i]][friends[j]]
                fr2 = friends_give_take[friends[j]][friends[i]]             
                if (fr1 == 0 and fr2 == 0) or fr1 == fr2: # 주고 받은 적 x or 주고 받은 수 같을 때
                    if friends[friends[i]] > friends[friends[j]]:
                        num_take[i] +=1
                    else: num_take[j] +=1
                else:
                    if fr1 > fr2:
                        num_take[i] +=1
                    else: num_take[j] +=1
                n_n[i][j] = 1
                n_n[j][i] = 1
            else:
                pass

    answer = max(num_take)

    answer=0
    return answer


print(solution(["a","b","c"] ,["a b","b a","c a","b c"]))
