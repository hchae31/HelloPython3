drop table emp;

create table emp (
                     empid int primary key,
                     fname varchar (30) not null,
                     lname varchar (30) not null,
                     phone varchar (100) not null,
                     hdate date not null,
                     email varchar (50) not null,
                     jobid varchar(20) not null,
                     sal int not null,
                     comm decimal(5,2),
                     mgrid int,
                     deptid int
);

-- 데이터 추가
insert into emp (empid, fname, lname, email, phone, hdate, jobid, sal, comm, mgrid, deptid)

values(100, 'Steven', 'king', 'SKING', '515.123.4567', '2003-06-17','AD_PRES', 24000, null, null, 90);

-- 데이터 조회 1 - 리스트
select empid, fname, email, jobid, deptid from emp;

-- 데이터조 2 - 상세
select * from emp where empid = 100;

