import sqlite3


# 성적 데이터 총 갯수 조회
def getTotalSungJuk():
    sql = 'select count(empid) + 1 total from emp'
    conn = sqlite3.connect('db/python.db')
    cursor = conn.cursor()
    cursor.execute(sql)
    cnt = cursor.fetchone()[0]
    cursor.close()
    conn.close()
    return cnt


# 처리된 사원데이터를 테이블에 저장
def newEmp(emp):
    sql = "insert into emp values (?,?,?,?, ?,?,?,?,"\
          "?, nullif(?,'null'), nullif(?,'null'))"
    conn = sqlite3.connect('db/python.db')
    cursor = conn.cursor()
    params = (emp[0],emp[1],emp[2],emp[3],emp[4],emp[5],emp[6],emp[7],emp[8],emp[9],emp[10])
    cursor.execute(sql, params)
    print(cursor.rowcount, '건의 데이터 추가됨!')
    conn.commit()
    cursor.close()
    conn.close()

# 사원 데이터 전체 조회
def readAllEmp():
    sql = 'select empid, fname, emeail, jobid, deptid from emp'
    conn = sqlite3.connect('db/python.db')
    cursor = conn.cursor()
    cursor.execute(sql)
    emps = cursor.fetchall()
    cursor.close()
    conn.close()
    return emps

# 사원 한명 상세 조회
def readOneEmp(empid):
    sql = 'select * from emp where empid = ?'
    conn = sqlite3.connect('db/python.db')
    cursor = conn.cursor()
    params = (empid,)
    cursor.execute(sql)
    emp = cursor.fetchall()
    cursor.close()
    conn.close()
    return emp

# 학생 한명의 성적 상세 조회
def readOneSungJuk(sjno):
    sql = 'select * from sungjuk where sjno = ?'
    conn = sqlite3.connect('db/python.db')
    cursor = conn.cursor()
    params = (sjno,)
    cursor.execute(sql, params)
    sj = cursor.fetchone()
    cursor.close()
    conn.close()
    return sj

#
def deleteEmp(empid):
    sql = 'delete from sungjuk where empid = ?'
    conn = sqlite3.connect('db/python.db')
    cursor = conn.cursor()
    params = (empid,)
    cursor.execute(sql, params)
    cnt = cursor.rowcount
    conn.commit()
    cursor.close()
    conn.close()
    return cnt






