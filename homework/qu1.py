'''
문제 1

아래와 같은 패턴의 별(*)을 출력하는 프로그램을 작성해 보세요. 
참고로 print('*', end='')와 같이 print 함수를 사용하면 
줄바꿈 없이 화면에 출력할 수 있습니다.

*****

'''

'''
print("*", end=" ")
print("*", end=" ")
print("*", end=" ")
print("*", end=" ")
print("*", end=" ")
'''


for i in range(5):
    print("*", end=" ")

