- 下载`tgz`文件
  - > 　https://fastdl.mongodb.org/linux/mongodb-linux-x86_64-debian10-4.2.7.tgz

  - 解压

  - 移动到自己想要保存到路径

- 建立/data/db文件夹

  - ```shell
    sudo mkdir -p /data/db
    sudo chmod 0755 /data/db
    ```

- 建立配置文件

  - 在`mongdb`(文件夹下有bin目录)安装位置文件夹下

    ```shell
    mkdir logs
    touch mongodb.log
    vim mongodb.config
    ```

  - 文件内容

    ```shell
    dbpath=/data/db   # 数据库文件路径
    port=27017        # 端口号
    bind_ip = 0.0.0.0
    logpath=/home/lss/mongodb/logs/mongodb.log #日志输出文件路径
    #以守护程序的方式启用，即在后台运行
    fork = true
    # 认证模式
    # auth=true
    ```

- 在系统服务目录下新建mongodb的启动服务

  - 输入

    ```shell
    cd /lib/systemd/system
    sudo vim mongodb.service
    ```

  - 内容

    ```shell
    [Unit]
      
    Description=mongodb
    After=network.target remote-fs.target nss-lookup.target
      
    [Service]
    Type=forking
    
    #根据自己文件所在位置改下面内容
    ExecStart=/usr/local/mongodb/bin/mongod --config /usr/local/mongodb/mongodb.conf   
    ExecReload=/bin/kill -s HUP $MAINPID
    ExecStop=/usr/local/mongodb/bin/mongod --shutdown --config /usr/local/mongodb/mongodb.conf
    
    
    PrivateTmp=true
    [Install]
    WantedBy=multi-user.target
    ```

  - 754权限

    ```shell
    chmod 754 mongodb.service
    ```

- ```
  启动
  systemctl start mongodb.service
  关闭
  systemctl stop mongodb.service
  
  注册到开机启动
  systemctl enable mongodb.service
  ```

