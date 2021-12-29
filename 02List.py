'''
파일명 : 02List.py

파이썬에는 연속된 Collection 데이터 구조에
list, tuple, dictionary, set이 있다

리스트(list)
    :대괄호[]안에 콤마로 항목을 구분하며, 대입연산자로 항목을 변경할 수 
    있는 시퀀스 자료형이다. 서로 다른 자료형의 항목으로도 구성할 수 있다.
    인덱싱, 슬라이싱, 연결, 반복 등이 가능하다.
    Mutable 데이터 타입이라고 한다.
'''
# 기본적인 선언과 사용법은 배열과 동일하다.
# 선언
list1 = [1,2,3,4,5]
list2 = ['Java','HTML','Python']
# 중첩된 리스트 선언
list3 = [10, 20, ['Java', 'HTML', 'Python']]

#출력
print('list1:', list1) #리스트 전체가 출력됨
print('list2[2]:', list2[2]) #Python
print('list3[2]:', list3[2]) #리스트 내의 리스트 ['Java', 'HTML', 'Python'] 출력됨

# 리스트 슬라이싱
print("===슬라이싱", "="*30)
print('list1[1:4]:', list1[1:4]) #1~3까지 출력
print('list1[:3]:', list1[:3]) #0~2까지 출력
print('list1[1:]:', list1[1:]) #1~마지막까지 출력

print('list2[:3]:', list2[:3]) #0~2까지 슬라이싱(정상출력)
print('list2[:4]:', list2[:4]) #슬라이싱의 경우 인덱스를 벗어나도
print('list2[:5]:', list2[:5]) #정상출력됨.
# 아래처럼 넘어간 인덱스를 슬라이싱이 아니라 직접 지정하면 에러가 발생한다.
# print('list2[5]:', list2[5]) #index out of range 오류

#리스트 연결
print("===리스트 연결", "="*30)
# 리스트 내에 또다른 리스트를 삽입하여 연결하는 형태
all_list = [list1, list2]
print('all_list:', all_list)
print('all_list[1][0]:', all_list[1][0]) #java 출력됨.

print("===list 관련 메소드", "="*30)
list1.append(6) #추가
print('append(6)=>', list1
      )
list1.clear() # 항목 전체 삭제
print('clear()=>', list1)

list1.extend([10, 20, 30, 40, 50]) #리스트 확장
print('extend=>', list1)
list1.insert(1, 99) #지정된 인덱스에 요소 삽입.
print('insert=>', list1)

print(list1.pop())# 마지막 항목 반환 및 삭제
print('pop()=>',list1)

list1.remove(99) #처음 나오는 항목 99 삭제
print('remove=>', list1)

list1.reverse() # 리스트를 뒤집을때 사용
print('reverse()=>', list1)

'''
List Comprehension
    :대괄호 안에 for 루프로 반복적인 표현식을 실행해서
    리스트 요소들을 초기화 하는 방법
    형식[
        [표현식 for 요소 in 컬렉션 [if조건식]]
'''
print("===List Comprehension", "="*30)
'''
    표현식(n의 제곱) 반복문(0~9까지반복) 조건식(3의배수)
    => 0~9까지의 정수 중 3의 배수의 제곱을 리스트에 초기화 한다.
'''
list = [n ** 2 for n in range(10) if n%3==0]
print(list)