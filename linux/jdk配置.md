### 修改环境变量

```shell
sudo vim /etc/bash.bashrc
```
### 在最后添加

```shell
JAVA_HOME=/home/lss/jdk-10.0.2   # jdk位置
CLASSPATH=.:$JAVA_HOME/bin.tools.jar
PATH=$JAVA_HOME/bin:$PATHs
export JAVA_HOME CLASSPATH PATH
```
### 生效

```shell
    source /etc/bash.bashrc
```



