## 查询

### 查询指定表的指定列

> select 列 from 表

- select ：指定的列
- from：指定的表

```mysql
-- 查询学生表中的成绩
select achievement from student
```

### 查询多列

> select 列1, 列2,... from 表

- 查询全部可以使用*****，但不建议

```mysql
-- 查询学生表中的学生姓名和成绩
select name, achievement from student
```

### 查询到的数据去重

> select distinct 列 from 表名

### 查询到的数据使用别名

> select 列 as '别名' from 表

```mysql
select achievement as '成绩' from student
```

### 查询到的数据进行运算：**+ - * /**

```mysql
-- 查询到的数据乘以12
select 列*12 from 表
```

### 查询数据排序

> select 列1, 列2...  from 表 order by [排序列] 排序规则, [排序列] 排序规则...

- 排序列：按照哪个列排序，可以省略
- 排序规则：**ASC（升序），DESC（降序）**

```mysql
-- 查询学生表中的成绩升序排序
select achievement, name from student order by achievement ASC;
```

### 条件查询

> select 列 from 表 where 条件

- 条件：布尔表达式，在查询的结果中筛选符合条件的数据

#### 等值判断（=）

```mysql
-- 查询学生表中成绩等于100的学生
select * from student where achievement = 100;
```

#### 不等值判断（>、<、<=、>=、!=、<>)

```mysql
-- 查询学生表中成绩大于90的学生
select * from student where  achievement > 90;
```

#### 逻辑判断（and、or、not）

```mysql
-- 查询学生表中成绩在80到90的学生(包含80和90)
select * from student where achievement >= 80 and achievement <= 90;
```

#### 区间判断（between and）

```mysql
-- 查询学生表中成绩在80到90的学生(包含80和90)
select * from student where achievement between 80 and 90;
```

#### NULL 值判断（IS NULL、IS NOT NULL）

```mysql
select * from student where achievement is NULL;
```

#### 枚举查询（IN）

```mysql
-- 查询成绩为70,80,90的学生
select * from student where achievement in(70, 80, 90);
```

#### 模糊查询（like）

> select 列 from 表 where 列 like _
>
> select 列 from 表 where 列 like %

- _ ：单个任意字符
- %：任意长的任意字符

```mysql
-- 查询姓李的学生,名字长度为2的
select * from student where name like '李_';
-- 查询姓李的学生
select * from student where name like '李%';
```

### 分支结构查询

> case 
> 	when 条件1 then 结果1
> 	when 条件2 then 结果2
> 	when 条件3 then 结果3
> 	else 结果
> end

```mysql
-- 给学生的成绩打级别ABCD
select name, achievement, 
case 
    when achievement >= 90 then 'A'
    when achievement >= 80 and achievement < 90 then 'B'
    when achievement >= 70 and achievement < 80 then 'C'
    else 'D'
end as '级别'
from student;
```

### 聚合函数

> select 聚合函数(列) from 表;

- sum()：和
- avg()：平均值
- max()：最大值
- min()：最小值
- count()：总行数（忽略NULL）

```mysql
-- 计算成绩平均值
select avg(achievement) from student;
```

### 分组查询（group by）

> select 列 from 表 where 条件 group by 列(分组依据);

```mysql
-- 查询学生中各个年龄的人数
select age, count(id) from student group by age;
```

- ***分组查询中显示的列一般是分组依据列，否则会出错***

#### 分组过滤查询（having）

> select 列 from 表 where 条件 group by 列(分组依据) having 过滤规则;

```mysql
-- 查询学生中年龄为16, 17, 18的人数
select age, count(id) from student group by age having age in(16, 17, 18);
```

### 限定查询

> select 列 from 表 limit 起始行, 总行数

```mysql
# 查询前5行
select achievement from student limit 0, 5
```

- ***0 从第一行开始***
- 5 查询行数为5

### 子查询

#### 子查询是单行单列

```mysql
-- 平均成绩
select avg(achievement) from student;
-- 成绩大于平均成绩的学生
select * from student where achievement > (select avg(achievement) from student);
-- 所有姓李的学生的成绩
select achievement from student where name like '李%';
-- 成绩比姓李的高的所有学生的成绩
select * from student where achievement > all(select achievement from student where name like '李%');
```

- ALL ：所有
- ANY：部分

#### 子查询是多行多列

```mysql
-- 查询学生中所有姓李的信息并按成绩排序
select * from student where name like '李%' order by achievement desc;
-- 学生中姓李的成绩前5名
select * from (select * from where name like '李%' order by achievement desc) as temp limit 0, 5;
```

- **<u>子查询出来的表一定要有一个临时表名</u>**



### 合并查询

>  select * from t1 union select * from t2;

- 合并列数必须相同

- union：会去重

- union all：不会去重