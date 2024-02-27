############# 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
def is_id_valid(user):
    if user['id'][-1].isdigit():
        return True
    else:
        return False

    

# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############# 테스트 코드 삭제 금지 #################
user_data1 = {
    'id': 'jungssafy5',
    'password': '1q2w3e4r',
}
print(is_id_valid(user_data1)) # True

user_data2 = {
    'id': 'kimssafy!',
    'password': '1q2w3e4r',
}
print(is_id_valid(user_data2)) # False
# ####################################################
