-- wildcard % 或_ 效率慢

where Soundex(cust_contact) = Soundex('Y Lie')

-- 1000/2000都出现
select prod_name
from table
where prod_name regexp '.000'
order by prod_name;

-- or
where prod_name regexp '1000|2000|3000'

-- []里定义一组字符
where prod_name regexp '[123] ton'

-- ^ 除这些字符串以外的任何
where prod_name regexp '[^123] ton'

-- 区分大小写
where prod_name regexp binary 'JeckPack .000'

-- 匹配特殊字符需要加前导 \\，转义escaping
where prod_name regexp '\\.'

[:alnum:]
[a-zA-Z0-9]

[:alpha:]
[a-zA-Z]

[:digit:]

-- 16进制
[:xdigit:]
[a-fA-F0-9]

[:upper:]
[A-Z]
[:lower:]
[a-z]

-- ? 它前面的0个或1个匹配
-- * 0个或多个匹配={0,}
-- + 1个或多个匹配={1,}
-- {n}{n,}{n,m}
where prod_name regexp '\\([0-9] sticks?\\)'

-- 匹配连在一起的四位数字
where prod_name regexp '[[:digit:]{4}'
where prod_name regexp '[0-9][0-9][0-9][0-9]'

-- 只在第一个字符时定位匹配
where prod_name regexp '^[0-9\\.]'

--拼接
select Concat(RTrim(vendor_name), '(', vendor_country, ')')

--返回串左边的字符
left()

--找出串的子串
Locate()
