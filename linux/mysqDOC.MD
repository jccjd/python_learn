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
