-- 建表
create table student(
sno varchar(20) primary key,
sname varchar(20) not null,
ssex varchar(10) not null,
sbirthday datetime,
class varchar(20)
);

create table teacher(
tno varchar(20) primary key,
tname varchar(20) not null,
tsex varchar(10) not null,
tbirthday datetime,
prof varchar(20) not null,
depart varchar(20) not null
);

create table course(
	cno varchar(20) primary key,
	cname varchar(20) not null,
	tno varchar(20) not null,
	foreign key(tno) references teacher(tno)
);

create table score(
	sno varchar(20) primary key,
	cno varchar(20) not null,
	degree decimal,
	foreign key(sno) references student(sno),
	foreign key(cno) references course(cno)
);


-- 添加数据
insert into student values('108', 'Anber', 'G', '1997-09-01', '95033');
insert into student values('107', 'Bank', 'B', '1998-09-21', '95031');
insert into student values('106', 'Cash', 'B', '1999-08-01', '95033');
insert into student values('105', 'Cherry', 'G', '1992-09-01', '95031');
insert into student values('104', 'Jerry', 'B', '1997-09-21', '95033');
insert into student values('103', 'Sandy', 'B', '1998-09-21', '95031');
insert into student values('102', 'Lily', 'G', '1999-07-01', '95033');
insert into student values('101', 'Sophie', 'G', '1993-09-01', '95031');
insert into student values('100', 'Rachel', 'F', '1994-11-01', '95031');
update student set sbirthday='1993-03-01' where sno='102';

insert into teacher values('804', 'Toogood', 'B', '1970-03-01', 'Professor', 'Engineering');
insert into teacher values('803', 'Tooold', 'G', '1969-08-01', 'Professor', 'Maths');
insert into teacher values('802', 'Toogood', 'B', '1980-06-01', 'Assistant', 'Physics');
insert into teacher values('801', 'Tooold', 'G', '1959-04-01', 'Director', 'Arts');

insert into course values('3-105', 'Intro to Python', '804');
insert into course values('6-247', 'Intro to SDE', '803');
insert into course values('2-105', 'Intro to Painting', '801');
insert into course values('4-185', 'Intro to Solar', '802');

insert into score values('108', '3-105', '88');
insert into score values('107', '6-247', '88');
insert into score values('106', '2-105', '98');
insert into score values('105', '6-247', '86');
insert into score values('104', '3-105', '68');
insert into score values('103', '4-185', '89');
insert into score values('102', '2-105', '90');
insert into score values('101', '3-105', '100');
insert into score values('100', '4-185', '100');
-- 修改
update score set degree='101' where sno='100';

-- 排序

select * from score order by cno asc, degree desc;
+-----+-------+--------+
| sno | cno   | degree |
+-----+-------+--------+
| 106 | 2-105 |     98 |
| 102 | 2-105 |     90 |
| 101 | 3-105 |     88 |
| 108 | 3-105 |     88 |
| 104 | 3-105 |     68 |
| 100 | 4-185 |    100 |
| 103 | 4-185 |     89 |
| 107 | 6-247 |     88 |
| 105 | 6-247 |     86 |
+-----+-------+--------+
-- 计数
select count(*) from student where class='95031';
+----------+
| count(*) |
+----------+
|        5 |
+----------+

-- 找到score表中最高分学生的学号与课程号
-- 法一
select sno, cno, degree from score where degree=(select max(degree) from score);
+-----+-------+--------+
| sno | cno   | degree |
+-----+-------+--------+
| 100 | 4-185 |    100 |
| 101 | 3-105 |    100 |
+-----+-------+--------+
-- 法二
-- 排序并取出最高分，存在缺陷，万一有两个最高分
-- limit 第一个参数表示位置，第二个参数表示查询多少条
select sno, cno from score order by degree desc limit 0, 1;
+-----+-------+
| sno | cno   |
+-----+-------+
| 100 | 4-185 |
+-----+-------+

select sno, cno from score order by degree desc limit 0, 2;

+-----+-------+
| sno | cno   |
+-----+-------+
| 100 | 4-185 |
| 101 | 3-105 |
+-----+-------+

select * from course;
+-------+---------------------+-----+
| cno   | cname               | tno |
+-------+---------------------+-----+
| 2-105 | Intro to Painting   | 801 |
| 3-105 | Intro to Python     | 804 |
| 4-185 | Intro to Solar      | 802 |
| 6-247 | Introduction to SDE | 803 |
+-------+---------------------+-----+

-- 每门课的平均成绩
select cno, avg(degree) from score
group by cno;
+-------+-------------+
| cno   | avg(degree) |
+-------+-------------+
| 2-105 |     94.0000 |
| 3-105 |     85.3333 |
| 4-185 |     94.5000 |
| 6-247 |     87.0000 |
+-------+-------------+
-- 至少2名学生选修并且以3开头的课程的平均分数
select cno, avg(degree),count(*) from score 
group by cno
having count(cno)>=2 and cno like '3%';
+-------+-------------+----------+
| cno   | avg(degree) | count(*) |
+-------+-------------+----------+
| 3-105 |     85.3333 |        3 |
+-------+-------------+----------+
-- 查询分数大于70、小于90的sno列
select sno, degree from score
-- where degree > 70 and degree < 90;
where degree between 70 and 90;
+-------+-------------+----------+
| cno   | avg(degree) | count(*) |
+-------+-------------+----------+
| 3-105 |     85.3333 |        3 |
+-------+-------------+----------+


-- 跨表查询，多表联合
select sname, cno, degree from student, score
where student.sno=score.sno;

+--------+-------+--------+
| sname  | cno   | degree |
+--------+-------+--------+
| Rachel | 4-185 |    100 |
| Sophie | 3-105 |    100 |
| Lily   | 2-105 |     90 |
| Sandy  | 4-185 |     89 |
| Jerry  | 3-105 |     68 |
| Cherry | 6-247 |     86 |
| Cash   | 2-105 |     98 |
| Bank   | 6-247 |     88 |
| Anber  | 3-105 |     88 |
+--------+-------+--------+

select sname, cname, degree, student.sno, course.cno from student, course, score
where student.sno=score.sno and course.cno=score.cno;
+--------+---------------------+--------+-----+-------+
| sname  | cname               | degree | sno | cno   |
+--------+---------------------+--------+-----+-------+
| Lily   | Intro to Painting   |     90 | 102 | 2-105 |
| Cash   | Intro to Painting   |     98 | 106 | 2-105 |
| Sophie | Intro to Python     |    100 | 101 | 3-105 |
| Jerry  | Intro to Python     |     68 | 104 | 3-105 |
| Anber  | Intro to Python     |     88 | 108 | 3-105 |
| Rachel | Intro to Solar      |    100 | 100 | 4-185 |
| Sandy  | Intro to Solar      |     89 | 103 | 4-185 |
| Cherry | Introduction to SDE |     86 | 105 | 6-247 |
| Bank   | Introduction to SDE |     88 | 107 | 6-247 |
+--------+---------------------+--------+-----+-------+

-- 95031班学生每门课的平均分
select avg(degree) from score where sno in (select sno from student where class='95031');
+-----+-------+--------+
| sno | cno   | degree |
+-----+-------+--------+
| 100 | 4-185 |    100 |
| 101 | 3-105 |    100 |
| 103 | 4-185 |     89 |
| 105 | 6-247 |     86 |
| 107 | 6-247 |     88 |
+-----+-------+--------+

-- 某个班所有人的课程平均成绩
select cno, avg(degree)
from score 
where sno in (select sno from student where class='95031')
group by cno;
+-------+-------------+
| cno   | avg(degree) |
+-------+-------------+
| 4-185 |     94.5000 |
| 3-105 |    100.0000 |
| 6-247 |     87.0000 |
+-------+-------------+

-- 某门课大于特定成绩的同学和成绩
select * from score where cno='3-105' and degree>(select degree from score where sno='104' and cno='3-105');
+-----+-------+--------+
| sno | cno   | degree |
+-----+-------+--------+
| 101 | 3-105 |    100 |
| 108 | 3-105 |     88 |
+-----+-------+--------+


-- 查特定出生年份的所有学生的信息
select year(sbirthday) from student
where sno in (108, 101);
+-----------------+
| year(sbirthday) |
+-----------------+
|            1993 |
|            1997 |
+-----------------+
select * from student 
where year(sbirthday) in (select year(sbirthday) from student where sno in (108, 101));
+-----+--------+------+---------------------+-------+
| sno | sname  | ssex | sbirthday           | class |
+-----+--------+------+---------------------+-------+
| 101 | Sophie | G    | 1993-09-01 00:00:00 | 95031 |
| 102 | Lily   | G    | 1993-03-01 00:00:00 | 95033 |
| 104 | Jerry  | B    | 1997-09-21 00:00:00 | 95033 |
| 108 | Anber  | G    | 1997-09-01 00:00:00 | 95033 |
+-----+--------+------+---------------------+-------+

-- 某个老师任课的学生成绩
-- select tno from teacher where tname='Toogood';
select cno from course where tno in (select tno from teacher where tname='Toogood');
+-------+-----------------+-----+
| cno   | cname           | tno |
+-------+-----------------+-----+
| 4-185 | Intro to Solar  | 802 |
| 3-105 | Intro to Python | 804 |
+-------+-----------------+-----+
select * from score where cno in (select cno from course where tno in (select tno from teacher where tname='Toogood'));
+-----+-------+--------+
| sno | cno   | degree |
+-----+-------+--------+
| 100 | 4-185 |    100 |
| 103 | 4-185 |     89 |
| 101 | 3-105 |    100 |
| 104 | 3-105 |     68 |
| 108 | 3-105 |     88 |
+-----+-------+--------+

-- 某课程同学人数大于3人的教师姓名
select * from score;
+-----+-------+--------+
| sno | cno   | degree |
+-----+-------+--------+
| 100 | 4-185 |    100 |
| 101 | 3-105 |    100 |
| 102 | 2-105 |     90 |
| 103 | 4-185 |     89 |
| 104 | 3-105 |     68 |
| 105 | 6-247 |     86 |
| 106 | 2-105 |     98 |
| 107 | 6-247 |     88 |
| 108 | 3-105 |     88 |
+-----+-------+--------+
select cno from score group by cno;
+-------+
| cno   |
+-------+
| 2-105 |
| 3-105 |
| 4-185 |
| 6-247 |
+-------+
select cno from score group by cno having count(*)>2;
+-------+
| cno   |
+-------+
| 3-105 |
+-------+
select tname from teacher where tno=(select tno from course where cno=(select cno from score group by cno having count(*)>2));


