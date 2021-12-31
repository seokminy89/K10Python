'''
sqlite
sqlite3 모듈은 파이썬 표준 라이브러리로 별도의 설치없이 
기본적으로 사용할 수 있다. 
그러므로 import만 하면 데이터베이스를 사용할 수 있다. 
sqlite는 작은 데이터를 저장할때 편리하고, 퍼블릭 라이센스이므로 
어떤 목적으로든 사용할 수 있는 RDB(관계형데이터베이스)이다. 

자료형
 SQLite3 자료형 파이썬 자료형      용도          			설명
 NULL                None          공백						

INTEGER              int          정수형    		별도로 크기를 지정하지 않으며
 REAL                float        실수형    		두가지 자료형을 
 TEXT              str, bytes     문자형    		혼용해서 사용할 수 있다.
 
 BLOB               buffer      바이너리 데이터    이미지와 같은 파일 자체를 저장
'''

###DB연결 및 해제###

# sqlite3 모듈을 불러온다.
import sqlite3

# "my_home.db" 파일을 데이터베이스로 연결하여 사용한다.
con = sqlite3.connect("my_home.db") 

# 커서를 생성한다.
cur = con.cursor() 

# 데이터베이스를 종료한다.
con.close() 


'''Connection 객체는 DB와의 연결을 주로 처리한다.
Cursor 객체는 데이터를 저장 및 조회를 담당한다.'''


###테이블생성###
#아래 2개의 테이블은 동일한 자료형을 가진 테이블이 된다. 

#SQLite3 자료형을 사용
cur.execute("CREATE TABLE my_table1 (name TEXT, age INTEGER, money REAL)")

#파이썬의 자료형을 사용
cur.execute("CREATE TABLE my_table2 (name str, age int, money float)")

#기존에 생성된 테이블이 있는지 확인한 후 생성
cur.execute("CREATE TABLE IF NOT EXISTS my_table3 (name str, age int, money float)")


###레코드 삽입###

#기본형
cur.execute("INSERT INTO my_table1 VALUES ('홍길동', 10, 15000.99)")

#1개의 튜플 입력
cur.execute("INSERT INTO my_table1 VALUES (?,?,?)", ('홍길동', 10, 15000.99))

#2개이상의 튜플 입력
tu_record = (
	('이순신', 10, 15000.99),
	('성삼문', 20, 46000.99),
	('류성용', 30, 99000.99)
)
cur.executemany("INSERT INTO my_table1 (name, age, money) VALUES (?,?,?)", tu_record)

'''insert문 작성시 컬럼은 생략가능함
1개의 레코드 입력시 execute(), 여러개의 레코드 입력시 executemany() 사용'''


###레코드 조회1###

cur.execute("SELECT * FROM my_table1")
print(cur.fetchone())
print(cur.fetchall())

'''레코드를 한개씩 인출할때는 fetchone() 사용
레코드 전체를 한꺼번에 인출할때는 fetchall()을 사용한다. 단, 위와같이 fetchone()을 먼저 실행하였다면 첫번째 레코드는 이미 인출되었으므로 두번째 레코드부터 인출된다. 
'''


###레코드 조회2###

# 방법1
param1 = ('홍길동',)
cur.execute('SELECT * FROM my_table1 WHERE name=?', param1)
print('방법1', cur.fetchall())

# 방법2
param2 = '류성용'
cur.execute("SELECT * FROM my_table1 WHERE name='%s'" % param2) 
print('방법2', cur.fetchall())

# 방법3
cur.execute("SELECT * FROM my_table1 WHERE name=:n1", {"n1": 1})
print('방법3', cur.fetchall())

# 방법4
param4 = ('류성용', '이산')
cur.execute('SELECT * FROM my_table1 WHERE name IN(?,?)', param4)
print('방법4', cur.fetchall())

# 방법5
cur.execute("SELECT * FROM my_table1 WHERE name IN('%d','%d')" % ('류성용', '이산'))
print('방법5', cur.fetchall())

# 방법6
cur.execute("SELECT * FROM my_table1 WHERE name=:n1 OR name=:n2", {"n1":'류성용', "n2":'이산'})
print('방법6', cur.fetchall())


'''서식문자는 Java와 동일하게 정수는 %d, 실수는 %f, 문자는 %s 를 사용한다. 
방법3, 방법6은 딕셔너리를 사용한다. 
대부분은 문자열 포매팅에서 다루었던 내용들이다. '''





###레코드 수정###

# 방법 1
cur.execute("UPDATE my_table1 SET name=? WHERE age=?", ('김연아', 10))
# 방법 2
cur.execute("UPDATE my_table1 SET name=:name WHERE age=:age", {"name": '이상화', 'age': 20})
# 방법 3
cur.execute("UPDATE my_table1 SET name='%s' WHERE age=%d" % ('박찬호', 30))


###레코드 삭제###

# 방법 1
cur.execute("DELETE FROM my_table1 WHERE age=?", (10,))
# 방법 2
cur.execute("DELETE FROM my_table1 WHERE age=:age", {'age': 20})
# 방법 3
cur.execute("DELETE FROM my_table1 WHERE age=%d" % 30)

