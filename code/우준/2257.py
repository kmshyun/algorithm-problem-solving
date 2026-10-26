s = input()
e = {"H" : 1, "C" : 12, "O" : 16}
ch = 0
bch = 0
stack = []
bracket_stack = []
braket = False

for i in s:
    if i in e:
        if braket:
            stack.append(i)
        else:
            bracket_stack.append(i)
    elif i == '(':
        braket = True
    elif i == ')':
        braket = False
        for i in bracket_stack:
            bch += e[i]
        ch += bch
        bch = 0
        bracket_stack = []

    else: # 숫자
        if braket:
            k = bracket_stack.pop()
            bch += k * i
        else:
            k = stack.pop()
            ch += k * i

'''
e에 있는 애가 오면
스택에 분자량 append
숫자가 오면 pop 후 숫자에 곱해 화학식량에 더하기
괄호는 괄호만 받는 스택 따로 만들어놓기
괄호가 오면
괄호가 닫히기 전까지 따로 처리한 후
스택에 넣기
그 후 괄호스택은 비워둬야함 ([]로 초기화하기!)
끝까지 pop이 안된 아이들은 계수가 1임
= 마지막에 다 더해주기

ex)

CO2
[C], s = 0
[C O], s = 0
[C], s = 32
[], s = 44


H(CO2)2
[H], s = 0
[H] [C]
[H] [C O]
[H] [C] 32
[H] [] 44
[H] 88
[] 89
'''