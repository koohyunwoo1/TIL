number_of_people = 0    # 변수


def increase_user():
    global number_of_people
    number_of_people += 1
    return number_of_people


print('현재 가입된 유저수 : ' , increase_user())
