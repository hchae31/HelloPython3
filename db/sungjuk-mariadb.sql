drop table emp;


create table emp (
                     empid integer primary key,
                     fname varchar (30) not null,
                     lname varchar (30) not null,
                     phone varchar (100) not null,
                     email varchar (500) not null,
                     hdate date not null,
                     jobid varchar (20) not null,
                     sal integer not null,
                     comm decimal(5,2),
                     mgrid integer,
                     deptid integer
);

-- 데이터 추가
insert into emp (empid, fname, lname, email, phone, hdate, jobid, sal, comm, mgrid, deptid)

values(100, 'Steven', 'king', 'SKING', '515.123.4567', '2003-06-17','AD_PRES', 24000, null, null, 90);

-- 데이터 조회 1 - 리스트
select empid, fname, email, jobid, deptid from emp;

-- 데이터조 2 - 상세
select * from emp where empid = 100;








-- import sqlite3
--
-- # 회원정보를 입력받아 member 테이블에 저장
-- # 저장대상 : 아이디, 비밀번호, 이름, 이메일
--
-- # 파이썬으로 데이터베이스 다루기 1 - 테이블 생성
-- # 1. 데이터베이스 연결
-- conn = sqlite3.connect('db/python.db')
--
-- # 2. 데이터베이스 커서 생성
-- cursor = conn.cursor()