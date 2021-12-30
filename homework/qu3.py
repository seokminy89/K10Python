'''
문제 3

아래와 같은 패턴의 별(*)을 출력하는 프로그램을 작성해보세요.
*
**
***
****
*****
'''

'''
print("*")
print("**")
print("***")
print("****")
print("*****")'''

for i in range(5):
        for j in range(i+1):
                print('*', end=' ')
        print()



