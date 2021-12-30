'''
문자열 함수

'''


'''
capitalize()
    : 첫 문자가 대문자이고 나머지가 소문자인 문자열의 복사본을 리턴한다.
'''
a = 'PYTHON'
print( a.capitalize() )
# 결과 : Python

'''
count(x, start, end)
    :  인자 x의 갯수를 카운트하여 리턴한다.
    x - 개수를 찾을 문자열 또는 문자입니다.
    str (선택 사항) - 검색이 시작되는 문자열 내에서 시작 색인.
    end (선택 사항) - 검색이 끝나는 문자열 내에서 끝 인덱스.
'''
a = 'pythonpp'
print(a.count('p'))
#결과 : 3 
a = 'pythonpy'
print(a.count('py',0,5))
#결과 : 1

'''
find(sub, start, end)
    : 문자열 내에서 하위 문자열의 인덱스를 반환한다.
    문자나 문자열이 없을시 -1 을 반환한다.
    sub - 검색 할 하위 문자열 입니다.
    start (선택 사항) - 검색이 시작되는 문자열 내에서 시작 색인.
    end(선택 사항) - 검색이 끝나는 문자열 내에서 끝 인덱스.
'''
a = 'pythonpy' 
print(a.find('y'))
#결과 : 1 
print(a.find('py',0,5))
#결과 : 0 
print(a.find('tk')) 
#결과 : -1

'''
index(sub, start, end)
    : 문자열 내에서 하위 문자열의 인덱스를 반환한다. 문자나 문자열이 없을시 오류가 발생한다.
    sub - 검색 할 하위 문자열 입니다.
    start (선택 사항) - 검색이 시작되는 문자열 내에서 시작 색인.
    end(선택 사항) - 검색이 끝나는 문자열 내에서 끝 인덱스.
'''
a = 'pythonpy' 
print(a.index('y')) 
#결과 : 1
 
print(a.index('py',0,5)) 
#결과 : 0
 
#print(a.index('tk')) 
#결과 : 오류 발생

'''
isalnum()
    : 문자열의 모든 문자가 숫자 또는 알파벳 또는 한글 이면 True 를 반환, 
    아니면 False 를 반환
'''

a = 'python'
print( a.isalnum() )
# >>> True
 
a = 'python홍길동'
print( a.isalnum() )
# >>> True
 
a = 'python%%'
print( a.isalnum() )
# >>> False

'''
isalpha()
    : 문자열의 모든 문자가 알파벳이면 True 반환, 아니면 False 반환
        그러나 테스트시 한글이 들어가도 True 반환, 알파벳과 한글이 나뉘어 있을시에는 False 반환
    python ⇒ True
    python홍길동 ⇒ True
    python 홍길동 ⇒ False
    python%% ⇒ False
'''
a = 'python'
print( a.isalpha() )
#결과 : True 
a = 'python홍길동'
print( a.isalpha() )
#결과 : True 
a = 'python 홍길동'
print( a.isalpha() )
#결과 : False 
a = 'python%%'
print( a.isalpha() )
#결과 : False

'''
isdecimal()
    : 문자열의 모든 문자가 10진수이면 True 반환, 아니면 False 반환
'''

a = '123'
print( a.isdecimal() )
# >>> True 
a = '123 ##'
print( a.isdecimal() )
# >>> False 
a = '123 홍길동'
print( a.isdecimal() )
# >>> False

'''
isdigit()
    : 문자열의 모든 문자가 숫자인 경우 True 반환, 아니면 False 반환
'''
a = '123'
print( a.isdigit() )
#결과 : True
a = '123 ##'
print( a.isdigit() )
#결과 : False
a = '123 홍길동'
print( a.isdigit() )
#결과 : False
a = 'python 123'
print( a.isdigit() )
#결과 : False

'''
islower()
    : 문자열의 모든 알파벳이 소문자 이면 True 반환, 
        문자열에 대문자 하나 이상 있으면 False 반환
'''
a = 'python'
print( a.islower() )
#결과 : True 
a = '123 ##'
print( a.islower() )
#결과 : False 

'''
isspace()
    : 문자열에 공백 문자열만 있을경우 True 를 반환, 아니면 False 반환
        간격에 사용되는 문자를 공백 문자라고한다. [예 : 탭, 공백, 줄 바꿈 등]
'''
a = '   \t'
print(a.isspace())
#결과 : True
a = ' a '
print(a.isspace())
#결과 : False

'''isupper()
    : 문자열의 모든 알파벳이 대문자 이면 True 반환, 
        문자열에 소문자 하나 이상 있으면 False 반환
'''
a = 'PYTHON'
print( a.isupper() )
#결과 : True 
a = 'PYTHON홍길동'
print( a.isupper() )
#결과 : True 
a = 'python%%'
print( a.isupper() )
#결과 : False

'''
join(iterable)
    : join 은 반복 가능한 객체에 사이사이에 문자열을 연결하게 해준다.
    iterable : 리스트 ,튜플, 리스트, 문자열 등
'''

# 리스트 join
numList = ['1', '2', '3', '4']
separator = ','
print(separator.join(numList))
#결과 : 1,2,3,4

'''
lower()
문자열의 모든 대문자를 소문자로 변환합니다.
upper()
문자열의 모든 소문자를 대문자로 변환합니다.
lstrip()
문자열 중에 가장 왼쪽에 연속된 공백들을 지운다.
rstrip()
문자열 중에 가장 오른쪽에 연속된 공백들을 지운다.
'''

'''
swapcase()
    : 문자열의 모든 대문자는 소문자로 변환, 
        문자열의 모든 소문자는 대문자로 변환
'''

string = 'THIS IS GOOD'
print( string.swapcase() )
# >>> this is good
 
string = 'this is good'
print( string.swapcase() )
# >>> THIS IS GOOD
 
string = 'tHiS iS GOoD'
print( string.swapcase() )
# >>> ThIs Is goOd

'''
title()
    : 각 단어의 첫 글자를 대문자로 반환한다.
'''

a = 'this is good'
print(a.title())
# >>> This Is Good















