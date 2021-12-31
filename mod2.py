def mul(a, b):
    return a * b

def div(a, b):
    return a / b
'''
__name__변수란?
    : 파이썬의 __name__ 변수는 내부적으로 사용하는 특별한 변수 이름이다.
    만약 콘솔에서 직접 mod2.py를 실행할 경우 해당 변수에는 __main__이 저장된다.
    하지만 import를 하는 경우 모듈이름 값 mod2가 저장된다.
'''
if __name__ == "__main__":
    print("==여긴 mod2.py==")
    print(mul(1, 4))
    print(div(4, 2))

