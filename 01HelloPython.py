# 라인단위 주석은 #(샵)을 사용한다.
'''
블럭단위주석은 싱글쿼테이션을 3개 연결한다.
'''
'''이미 작성한 문장을 주석으로 하고싶으면
블럭으로 설정한(드래그한)후 싱글을 3개 써도 된다.'''

#파이썬은 문장의 끝에 ;(세미콜론)을 사용하지 않는다.
print("Hello Python")
#한줄에 여러 명령을 쓰는 경우 ;으로 구분해야 한다. 역시 가장 마지막엔 세미콜론x
print("한줄에 "); print("여러줄 쓰려면 "); print("세미콜론이 필요함 ")

print("====================")
print("여러 변수 선언")
print("====================")
# 좌측항은 변수, 우측한은 할당할 값으로 구분하여 선언 및 초기화한다.
r, g, b ="Red","Green","Blue"
# 여러개의 변수를 출력할때는 콤마를 통해 구분한다.
print(r,g,b)


print("====================")
print("정수형")
print("====================")
# 파이썬은 변수 선언시 별도의 데이터형을 붙이지 않는다.
x = 2
y = 4
z = 8

print("x / y", x / y) #나누기. 항상 float형 결과를 반환한다.(소수점도 표현함.) 결과 0.5
print("x // y", x // y) #나누기. 소수부분을 제거하므로 항상 int형의 결과를 반환한다. 결과0나옴
print("x * y", x * y)
print("x ** y", x ** y) #거듭제곱 2의 4승을 계산한다.
print("pow(x, y)", pow(x, y)) #함수를 통해 거듭제곱을 계산한다.
print("pow(x, y, z)", pow(x, y, z)) #2의 4승을 8로 나눈 나머지를 반환한다. 결과값 0
print("divmod(x, y)", divmod(x, y)) #x와 y를 나눈 몫과 나머지를 튜플로 반환한다.

# import는 모듈을 불러올때 사용하는 명령으로 math모듈을 사용한다는 의미.
import math
print("math.factorial(5)", math.factorial(5))

print("====================")
print("String형")
print("====================")
str = """아래와 같이
여러줄에 걸쳐 문자열을 작성하고 싶으면
이와같이 더블쿼테이션을 3개 작성한다.
"""

print(str)

head = "나는 헤더 "
bottom = "나는 보텀 "
print(head + bottom) #문자열 합치기(덧셈 기호 사용)
print(head *3) #문자열 반복하기(곱셈 기호 사용)

# 문자열 슬라이싱 : 인덱스와 범위를 통해 접근할 수 있다.
engStr = "Hello Python Good"
print(engStr[0]) #0번 인덱스 : H
print(engStr[:3]) #0~3미만 즉 0,1,2 번 인덱스 : Hel
print(engStr[1:3]) #1~2미만 즉 1,2 번 인덱스 : el
print(engStr[1:]) #1~마지막까지 가져온다. :ello Python Good

korStr = "안녕하세요? 파이썬입니다."
print(korStr[0]) #안
print(korStr[:2]) #안녕
print(korStr[0:6]) #안녕하세요?

'''
format()
    : 문자열의 format()함수를 사용하면 좀 더 발전된 스타일로
    문자열 포맷을 지정할 수 있다.
'''
# 인덱스를 사용하는 방법
print("{0}는 중복되지 않는 숫자 {1}개로 구성된다".format("Lotto",6))
print("{1}는 중복되지 않는 숫자 {0}개로 구성된다".format("Lotto",6))

# 인덱스 대신 변수를 사용하는 방법. 단 default 값을 지정할때는 "변수명=값" 으로 사용한다.
menu1= "치킨"
menu2= "맥주"
print("오늘 {str}은 {0}과 {1}로 정했다".format(menu1, menu2, str="저녁"))



