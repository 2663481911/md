## 创建数据库

> create database 数据库名称;

```mysql
-- 创建数据库名称为hello的数据库
create database hello;
```

### 指定编码的数据库

> create database 数据库名称 character set 编码;

```mysql
-- 创建数据库名称为hello的数据库并指定编码为gbk
create database hello character set gbk;
```

### 数据库不存在，创建数据库

> create database if not exists 数据库名称;

```mysql
-- 创建数据库hello
create database if not exists hello;
```

### 查看如何创建数据库

```mysql
show create database 数据库名称;
```

## 修改数据库

### 修改数据库编码

> alter database 数据库名称 character set utf8;

```mysql
-- 修改数据库hello的编码为utf-8
alter database hello character set utf8;
```

## 删除数据库

> drop database 数据库名称;  

```mysql
-- 删除数据库hello
drop database hello;
```

- 