'''
람다(lambda) 함수
    :def 키워드를 사용하지 않고 식 형식으로 되어있다해서 
    람다식이라고 부르는데, 이름이 없으므로 익명함수로 부르기도 한다.
    lambda키워드를 사용해서 간편하게 작성할 수 있고, 
    재사용되지 않는 1회성 함수를 만들때 사용한다.
'''
# 두 수의 합을 일반적인 함수로 정의
def two_sum(x, y):
    return x + y
print("함수를 통한 두 수의 합=", two_sum(10, 20))

'''
형식]
    람다식 이름 = lambda 매개변수1, 매개변수2 : 실행문장
'''
# 위 two_sum() 함수를 람다식으로 표현하면 아래와 같다.
sum = lambda arg1, arg2: arg1 + arg2
print("람다식을 통한 합=", sum(10, 20))

# 인수를 제곱해서 반환하는 람다식
power = lambda num : num**2
print("5의 제곱은=", power(5))

'''
람다식 자체호출
    : 람다식을 변수에 할당하지 않고, 괄호를 이용해서
    식 자체를 바로 호출할 수 있다.
'''
print("람다식 자체호출=", (lambda x, y: x + y)(100, 200))

'''
map()함수
    :전달된 데이터를 동일 함수에 반복적으로 적용시켜 주는 역할을 한다.
    for문과 같은 반복문을 사용하지 않아도 지정한 함수로 인수를
    여러번 전달해서 그 결과를 list 형태로 반환하는 유용한 함수이다.
    형식]
        map(람다식, 파라미터);
'''
print("### 람다식과 map함수1 ###")
multiLambda = lambda x: x*2 # 인자에 2를 곱한 결과를 반환하는 람다식 정의
list_data = [1,2,3,4,-1,-2,-5,-10] # 리스트 정의
#list_data의 원소 갯수만큼 람다식을 반복 호출하여 얻어진 결과를 리스트로 반환한다.
result_list = list(map(multiLambda, list_data))
print("result_list =", result_list)

'''
람다식에서 조건부 표현식 사용하기
형식]
    실행문1 if 조건식 else 실행문2
    - 조건식이 참일때 실행문1, 거짓일때 실행문2 를 사용한다.
    - 람다식에서 조건부 표현식을 사용할 때는 :을 붙히지 않는다.
    - if를 사용했다면 반드시 else를 사용해야 한다.
    - elif는 사용할 수 없다. 따라서 2개 이상의 조건도 if를 연속으로 사용해야 한다.
'''
print("### 람다식과 map함수2 ###")
list_data2 = [1,2,3,4,5,6,7,8,9,10]
# 인자가 3의 배수인 경우 문자형태로 반환하고, 아니면 숫자 그대로를 반환하는 람다식 정의
strNumLambda = lambda x: str(x) if x%3==0 else x
result_list2 = list(map(strNumLambda, list_data2))
print("result_list2 =", result_list2)
# 출력결과 : 3의 배수는 문자로, 나머지는 숫자로 출력된다.

'''
filter함수 
    : 반복 가능한 객체에서 특정 조건에 맞는 요소만 가져오는데
    지정된 람다식에서 true를 반환하는 것만 해당 요소를 반환한다.
    형식은 map과 동일하다.
'''
print("### 람다식과 filter함수 ###")
powLambda = lambda y : y**2 # 인수를 제곱해서 반환하는 람다식 정의
list_data3 = [1,4,9,16,25,46,64,81,100]
result_list3 = list(map(powLambda, list_data3)) # map을 통해 리스트 원소의 제곱을 구한다.
print("result_list3 =", result_list3)

# 50초과 & 1000미만인 경우에만 true를 반환하는 람다식을 통해 원소를 필터링한다.
filter_result = list(filter(lambda z: z>50 and z<1000, result_list3))
print('filter_result =', filter_result)
# 실행결과 : 81, 256, 625

'''
reduce함수
    : 반복 가능한 객체의 각 요소를 지정된 함수로 처리한 뒤 
    이전 결과와 누적해서 반환하는 함수.
    파이썬 3 부터는 내장 함수가 아니므로 functools모듈을 
    import한 후 사용해야 한다.
'''
print("### 람다식과 reduce함수 ###")
import functools, operator

'''
    1~10까지의 합을 반환한다. 람다식이 두 요소를 더해서 반환하도록
    정의 되었으므로, 처음엔 1과 2가 인수로 주어져 더해지고,
    그 결과에 3을 더하는 구조를 가지게 된다.
'''
sum1 = functools.reduce(lambda i, j: i + j, range(1,11))
print("sum1=", sum1) # 결과 : 55

# operator 모듈의 add() 함수를 사용하여 위와 동일한 결과값을 반환한다.
sum2 = functools.reduce(operator.add, range(1,11))
print("sum2=", sum2) # 결과 : 55






