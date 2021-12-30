'''
함수
    형식] def 함수명(매개변수1, 매개변수2):
            실행부
            return 결과1, 결과2
        return문은 경우에 따라 생략할 수 있다.
        또한 2개 이상의 결과를 콤마로 구분하여 반환할 수 있고.
        반환값은 튜플로 받을 수 있다.
        
        아래는 계산기를 구현해본 예제.
'''

# 메뉴출력 및 선택용 함수 정의
def menu():
    print('메뉴 중 숫자를 선택하세요:')
    print('1.덧셈 2.뺄셈 3.곱셈 4.나눗셈')
    print('5.종료')
    return input('번호선택:') # 사용자가 입력한 번호가 반환된다.

# 사칙연산 용도의 함수 정의
def add(a, b):
    print(a, "+", b, '=', a+b)
def sub(a, b):
    print(a, "-", b, '=', a-b)
def mul(a, b):
    print(a, "*", b, '=', a*b)
def div(a, b):
    print(a, "/", b, '=', a/b)

# loop가 1일때 지속적으로 수행 가능한 반복문을 생성(무한루프)
loop = 1
choice = 0
while loop==1:
    choice = int(menu()) #메뉴출력 및 번호입력
    if choice == 1:
        add(int(input("덧셈 a= ")), int(input("b=")))
    elif choice == 2:
        sub(int(input("뺄셈 a= ")), int(input("b=")))
    elif choice == 3:
        mul(int(input("곱셈 a= ")), int(input("b=")))
    elif choice == 4:
        div(int(input("나눗셈 a= ")), int(input("b=")))
    elif choice == 5: #사용자가 5를 입력하면 while문 탈출
        loop = 0
print("연산 종료!!")

# 2개 이상의 반환값을 가진 함수 정의
def min_max(num):
    # 매개변수로 전달된 튜플의 원소를 더해 누적합을 구함.
    sum = 0
    for val in num:
        sum += val
    # 파이썬에 내장된 최대, 최소값을 구하는 함수를 통해 결과 구함
    return sum, min(num), max(num)

# 인자로 사용할 튜플 생성
numbers = (8,7,6,8,4,9,5)

# 반환값의 갯수만큼 변수를 선언한 후 함수 호출
sumval, minval, maxval = min_max(numbers)
print("튜플의합, 최대값, 최소값:", sumval, minval, maxval)
    
