-- 多条查询语句的结果合成一个结果
-- 联合查询



-- time
select now()
select curdate()
select curtime()

select year(hiredate)
select month(now())
select monthname(now())
-- 大写4位的年份；小写2位的年份；c不补零的月份；m补零的月份
select str_to_date('9-13-1999', '%m-%d-%Y') as out_put;
select * from employee where hiredate = str_to_date('%c-%d %Y');
-- 日期转换成字符
select date_format('2018/6/6','%Y年%m月%d日');

-- 生日在1988年之后
datediff(borndate, '1988-1-1')>0

-- 拼接
select concat(last_name, '_', 'first_name') from employees;

select upper('john')
select lower('joRn')
select concate(upper(last_name), lower(first_name))
select concate(upper(substr(last_name, 1, 1), '_', lower(substr(last_name, 2)))

-- 截取字符串
select substr('李莫愁爱上了陆展元',7) # 陆展元
select substr('李莫愁爱上了陆展元',1, 5) # 李莫愁爱上

-- 返回子串在大字符串里的起始索引，若找不到返回0
select inster('杨不悔爱上了殷六侠', '殷六侠') #7

-- 邮箱用户名
select substr(email, 1, instr(email, '@')-1)

-- 去前后空格
select trim('     hello    ');
select trim('a' from 'aaaahelloaaaa');

select replace('张无忌爱上了周芷若', '周芷若', '赵敏')

-- 四舍五入
round()

-- 向上/下取整
ceil()/floor()

-- 截断
truncate(1,655555, 1) # 1.6

-- 取余
mod(-10, -3) # a-a/b*b
select 10%3

-- case流程控制（1）等值判断
select salary 原始工资, department_id
case department_id
when 30 then salary*1.1
when 40 then select*1.2
else salary
end as 新工资

-- case流程控制（2）多重if，区间判断
select salary
case
when salary > 20000 then 'A'
else'B'
end


-- 用指定字符左填充
select lpad('殷素素', 10, '*') # *******殷素素
-- 若超过长度，从右边截断
select lpad('殷素素', 2, '*') # 殷素

-- 含a
where last_name like '%a%'
-- 第3位、第5位指定
where last_name like '__n_l%'
-- 第2个为下划线需要转译
where last_name like'_\_%'
-- 或者ESCAPE关键字任意指定转译字符
where last_name like '_$_%' ESCAPE '$'

select now()

-- 窗口函数
select *,
   rank() over (partition by 班级
                 order by 成绩 desc) as ranking
from 班级表

select *,
   rank() over (order by 成绩 desc) as ranking,
   dense_rank() over (order by 成绩 desc) as dese_rank,
   row_number() over (order by 成绩 desc) as row_num
from 班级表


-- 考虑奖金为0
select salary*12*(1+ifnull(commission_pct, 0)) as annual_salary

-- 有员工的部门名
-- 法一
-- exists()
select department_name
from department d
where exists(
	select * 
	from employee e
	where e.'department_id' = d.'department_id'
);


-- 法二
select department_name
from department d
where d.'department_id' in (select department_id from employee);