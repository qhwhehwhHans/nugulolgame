import pymysql

db=pymysql.connect(host='localhost',user='root',password='Gkstm785gkstm@',db='my_db',charset='utf8',port=3306)

# 커서 가져오기
cursor = db.cursor()

# SQL 문 만들기
sql = '''
            CREATE TABLE hero (
                   name VARCHAR(20) NOT NULL,
                   skill VARCHAR(20) NOT NULL
            );
        '''

# 실행하기
cursor.execute(sql)

# DB에 Complete 하기
db.commit()

# DB 연결 닫기
db.close()
