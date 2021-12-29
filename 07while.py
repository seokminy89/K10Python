'''
반복문
    :파이썬에서의 반복문은 while문과 for문만 있다.
    do~while문은 없다.
'''
str = 'python'
# str이 공백이 될때까지 반복한다. 공백이 아니면 true를 반환한다.
while str:
    # 출력문 끝에 공백을 추가하여 줄바꿈 없이 출력한다.
    print(str, end=' ')
    # 슬라이싱을 통해 제일 앞에 문자 하나를 제거한 후 str에 대입.
    str = str[1:]
print()
print("=================="*3)

# 시나리오 ] 1~10까지의 합을 구하시오.
'''
    파이썬에서는 while문에 else를 추가할 수 있다.
    while문의 조건이 false일때 탈출하여 else 구문이 실행된다.
'''
sum = 0
i = 1
while i<=10:
    sum += i # 누적해서 더하는 부분
    if i<10:
        print(i, end=" + ")
    else:
        print(i, end=" = ")
    i += 1 # i값 증가.
else:
    # while문을 벗어나면 실행된다.
    print(sum)

print("==================="*3)
# 시나리오] 구구단을 출력하되 짝수단만 출력하시오
dan = 2
while dan<=9 :
    if dan%2==1: #만약 단이 홀수라면...
        dan += 1
        continue #반복문 내에서 continue를 만나면 반복문의 처음으로 돌아간다.
    else: #단이 짝수일때 아래 문장을 출력한다.
        su = 1
        while su<=9:
            #printf()같이 서식문자를 사용할 때는 %로 문자열과 변수를 구분한다.
            print("%2d * %2d = %2d" % (dan, su, su*dan), end=' ')
            su += 1
    dan += 1
    print()
print()
    
    






