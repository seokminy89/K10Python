'''
인스턴스 변수
    : 메서드 안에 정의되는 변수
    -클래스 내부에서는 self.변수명 형태로 접근한다.
    -클래스 외부에서는 객체변수.인스턴스변수 형태로 접근한다.
인스턴스 메서드
    : 인스턴스 변수에 항상 접근할 수 있도록 메서드의 첫번재
    파라미터에 항상 객체 자신을 의미하는 self를 선언해야 한다.
'''
#클래스 선언
class FourCalculator:
    # setter()메서드로 초기화를 담당한다.
    def setdata(self, first, second):
        # self.매개변수 = 매개변수 형태로 기술됨. java의  this 와 비슷한 역할.
        self.first = first
        self.second = second
    # 사칙연산을 수행하는 인스턴스 메서드 정의. 멤버변수에 접근하기 위해
    # 첫번째 파라미터는 self를 반드시 사용해야 한다.
    def addition(self):
        result = self.first + self.second
        return result
    def substraction(self):
        result = self.first - self.second
        return result
    def multiplication(self):
        result = self.first * self.second
        return result
    def division(self):
        result = self.first / self.second
        return result

# 객체 생성. java와 달리 파이썬에서는 new를 사용하지 않는다.
a = FourCalculator()
b = FourCalculator()

# 각 객체의 setter() 메서드를 통해 인스턴스 변수를 초기화 한다.
a.setdata(4, 2)
b.setdata(3, 8)

# 각 객체의 인스턴스 메서드를 호출한다.
print("객체a 덧셈", a.addition())
print("객체a 곱셈", a.multiplication())
print("객체b 뺄셈", b.substraction())
print("객체b 나눗셈", b.division())

'''
생성자(initializer)
    : 클래스로부터 객체를 만들 때 인스턴스 변수를 초기화 한다.
    init 양쪽에 언더바 2개를 붙여 정의한다.
정적메소드(staticmethod) 
    : 클래스명으로 바로 접근할 수 있는 메소드를 말한다.
    @staticmethod라는 데코레이터를 사용한다.
클래스메소드(classmethod) 
    : 정적메소드와 비슷한데, 객체 인스턴스를 의미하는
    self대신 cls라는 클래스를 의미하는 파라미터를 전달받는다.
    cls를 통해 클래스 변수에 엑세스 할 수 있다.
    @classmethod 라는 데코레이터를 사용한다.
'''
class CalculatorInit:
    
    #클래스 변수(클래스 전체에서 접근가능한 전역변수)
    count = 0
    
    '''
    파이썬에서는 Java처럼 생성자 오버로딩을 지원하지 않는다.
        def __init__(self):
        self.first = 1
        self.second = 2
    '''
    # 생성자 메서드 정의. 멤버변수 초기화를 위해 첫번째 파라미터에 self를 기술해야 한다.
    def __init__(self, first, second):
        self.first = first
        self.second = second
        # 생성자에서 클래스 변수 접근 가능
        CalculatorInit.count += 1
    
    # 일반적인 인스턴스 메서드 정의
    def addition(self):
        result = self.first + self.second
        return result
    
    # 정적메서드 정의. 클래스명으로 즉시 호출 가능함.
    @staticmethod
    def staticArea(pFirst, pSecond):
        result = pFirst * pSecond
        print("static메소드", result)
        
    # 클래스 메서드 정의. cls를 통해 클래스 변수에 접근할 수 있다.
    @classmethod
    def showInfo(cls):
        print('class메소드', cls.count)

#fCal = CalculatorInit() -> 인자가 없는 기본생성자는 정의되지 않았기 때문에 에러발생
# 2개의 인자를 전달해서 객체 생성
fCal = CalculatorInit(2010, 43)
# 일반적인 인스턴스 메서드 호출      
print(fCal.addition())
# 클래스 메서드 호출1 : 인스턴스 변수를 통한 호출
fCal.showInfo()
# 클래스 메서드 호출2 : 클래스명을 통한 호출.
CalculatorInit.showInfo()
#정적메소드 호출
CalculatorInit.staticArea(5, 8)

# 상속 : 파이썬에서는 별도의 키워드 없이 클래스 정의시 매개변수 형태로 상속한다.
class MoreCalculator(CalculatorInit):
    # 자식쪽에서 확장한 인스턴스 메서드
    def pow(self):
        # first를 second만큼 거듭제곱 한다.
        result = self.first ** self.second
        return result
    # 오버라이딩 : 부모의 기능을 자식쪽에서 재 정의함.
    def addition(self):
        return (self.first + self.second) * 2
# 자식 객체 생성 및 호출
moreCal = MoreCalculator(4, 3)    
print("상속후", moreCal.pow()) # 4의 3승의 결과 출력

# 부모 객체 및 자식 객체 생성
p1 = CalculatorInit(100, 200) # 결과 : 300
p2 = MoreCalculator(100, 200) # 결과 : 600
# 오버라이딩 결과 확인하기.
print("부모객체로호출", p1.addition())
print("자식객체로호출", p2.addition())

# 정보은닉 : 인스턴스 변수를 비공개속성(private)으로 설정한다.
class Person:
    # 생성자 메서드 정의
    def __init__(self, n, a, pw):
        self.name = n
        self.age = a
        # 인스턴스 변수앞에 언더바를 2개 붙이면 private이 된다.
        self.__passwd = pw # 생성자에서 초기화 함
    # 아래의 메서드가 getter의 역할을 한다. 외부로 보내주는 역할.
    def secret_info(self):
        return self.__passwd
    
p1 = Person('my', 22, 'qwer1234')
print("이름", p1.name)
print("나이", p1.age)
# private 변수이므로 클래스 외부에서는 접근할 수 없어 에러발생
#print("비밀번호1", p1.__passwd)
# 언더바가 없는 형태의 passwd라는 변수가 없으므로 에러발생
#print("비밀번호2", p1.passwd)
# getter 역할을 하는 아래의 secret_info()메서드를 통해 간접적으로 접근가능.
print("비밀번호", p1.secret_info)


    