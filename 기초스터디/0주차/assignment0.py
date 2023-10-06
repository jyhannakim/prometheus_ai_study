# # 주의: 기존 코드를 수정하지 마세요.
# # 주석을 통해 코드를 설명하는 것을 권장합니다.
# # 세미 콜론(;)을 통한 코드 이어 붙이기는 금지입니다.

# # Problem 1
# # 내부 코드는 오로지 한 줄이어야 합니다.
# # Hint: max 함수에 대해 알아보세요.
def p1(X):
    return [max(row, key=lambda x: sum(int(num) for num in str(x))) for row in X]

#Problem 2
# 내부 코드는 최대 세 줄이어야 합니다.
def p2(idx):
    idx = [i for i in idx if i>=0] #음수 삭제
    size = max(idx) + 1
    
    answer = []
    for i in idx:
        lst = []
        for k in range(size):
            if k == i:
                lst.append(1)
            else:
                lst.append(0)
                
        answer.append(lst)
    return answer   

#def p2(nums):
#    nums = [n for n in nums if n >= 0]  # 음수 제거
#    size = max(nums) + 1  # 0부터 최대값까지의 크기를 구함
#    return [[1 if i == n else 0 for i in range(size)] for n in nums]


# Problem 3
# 내부 코드는 최대 네 줄이어야 합니다.
# Hint: sample과 data의 크기가 클 수 있기 때문에 효율적인 자료구조를 사용하세요.

def p3(sample, data):
    last_name = [i[0] for i in data]
    first_name = [i[1:] for i in data]

    lst = []
    for i in sample:
        if i[0] in last_name and i[1:] in first_name:
            lst.append(bool(True))
        else:
            lst.append(bool(False))
    return lst
    
# Problem 4
# 내부 코드는 최대 여섯 줄이어야 합니다.

def p4(sample, data):
    pass
    
    

