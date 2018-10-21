import pymysql
import re
import json

# MySQL Connection 연결
conn = pymysql.connect(host='yejs.cafe24.com', user='yejs', password='skfnxh99',
                       db='yejs', charset='utf8')
conn.query("set character_set_connection=utf8;")
conn.query("set character_set_server=utf8;")
conn.query("set character_set_client=utf8;")
conn.query("set character_set_results=utf8;")
conn.query("set character_set_database=utf8;")

# Connection 으로부터 Cursor 생성
curs = conn.cursor()

with open('result.json') as f:
    data = json.load(f)

pattern = re.compile('[^\d]')
# SQL문 실행
#sql = "select * from quant"


# 데이타 Fetch
#rows = curs.fetchall()
for n in data:
    print(n)
    sql = "UPDATE quant SET `6` = '" + str(data[n]) + "' WHERE `1` = " + str(n)
    curs.execute(sql)
    conn.commit()
    # if rows[0][7]:
    #     stock_n = rows[0][7]
    #     tot=format(int(pattern.sub('',data[n])) * int(pattern.sub('',stock_n)),',')
    #     sql = "update quant set `6` = " + data[n] + ", `7` = " + tot + " where `1` = " + n
    #     print(n)
    #     print(data[n])
    #     print(tot)
# print(rows[7])  # 전체 rows
# print(rows[7][5])  # 주가
# print(rows[7][6])  # 시총
# print(rows[7][7])  # 주식수
# print(rows[0])  # 첫번째 row: (1, '김정수', 1, '서울')
# print(rows[1])  # 두번째 row: (2, '강수정', 2, '서울')

# Connection 닫기
conn.close()