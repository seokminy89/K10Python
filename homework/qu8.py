'''
문제 8

아래와 같은 패턴의 별(*)을 출력하는 프로그램을 작성 해보세요.
*********
 *******
  *****
   ***
    *
    
print("*","*","*","*","*")
print("","*","*","*","*")
print("","","*","*","*")
print("","","","*","*")
print("","","","","*")
'''

for i in range(5):
        for j in range(i):
                print(' ', end=' ')
        for j in range(2*(5-i)-1):
                print('*', end=' ')
        print("")