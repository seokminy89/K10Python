'''
예외처리
    : 에러를 핸들링 하기 위해 사용된다.
    파이썬에서는 try ~ except를 사용한다.
    그리고 else를 사용할 수 있다.
'''

def calc(val):
    sum = None
    try: # 예외 발생이 예상되는 지점을 try로 묶는다.
        sum = val[0] + val[1] + val[2]
        if val[0]==100:
            print(no_var) # 선언되지 않은 변수를 출력하므로 예외 발생.
        elif val[0]==55:
            result = val[0] / 0 # 숫자를 0으로 나누므로 예외발생
            print("결과", result)
    # 예외명을 명시하여 특정 예외만 처리한다.
    except IndexError:
        print('리스트의 인덱스에 에러가 있습니다.')
    # 예외발생시의 에러메세지를 변수로 받아서 출력한다.
    except NameError as err:
        print('선언되지 않은 변수를 사용하였습니다.', str(err))
    # 예외명을 명시하지 않으면 모든 예외를 처리할 수 있는 블럭이 된다.
    except:
        print("예외가 발생하였습니다.")
    # 예외가 발생되지 않았을 때 실행되는 블럭
    else:
        print("에러없음.")
    # try로 진입했을때 예외발생과 상관없이 무조건 실행되는 블럭
    finally:
        print("sum", sum)
        
print('실행1')
calc([1, 2, 3]) # 정상실행
print('실행2')
calc([10, 20]) # 인덱스 에러
print('실행3')
calc([100, 101, 102, 103]) # NameError 예외발생
print('실행4')
calc([55, 56, 57]) # 0으로는 나눌 수 없기 때문에 예외발생.

# 중첩된 예외처리 구문
print('실행5')
try:
    # 파일을 읽기 전용으로 오픈
    fp = open("test.txt", "r")
    try:
        lines = fp.readlines()
        print(lines)
    finally:
        print("파일 객체를 닫습니다.")
        fp.close()
except IOError: # 현재 경로에 test.txt 파일이 업으므로 예외발생
    print('파일에러발생')
    
# 개발자가 직접 예외 발생시키기.
print('실행6')
try:
    x = int(input('3의 배수를 입력하세요: '))
    # 입력한 수가 3의 배수가 아닐때 예외를 발생시킨다.
    if x % 3 != 0:
        # 예외발생시 throw 대신 raise를 사용한다.
        raise Exception('[예외메세지] 3의 배수가 아님')
    print(x)
except Exception as e:
    print('예외가 발생하였습니다.', e)
'''
개발자 정의 예외클래스 생성
    : 예외 클래스 생성 시 Exception 객체를 상속하고
    생성자에서 예외발생시 출력할 메세지를 정의한다.
'''
print('실행7')
class GugudanRangeExcept(Exception):
    def __init__(self):
        super().__init__('구구단의 범위를 벗어났습니다.')

def print_gugudan(end_num):
    try:
        # 예외를 발생시킬 조건에서 해당 클래스를 raise한다.
        if end_num > 9:
            raise GugudanRangeExcept
        end_su = end_num + 1
        for su in range(2, end_su):
            for dan in range(1,10):
                print("%2d * %2d = %2d" % (su, dan, su*dan), end=' ')
            print()
        print()
    except Exception as e:
        print('예외발생', e)
print_gugudan(int(input("출력할 단 수를 입력하세요:")))
