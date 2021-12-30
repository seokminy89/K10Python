
'''
전역변수와 지역변수
    :파이썬에서는 변수 선언시 자료형을 별도로 기술하지 않으므로
    아래와 같은 경우 함수 밖과 안의 total은 서로 다른 변수가 된다.
'''
total = 0 # 전역변수 선언
def sum(arg1, arg2):
    total = arg1 + arg2 #지역변수 선언
    print("지역변수 total=", total)
    return total

print("전역변수 total=", total) # 초기값 0이 그대로 출력됨
print("sum(10, 20)호출후 반환값=", sum(10, 20)) # 합의 결과 30이 출력됨.
print("=============================")

'''
내부함수
    :파이썬은 함수 내부에 또 다른 함수를 선언할 수 있다.
    형식]
        def 함수명1():
            실행문
            def 함수명2():
                실행문
'''
def commander(saying):
    def inner(quote): #내부함수 정의
        return "조선의 위대한 장군 = '%s'" % quote
    return inner(saying) #내부함수 호출(2차호출)
print(commander("이순신")) #1차 호출
print("=============================")

'''
매개변수를 전달하는 방식에는 4가지가 있다.
1.순서매개변수 : 함수에서 사용하는 일반적인 매개변수로 작성 순서대로 전달된다.
'''
def printme(str1, str2):
    print(str1, str2)
    return
cont = "은 매우 좋은 프로그램입니다."
printme("Python", cont)
print("==============================")

#2.키워드 매개변수 : 순서와 상관없이 매개변수명에 따라 전달된다.
def printinfo(name, age):
    print("이름:", name)
    print("나이:", age)
    return
printinfo(age=50, name='홍길동')
print("==============================")

#3.기본 매개변수 : 인수가 전달되지 않는 경우 디폴트로 지정되는 값을 말한다.
def defaultArgs(lan="Java"):
    print("내가 좋아하는 언어는 : ", lan, "입니다")
    return
defaultArgs() # 이 경우 Java가 출력됨
defaultArgs("C++") # 이 경우 C++이 출력됨
# 만약 Java에서의 호출이라면 첫번째 호출에서 에러가 발생하게 될 것이다.
print("==============================")

'''
4.가변 매개변수
    :여러개의 매개변수를 전달해야 할때 사용하는 매개변수로
    Java의 가변인자와 비슷하다.
    *를 이용해서 매개변수값을 튜플로 그룹화 한다.
    **를 이용해서 매개변수를 딕셔너리로 사용할 수 있다.

'''
def product(*args):
    print("*args => ", args) #튜플 형태로 출력된다.
    result = 1
    for a in args: # 튜플이므로 반복문 사용가능
        result *= a # 각 원소를 통해 누적곱을 계산함
    return result
print("product(1,2,3,4) =", product(1,2,3,4))


def famousMan(**man):
    print('**man', man) # 딕셔너리 형태로 출력된다.
    for key in man: # 딕셔너리는 key를 통해 value를 출력한다.
        print(key, "=>", man[key])
famousMan(의인= '홍길동', 장군='이순신', 임금='세종대왕')

    
defaultArgs()
defaultArgs("C++")
print("==============================")

