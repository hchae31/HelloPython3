class SungJuk:
    # 생성자 : 클래스를 이용해서 객체를 만들떄 초기화 작업을 수행하는 특별한 함수
    # 변수선언: self.변수명
    def __init__(self, name, kor, eng, mat):
        self.sjno = 0
        self.name = '홍길동'
        self.kor = 0
        self.eng = 0
        self.mat = 0
        self.tot = 0
        self.avg = 0.0
        self.grd = '가'
        self.regdate = '2024-07-23 17:00:00'

# 사원 클래스
class Employee:
    def __init__(self, empid, fname, lname, email, phone, hdate, jobid,
                 sal,comm,mgrid,deptid):
        self.empid = empid
        self.fname = fname
        self.lname = lname
        self.email = email
        self.phone = phone
        self.hdate = hdate
        self.jobid = jobid
        self.sal = sal
        self.comm = comm
        self.mgrid = mgrid
        self.deptid = deptid