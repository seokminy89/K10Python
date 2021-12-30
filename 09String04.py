'''
replace('바꿀문자열', '새문자열')
    : 특정 문자열을 찾아 변경한다.
'''

print("="*5, "replace()", "="*20)
print('Hello, world!'.replace('world', 'Python'))

s = 'Hello, world!'
s = s.replace('world!', 'Python')
print(s)

'''
문자바꾸기
    transelate()는 문자열 안의 문자를 다른 문자로 변경한다.
    maketrans('바꿀문자','새문자')로 변환 테이블을 만든 후 적용한다.
    아래는 a는1로, e는 2로 변경된다.
'''
print("="*5, "maketrans()/transelate()", "="*20)
str1 = "apple"
table = str1.maketrans('aeiou', '12345')
print(str1.translate(table))

# '한'은 X, '아'는 Y로 변경된다.
str2 = "한글은 아름다운 언어"
table = str2.maketrans('한아언', 'XYZ')
print(str2.translate(table))

'''
'구분자'.join(합칠문자열)
    : 합칠 문자열을 구분자를 통해 합쳐서 반환한다.
'''
print("="*5, "join()", "="*20)
print('-'.join(['010','1111','2222']))

'''
공백삭제 혹은 특정문자 삭제
    lstrip(왼쪽), rstrip(오른쪽), strip(양쪽)
    별도의 인자가 없으면 공백이 삭제된다.
'''
print("="*5, "strip()", "="*20)
str = "#^%오늘은 @@ 파이ㅣ썬 @@ 공부하는날#^%"
print(str.lstrip('#'))
print(str.rstrip('%'))
print(str.rstrip('%').lstrip('#').replace('@', ''))

'''
열 위치 찾기
    find(왼쪽에서 부터), rfind(오른쪽에서 부터 찾기)
'''
print("="*5, "find()", "="*20)
print('apple pineapple'.find('pl'))
print('apple pineapple'.rfind('pl'))



