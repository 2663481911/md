## shell

$：表示普通用户

#：表示管理员用户root

root是Linux系统中权限最高的用户。

用sudo <command> <arguments>执行命令的效果和root一样。



## 基本命令

通用语法格式：指令名称 [选项] [操作的目标]

#### cat   这个命令是将文件中的内容显示到shell窗口中

- 显示当前目录下单1.py文件内容

  ```shell
  cat ./1.py
  ```

#### ls 默认参数为当前目录 ,

- ls -l显示详细的列表
- ls -F显示文件类型信息

- ls -a 显示隐藏文件
  - 显示当前目录下的后缀为py文件

    ```
    ls *.py
    ```

#### cp: 复制文件,可复制多个文件

- 复制1.py、2.py文件到pp文件夹里

  ```shell
  cp 1.py 2.py pp
  ```

#### mv : 重命名，移动文件

- 重命名1.py为2.py

  ```shell
  mv 1.py 2.py
  ```

- 移动1.py,2.py文件到文件夹pp

  ```shell
  mv 1.py 2.py pp
  ```

- 移动.py文件到pp

  ```shell
  mv *.py pp
  ```

#### touch ： 创建文件

- 创建3.py文件

  ```shell
  touch 3.py
  ```

#### rm: 用来删除文件

- 删除3.py文件

  ```
  rm 3.py
  ```

#### mkdir: 创建新目录

- 创建cc文件夹

  ```shell
  mkdir cc
  ```

#### rmdir 删除目录

#### grep :显示文件和输入流中和参数匹配的行

- 显示当前目录下所有文件中有s的行

  ```shell
  grep s ./*
  ```

#### less : 要查看的文件过大或者内容多得需要滚动屏幕的时候，可以使用less命令

- 按空格键可查看下一屏，B键查看上一屏，Q键退出

#### pwd 显示当前工作目录

#### file 一个文件的格式信息

#### diff 对比两个文件不同



