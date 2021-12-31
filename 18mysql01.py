'''
파이썬에서 MySQL(or MariaDB)를 사용하기 위해서 PyMySQL 모듈을 
설치해야 한다.
'''
# 모듈 임포트
import pymysql

#DB연결
conn = pymysql.connect(host='localhost', user='kosmo_user',
                        password='1234', db='kosmo_db', charset='utf8')

'''
    , cursorclass=pymysql.cursors.DictCursor
    => 위 설정이 없는 경우에는 레코드를 튜플로 가져오고,
    설정이 추가되면 딕셔너리로 출력된다.
'''
# 커서 생성
curs = conn.cursor()

try:
    sql ="SELECT * FROM board"
    curs.execute(sql)
    
    # select한 모든 레코드 인출
    rows = curs.fetchall()
    print(rows)
    
    print('출력1', '-'*40)
    # 행 단위로 출력
    for row in rows:
        print(row)
    
    
    print('출력2', '-'*40)
    for row in rows:
        # 행단위로 출력하되 각 컬럼의 인덱스를 지정하여 출력한다.
        print(row[0], row[1], row[2], end=" ")
        pdate = row[3]
        id = row[4]
        vcnt = row[5]
        print("%s, %s, %s" % (pdate, id, vcnt))
    
    
    print('출력3', '-'*40)
    # format() 함수를 통해 쿼리문에 입력한 검색어를 추가한다.
    sql = sql + " WHERE title like '%{0}%' ".format(input('검색어입력:'))
    curs.execute(sql)
    rows = curs.fetchall()
    print(rows)

except Exception as e:
    print("쿼리 실행시 오류발생", e)
    
print('-'*40)
conn.close()
print('자원반납')
    