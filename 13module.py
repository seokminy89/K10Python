'''
모듈
    :다른 파이썬 프로그램에서 불러와 사용할 수 있게끔 만든 파이썬 파일로
    함수나 변수 또는 클래스를 모아놓은 것을 말한다.
    모듈을 모아 놓은것을 패키지라고 한다.
    
    형식]
        import 모듈명
        from 모듈명 import 함수
'''
# 모듈 사용방법1 : 함수 호출 시 모듈명을 같이 기술한다.
import mod1
print("모듈의 함수호출1 :", mod1.add(3, 4))
print("모듈의 함수호출2 :", mod1.sub(4, 2))

# 모듈 사용방법2 : 이와 같이 하면 함수 호출 시 모듈명을 생략할 수 있다.
from mod1 import add
result = add(3, 4)
print("결과 :", result)

# 방법2와 동일하지만 모든 함수를 한꺼번에 임포트 하는 방식이다.
from mod1 import *
result1 = add(3, 4)
print("결과 :", result1)
result2 = sub(3, 4)
print("결과 :", result2)

'''
__name__ 변수를 사용한 모듈로 이와 같이 import를 하게되면
"mod2"가 저장된다.
'''
import mod2
result = mod2.mul(3, 4)
print(result)

# 모듈을 나눠서 관리할때는 패키지를 사용한다.
import kosmo.mod3
kosmo.mod3.sum1To10()# 패키지명까지 포함한 형태로 함수 호출

# 이와 같이 하면 함수명만으로 호출이 가능해진다.
from kosmo.mod3 import sum1To10
sum1To10()

