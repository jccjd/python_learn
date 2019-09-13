####  mysql  密码修改
在mysql5.6和5.7的密码修改方式发生了很大的变化，5.7是可以直接通过mysql进入数据即库然后通过下面命令
直接修改即可

    UPDATE mysql.user SET plugin="mysql_native_password", authentication_string=PASSWORD("password") WHERE user="root";

5.6是直接登入不上，要进入mysql的配置文件添加字段 跳过登陆验证，进入数据库在修改密码
`UPDATE user SET Password = 'new-password' WHERE User = 'root';` 之后注释掉刚才的字段

    
    skip-grant-tables 
    # Remove leading # and set to the amount of RAM for the most important data
    # cache in MySQL. Start at 70% of total RAM for dedicated server, else 10%.
    # innodb_buffer_pool_size = 128M
    #
    # Remove leading # to turn on a very important data integrity option: logging
    # changes to the binary log between backups.
    # log_bin
    #
    # Remove leading # to set options mainly useful for reporting servers.
    # The server defaults are faster for transactions and fast SELECTs.
    # Adjust sizes as needed, experiment to find the optimal values.
    # join_buffer_size = 128M
    # sort_buffer_size = 2M
    # read_rnd_buffer_size = 2M
    datadir=/var/lib/mysql
    socket=/var/lib/mysql/mysql.sock
    skip-grant-tables                       <<<<<<<<------------------
    # Disabling symbolic-links is recommended to prevent assorted security risks
    symbolic-links=0
    
#### 启动
    mysql -u root -p


#### 查看端口

    show global variables like 'port';

#### 版本信息
    select version();
    show databases 
    show tables
#### 表结构 
    show columns from 表名;
    
### insert
可以不用填完

    insert into tablename (args1, args2,...) values (value1,value2,...)


### linux 使用 navcate
启动Navicat premium：
    
    ./start_navicat
    
界面中文乱码问题，进入安装目录后，执行：

    vi  start_navicat
    将export LANG=" "改为
    export LANG="zh_CN.UTF-8"

如果到期的话，可以先调出终端执行

    cd ~
    rm -rf .navicat64
    ./start_navicat
