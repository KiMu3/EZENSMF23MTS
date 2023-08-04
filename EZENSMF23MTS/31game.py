import random

AID = {0:3, 1:2, 2:1, 3:2}
player = True
start = 1
count = 31

print('베스킨라빈스31 게임을 시작합니다.')
print('')
print('[ 규칙 설명 ]')
print(' 1. 플레이어와 봇은 1부터 31까지의 숫자를 번갈아 말합니다.')
print(' 2. 어느 한 쪽이 31을 말하면 그쪽이 패배합니다.')
print(' 3. 플레이어는 반드시 선공으로 시작합니다.')
print('')
print('행운을 빕니다.')
print('')

while count>0:
    if player:
        print('')
        print(' < 플레이어의 차례 >')
        n = 0
        while True:
            n = input('숫자를 몇 개 말할까요? (1~3 중 입력해주세요.): ')
            if n in ['1', '2', '3']:
                n = int(n)
                break
            else:
                print('잘못 입력하셨습니다.')
        for i in range(n):
            print(start)
            start += 1
            count -+ 1
            if start > 31:
                break
        if start > 31:
            break
        player = False
    else:
        print('')
        print('< 봇의 차례 >')
        na = count%4
        if na == 1:
            n = random.randint(1,3)
        else:
            n = AID[na]
        print('봇이 말한 숫자 수 : ', n)
        for i in range(n):
            print(start)
            start += 1
            count -= 1
            if start > 31:
                break
        if start > 31:
            break
        player = True