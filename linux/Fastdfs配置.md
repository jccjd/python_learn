---
data: 2019-10-16
---

### what is FASTDFS
简单来说就是非常快的文件管理系统, 由 `c语言`编写的轻量级的分布式文件系统

- 功能包括：文件存储、文件访问（文件上传、文件下载）、文件同步等，解决了大容量存储和负载均衡的问题。特别适合以文件为载体的在线服务，如相册网站、视频网站等等。
- 为互联网量身定制，充分考虑了冗余备份、负载均衡、线性扩容等机制，并注重高可用、高性能等指标。
- 可以帮助我们搭建一套高性能的文件服务器集群，并提供文件上传、下载等服务

在项目中将大文件的存取交给它去操作,可以提高项目性能

整个系统分为两部分,一个是`tracker server`,来接受客户端的请求,分配任务, `Storage server` 负责具体的文件的存储,管理文件


### FastDFS上传和下载流程

**上传文件**

1. `storage server`定时向`tracker`上传状态信息
2.  客户端向`stracker server`发送上传链接请求
3.  `stracker`查询可用的`storage`并返回`Storage`的ip和端口
4.  客户端上传文件(`file content & metadata`) 到`storage`
5.  `storage`将生成`file_id`并将数据写入磁盘,返回路径信息和文件名(`file_id`)


**下载文件**
1. 'storage' 依然向`tracker`上传状态信息
2. 客户端向 `stracker server`发送下载链接请求
3. `stracker`返回可用的`storage`的ip和端口
4. 客户端向`storage`通过`file_id`的到文件


### 在Docker中运行Fastdfs

**从仓库中拉取dfs镜像**

    docker image pull delron/fastdfs

**开启tracker服务**

将`/var/fdfs/tracker`当做运行目录

    sudo docker run -dit --name tracker --network=host -v /var/fdfs/tracker:/var/fdfs delron/fastdfs tracker
**开启storage服务**

local_ip是本机的内网ip,而非`127.0.0.1`,如果要镜像外网访问这里要设置内网ip

    sudo docker run -dti --name storage --network=host -e TRACKER_SERVER=local_ip:22122 -v /var/fdfs/storage:/var/fdfs delron/fastdfs storage

*在开启和关闭storage服务的时候会遇到,关闭之后不能开启的情况, 将`fdfs_storaged.pid`删除,再重启*


### 客户端连接Fastdfs
*安装`Fastdfs_client`*

    git clone https://github.com/JaceHo/fdfs_client-py.git
    cd fdfs_client
    python setup.py install

`Fastdfs_client`还需要`mutagen`支持

    pip install mutagen


*客户端配置*

在连接的时候需要加载配置,配置如下, 需要的基础配置有`base_path`(日志目录), `connect_timeout`(超时时间), `tracker_server`(服务ip和端口)

    base_path=/home/io/Desktop
    # connect timeout in seconds
    # default value is 30s
    connect_timeout=30

    # network timeout in seconds
    # default value is 30s
    network_timeout=120

    # the base path to store log files
    base_path=/home/io/Desktop/

    # tracker_server can ocur more than once, and tracker_server format is
    #  "host:port", host can be hostname or ip address
    tracker_server=47.97.91.156:22122

    #standard log level as syslog, case insensitive, value list:
    ### emerg for emergency
    ### alert
    ### crit for critical
    ### error
    ### warn for warning
    ### notice
    ### info
    ### debug
    log_level=info

    # if use connection pool
    # default value is false
    # since V4.05
    use_connection_pool = false

    # connections whose the idle time exceeds this time will be closed
    # unit: second
    # default value is 3600
    # since V4.05
    connection_pool_max_idle_time = 3600

    # if load FastDFS parameters from tracker server
    # since V4.05
    # default value is false
    load_fdfs_parameters_from_tracker=false

    # if use storage ID instead of IP address
    # same as tracker.conf
    # valid only when load_fdfs_parameters_from_tracker is false
    # default value is false
    # since V4.05
    use_storage_id = false

    # specify storage ids filename, can use relative or absolute path
    # same as tracker.conf
    # valid only when load_fdfs_parameters_from_tracker is false
    # since V4.05
    storage_ids_filename = storage_ids.conf


    #HTTP settings
    http.tracker_server_port=80

    #use "#include" directive to include HTTP other settiongs
    ##include http.conf

*测试连接*

    >>> from fdfs_client.client import *
    >>> client = Fdfs_client('/etc/fdfs/client.conf')
    >>> ret = client.upload_by_filename('绝对路径')
