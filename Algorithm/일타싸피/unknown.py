import socket
import time
import math

# 닉네임을 사용자에 맞게 변경해 주세요.
NICKNAME = 'unknown'

# 일타싸피 프로그램을 로컬에서 실행할 경우 변경하지 않습니다.
HOST = '127.0.0.1'

# 일타싸피 프로그램과 통신할 때 사용하는 코드값으로 변경하지 않습니다.
PORT = 1447
CODE_SEND = 9901
CODE_REQUEST = 9902
SIGNAL_ORDER = 9908
SIGNAL_CLOSE = 9909

# 게임 환경에 대한 상수입니다.
TABLE_WIDTH = 254
TABLE_HEIGHT = 127
NUMBER_OF_BALLS = 6
HOLES = [[0, 0], [127, 0], [254, 0], [0, 127], [127, 127], [254, 127]]

order = 0
balls = [[0, 0] for i in range(NUMBER_OF_BALLS)]

sock = socket.socket()
print('Trying to Connect: %s:%d' % (HOST, PORT))
sock.connect((HOST, PORT))
print('Connected: %s:%d' % (HOST, PORT))

send_data = '%d/%s' % (CODE_SEND, NICKNAME)
sock.send(send_data.encode('utf-8'))
print('Ready to play!\n--------------------')


def find_ball(balls, order):
    """
    선공일 경우 3번 공을 우선 타겟
    후공이면 2번을 우선 타겟
    """
    if order == 1:
        if balls[3][0] != -1 and balls[3][1] != -1:
            return 3
        elif balls[1][0] != -1 and balls[1][1] != -1:
            return 1
        else:
            return 5
    else:
        if balls[2][0] != -1 and balls[2][1] != -1:
            return 2
        elif balls[4][0] != -1 and balls[4][1] != -1:
            return 4
        else:
            return 5


def find_hole(start, end):
    """
    흰공과 표적구의 상대위치에 따라 공을 넣을 홀을 선택함
    """
    # 1 사분면
    if start[0] < end[0] and start[1] < end[1]:
        if end[0] < 127.0:
            hole = HOLES[4]
        else:
            hole = HOLES[5]
    # 2 사분면
    elif start[0] < end[0] and start[1] > end[1]:
        if end[0] < 127.0:
            hole = HOLES[1]
        else:
            hole = HOLES[2]
    # 3 사분면
    elif start[0] > end[0] and start[1] > end[1]:
        if end[0] > 127.0:
            hole = HOLES[1]
        else:
            hole = HOLES[0]
    # 4 사분면
    else:
        if end[0] > 127.0:
            hole = HOLES[4]
        else:
            hole = HOLES[3]

    return hole


while True:

    # Receive Data
    recv_data = (sock.recv(1024)).decode()
    print('Data Received: %s' % recv_data)

    # Read Game Data
    split_data = recv_data.split('/')
    idx = 0
    try:
        for i in range(NUMBER_OF_BALLS):
            for j in range(2):
                balls[i][j] = float(split_data[idx])
                idx += 1
    except:
        send_data = '%d/%s' % (CODE_REQUEST, NICKNAME)
        print("Received Data has been currupted, Resend Requested.")
        continue

    # Check Signal for Player Order or Close Connection
    if balls[0][0] == SIGNAL_ORDER:
        order = int(balls[0][1])
        print('\n* You will be the %s player. *\n' % ('first' if order == 1 else 'second'))
        continue
    elif balls[0][0] == SIGNAL_CLOSE:
        break

    # Show Balls' Position
    print('====== Arrays ======')
    for i in range(NUMBER_OF_BALLS):
        print('Ball %d: %f, %f' % (i, balls[i][0], balls[i][1]))
    print('====================')

    angle = 0.0
    power = 0.0

    ##############################
    # 이 위는 일타싸피와 통신하여 데이터를 주고 받기 위해 작성된 부분이므로 수정하면 안됩니다.
    #
    # 모든 수신값은 변수, 배열에서 확인할 수 있습니다.
    #   - order: 1인 경우 선공, 2인 경우 후공을 의미
    #   - balls[][]: 일타싸피 정보를 수신해서 각 공의 좌표를 배열로 저장
    #     예) balls[0][0]: 흰 공의 X좌표
    #         balls[0][1]: 흰 공의 Y좌표
    #         balls[1][0]: 1번 공의 X좌표
    #         balls[4][0]: 4번 공의 X좌표
    #         balls[5][0]: 마지막 번호(8번) 공의 X좌표

    # 여기서부터 코드를 작성하세요.
    # 아래에 있는 것은 샘플로 작성된 코드이므로 자유롭게 변경할 수 있습니다.

    # 충돌구
    start = balls[0]
    # 표적구
    ball = balls[find_ball(balls, order)]
    # 홀
    end = find_hole(start, ball)

    # 홀 ~ 충돌구
    a = [end[0] - start[0], end[1] - start[1]]
    # 홀 ~ 표적구
    b = [end[0] - ball[0], end[1] - ball[1]]
    # 표적구 ~ 충돌구
    c = [ball[0] - start[0], ball[1] - start[1]]

    r = 5.73

    # 충돌지점
    b = [b[0] + ((b[0] * r) / ((b[0] ** 2 + b[1] ** 2) ** 0.5)), b[1] + ((b[1] * r) / ((b[0] ** 2 + b[1] ** 2) ** 0.5))]
    # 충돌지점 ~ 충돌구
    c = [a[0] - b[0], a[1] - b[1]]
    
    # 각도 연산
    theta = math.atan(c[1] / c[0])
    theta = math.degrees(theta)
    angle = 90 - theta

    # 흰공 기준 표적구가 왼쪽일 경우 각도 처리
    if c[0] < 0:
        angle += 180

    # 흰공 ~ 충돌지점까지 거리
    dis = (c[0] ** 2 + c[1] ** 2) ** 0.5
    # 표적구 ~ 홀까지 거리
    nd = (b[0] ** 2 + b[1] ** 2) ** 0.5

    # 거리에 따라 힘조절
    power = dis * 0.7

    # 힘이 너무 작으면 10만큼 추가
    if power < 20:
        power += 10

    elif power < 10:
        power += 20

    if power == 100:
        angle -= 0.05
        power = 95

    # 표적구 ~ 홀거리가 너무 멀면 힘 추가
    if nd > 180:
        power += 5

    # 주어진 데이터(공의 좌표)를 활용하여 두 개의 값을 최종 결정하고 나면,
    # 나머지 코드에서 일타싸피로 값을 보내 자동으로 플레이를 진행하게 합니다.
    #   - angle: 흰 공을 때려서 보낼 방향(각도)
    #   - power: 흰 공을 때릴 힘의 세기
    #
    # 이 때 주의할 점은 power는 100을 초과할 수 없으며,
    # power = 0인 경우 힘이 제로(0)이므로 아무런 반응이 나타나지 않습니다.
    #
    # 아래는 일타싸피와 통신하는 나머지 부분이므로 수정하면 안됩니다.
    ##############################

    merged_data = '%f/%f/' % (angle, power)
    sock.send(merged_data.encode('utf-8'))
    print('Data Sent: %s' % merged_data)

sock.close()
print('Connection Closed.\n--------------------')