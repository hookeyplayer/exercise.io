-- 1
mysql> select @@autocommit;
-- 执行sql时，效果立刻出现，不能回滚（不能撤销rollback）
-- 每执行一行立刻生效
+--------------+
| @@autocommit |
+--------------+
|            1 |
+--------------+
update user set money = money-100 where name='a';
update user set money = money+100 where name='b';


-- 2
-- 手动开启事务，可以rollback
begin;
-- 或
start transaction;

update user set money = money-100 where name='a';
update user set money = money+100 where name='b';
-- 此时再rollback没有效果


-- 设置mysql自动提交为false，关闭了自动提交
set autocommit=0;
+--------------+
| @@autocommit |
+--------------+
|            0 |
+--------------+

-- 3
commit;
-- 之后也不能rollback


-- 事务的四大特征
ACID(原子性、一致性、隔离性、持久性)

-- 查看隔离级别：可以重复读
select@@global.transaction_isolation;
+--------------------------------+
| @@global.transaction_isolation |
+--------------------------------+
| REPEATABLE-READ                |
+--------------------------------+


-- 修改隔离级别成：读未提交的
set global transaction isolation level read uncommitted;
+--------------------------------+
| @@global.transaction_isolation |
+--------------------------------+
| READ-UNCOMMITTED               |
+--------------------------------+

-- 不可重复读现象会出现在如下的级别设置后
set global transaction isolation level read committed;

-- dirty read: 一个事务读到了另一个没有提交的数据
-- （两个不同的地方都在进行操作，事务a开启后他的数据可以被其他事务读到）






