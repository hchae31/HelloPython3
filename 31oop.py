#1. 값만 저장하는 클래스 : V0
# 생성자는 : __init__ (매직함수) 기본값 생성하는
# 클래스 내에 선언된 멤머 변수 - 멤버변수 (주로 private 접근제한자 사용)

class SungJuk:
    # 생성자 : 클래스를 이용해서 객체를 만들떄 초기화 작업을 수행하는 특별한 함수
    # 변수선언: self.변수명
    def __init__(self):
        self.name = '홍길동'
        self.kor = 0
        self.eng = 0
        self.mat = 0
        self.tot = 0
        self.avg = 0.0
        self.grd = '가'


        # 객체의 맴버변수 접근 : 객체명.멤버변수명
print(sj.name)
print(sj.kor, sj.eng, sj.mat)

# 사원 데이터를 클래스(Employee)로 정의
# empid, fname, lname, emial, phone
# hdate, jobid, sal, comm, mgrid, deptid
class Employee():
    def __init__(self):
        self.empid = 100
        self.fname = 'Steven'
        self.lname = 'King'
        self.email = 'SKING'
        self.phone = '515.123.4567'
        self.hdate = '2003-06-17'
        self.jobid = 'AD_PRES'
        self.sal = '24000'
        self.comm = 'None'
        self.mgrid = 'None'
        self.deptid = '90'

emp = Employee()
print(emp.empid, emp.fname, emp.lname)

# 성적 데이터를 클래스로 다루기
sj = SungJuk()
sj.name = input('이름은')
sj.kor = int(input('국어는? '))
sj.eng = int(input('영어는? '))
sj.mat = int(input('수학는? '))

print(sj.name, sj.kor, sj.eng, sj.mat)

# 개선된 성적 클래스 - 생성자를 통해 객체 초기화
class SungJuk2:
    # 생성자 : 클래스를 이용해서 객체를 만들떄 초기화 작업을 수행하는 특별한 함수
    # 변수선언: self.변수명
    def __init__(self, name, kor, eng, mat):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.mat = mat
        self.tot = 0
        self.avg = 0.0
        self.grd = '가'
    # __str__ : 멤버변수들의 값을 문자열화해서
    # 객체정보를 외부에 출력할때 사용하는 특수한 함수
    def __str__(self):
        result = f'{self.name} {self.kor} {self.eng} {self.mat}'
        return result


# 성적 객체 생성 및 초기화
sj = SungJuk2('일지매',99,98,97)

# 성적 객체 출력
print(sj.name, sj.kor, sj.eng, sj.mat)
print(sj)

# 성적 객체 생성 및 초기화2
sj =  SungJuk2(input('이름은?'),int(input('국어는')),
               int(input('영어는?')),int(input('수학은?')))
print(sj)

# 2. 기능만 저장하는 클래스 1 - Service
class SungJukService:
    def read_sungjuk(self):
        name = input('이름은')
        kor = int(input('국어는? '))
        eng = int(input('영어는? '))
        mat = int(input('수학는? '))
        return SungJuk2(name,kor,eng,mat)

    def compute_sungjuk(self, sj):
        sj.tot = sj.kor + sj.eng + sj.mat
        sj.avg = sj.tot / 3
        sj.grd = '가'
        if (sj.avg >= 90): sj.grd = '수'
        elif (sj.avg >= 80): sj.grd = '우'
        elif (sj.avg >= 70): sj.grd = '미'
        elif (sj.avg >= 60): sj.grd = '양'

sjsrv = SungJukService()
sj = sjsrv.read_sungjuk()
sjsrv.compute_sungjuk(sj)

print(sj)
print(sj.tot, sj.avg, sj.grd)

# 4. 기능만 저장하는 클래스 2 - DAO
class SungJukDAO:
    def insertSungJuk(self,sj):
        pass

    def selectSungJuk(self):
        pass

    def updateOneSungJuk(self,sj):
        pass

    def deleteSungJuk(self, sjno):
        pass

sjdao = SungJukDAO()
sjdao.insertSungJuk(sj)
sjdao.selectSungJuk()