import pymysql

conn = pymysql.connect(host='localhost', user='kosmo_user',
    password='1234', db='kosmo_db', charset='utf8')

curs = conn.cursor()

sql = f"""delete from board where num='{input('삭제할일련번호:')}'"""
        
try:
    curs.execute(sql)
    # DB에 변경사항을 적용한다.
    conn.commit()
    print("1개의 레코드가 삭제됨")
except Exception as e:
    #오류가 발생하면 롤백한다.
    conn.rollback()
    print("쿼리 실행시 오류 발생", e)

conn.close()
    