'''
채우기와 정렬
    형식]
        '{인덱스:<길이}
    < : 좌측정렬
    > : 우측정렬
    ^ : 센터정렬
    남은 공백은 공백으로 채운다.
        
'''

# 문자열 앞에 f를 붙이고, 표현할 변수를 중괄호를 이용해서 삽입한다.
str = 'coffee'
num = 1
result = f'{str}는 하루에  {num}잔만 마시는게 좋아요'
print(result)

# 정해진 공간에서의 정렬
s1 = '좌측정렬'
result1 = f'|{s1:<10}|' #|은 서식에 포함되지 않는다. 단순히 공간을 확인하기 위한 용도로 사용되었다.
print(result1)

s1 = '센터정렬'
result2 = f'|{s1:^10}|'
print(result2)

s1 = '우측정렬'
result3 = f'|{s1:>10}|'
print(result3)

# f-String에 딕셔너리를 사용 : key값을 사용해서 변수를 출력
dics = {'name':'성유겸', 'gender':'남자', 'age':10}
result = f'{dics["name"]}은 {dics["gender"]}이고 나이는 {dics["age"]}살이다'
print(result)

# 리스트를 사용 : 배열처럼 index를 사용해서 변수를 출력
lists = [10, 20, 30]
print(f'리스트 : {lists[0]}, {lists[1]}, {lists[2]}')
for v in lists:
    print(f'반복출력 : {v}')



