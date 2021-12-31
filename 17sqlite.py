# sqlite를 사용하기 위해 임포트
import sqlite3
# 파일 형태로 존재하는 dbase1에 연결한다.
conn = sqlite3.connect('dbase1')
# DB작업을 위한 커서 생성
curs = conn.cursor()

# 테이블 생성.
'''
    첫 실행시에는 문제가 없으나 두번째 실행에서는 이미 테이블이
    존재하므로 예외처리를 해야 아래 문장이 실행된다.
'''
try:
    tblcmd = 'create table people (name char, job char, pay int)'
    curs.execute(tblcmd) # 쿼리 실행
except Exception as e:
    print("[예외발생]테이블은 이미 생성되었습니다.", e)

# 레코드 1개 삽입. 튜플을 사용하여 인파라미터를 설정한다.
curs.execute('insert into people values (?,?,?)',('이순신','장군',500))

# 레코드 2개 이상을 삽입할 경우 list를 활용한다.
curs.executemany('insert into people values (?,?,?)',
        [('강감찬','장군',700), ('홍길동','의적',800)])

# for문을 이용한 삽입
rows = [['곽재우', '의병', 1100],['유성룡', '재상', 1200],['임꺽정', '의적', 1500]]

for row in rows :
    curs.execute('insert into people values (?,?,?)', row)
# 커밋    
conn.commit()

# 조회1 : 조회된 레코드를 한꺼번에 출력한다.
curs.execute('select * from people')
print(curs.fetchall())
print('---------------------------------')

# 조회2 : 조회된 결과를 한 행(row)씩 출력한다.
curs.execute('select * from people')
for row in curs.fetchall():
    print(row)
print('---------------------------------')

# 조회3 : 각 컬럼별로 출력한다.
curs.execute('select * from people')
for(name, job, pay) in curs.fetchall():
    print(name, ':', job, ':', pay)
print('---------------------------------')


