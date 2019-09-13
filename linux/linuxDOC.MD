### 所常用命令
#### py2和py3和pip2和pip3
在py2和py3 pip2 and pip3之间自由切换主要是软连接的切换
    
    
    sudo apt-get install python3-pip  # 下载pip 
    whereis python
    ls -l /usr/bin | grep python
    mv /usr/bin/python /usr/bin/python.bak
    ln -s /usr/local/bin/python3 /usr/bin/python
    

`卸载软件包`

    sudo apt-get autoremove [packagename]   | 自动删除
    sudo apt-get remove [package]           | 删除
    sudo apt-get remove package --purge     | 包括配置文件
    sudo apt-get upgrade [package]          | 更新
    sudo apt-cache depends package          | 该包依赖那些包
    sudo apt-cache rdepends package         | 该包被哪些包依赖
    sudo apt-get clean                      | 清理吴用的包
    sudo apt-get autoclean                  | 自动清理
`更换pip的源`

    mkdir ~/.pip
    vim ~/.pip/pip.conf
输入内容, 地址为国内的一些源，可以更换

    [global]
    index-url = https://mirrors.aliyun.com/pypi/simple

    
    清华：https://pypi.tuna.tsinghua.edu.cn/simple
    中国科技大学 https://pypi.mirrors.ustc.edu.cn/simple/
    华中理工大学：http://pypi.hustunique.com/
    山东理工大学：http://pypi.sdutlinux.org/
    豆瓣：http://pypi.douban.com/simple/

### 报错
    Could not install packages due to an EnvironmentError: [Errno 13] 权限不够: '/usr/local/lib/python3.7/dist-packages/wheel-0.33.4.dist-info'
    Consider using the `--user` option or check the permissions.

需要在最后加上 `--user`

    pip install tensorflow --user

### 快捷键
`ctrl +shift -`, `ctrl -` 终端窗口的缩放
### ls
    
    ls -a 显示所有信息
    ls -l 列表
    ls -h 默认状态
ls的通配
    
    ls te* 显示以te开头的
    ls *html 以html结束的文件
    ls ?.c 只找第一个字符任意，后缀为.c的文件

### rm
    
    rm -i 删除前询问
    rm -f 强制删除
    rm -r 递归删除删除文件夹
    
### cp

	    
    cp -a 保留文件原有属性
    cp -f 若有重复不提示
    cp -i 若有重复请求用户确认
    cp -r 递归复制，复制文件夹
    cp -v view 
    
从服务器拷贝
	
	scp -r /etc root@192.168.60.135:/opt # 将本地的etc 拷到 服务器去
	scp root@192.168.60.133:/home/ixdba/etc.tar.gz /tmp 
### 重定向
    
    ls > test.txt ls的输出会存储在test.txt中

### 管道
一个命令的输出是另一个命令的输入
    
    ls -lh | more
    
### ln
`默认` 是硬链接

`软链接`:源文件失效也失效

`硬链接`:只能链接普通文件

    硬链接：ln 源文件 链接文件
    软链接：ln -s 源文件 链接文件

### grep
`匹配`
    
    grep -[] 'target' filename.txt
    
    -V 取反
    -n 显示行号
    -i 不区分大小写
    example:
       grep -in 'target' filename.txt

### grep 的正则式
    
    搜索每一行的
    ^a: 以a开头的 grep -n '^a' filename.txt
    $: 以某一字符结尾的 grep -n '$et' filename.txt
    []搜索某个单词，：grep -n '[tT]est' filename.txt
    .:点匹配：grep -n 't..t' filename.txt(.是占位)

### find
    
    # find name is ww.txt in ./ file
    find ./ -name ww.txt    
    # find name end is .sh in ./ file
    find ./ -name '*.sh'
    # find start with A - Z
    find ./ -name '[A-Z]*'
    finde /tmp -size +-size
    finde /tmp -size +size -size -2m
    #查找权限为777的文件
    find /tmp -perm 777
### tar
打包文件 压缩`当前文件`的内容

    -c creat
    -v view
    -f filename
    -z zip
    -x 解压
    # 打包
    tar -cvf name.tar *
    #打包加压缩 将当前路径的所有的东西压缩到 
    # name.tar.gz 
    tar -zcvf name.tar.gz *
    #解压到指定路径 
    -C
    tar -zxvf name.tar.gz -C path/
### gzip 
没啥雕用 还不如直接用tar 去压缩 而且压缩后的包要比tar的大

    -r 压缩： gzip -r name.tar 生成的是.tar.gz
    -d 解压: gzip -d name.tar.gz -> name.tar
### zip

    # 压缩
    zip name * ： 压缩到name里
    
    # 解压到当前目录下的test下，没有则创建
    unzip -d ./test name.zip 
### which
显示命令的位置；
    
    which pip -> /usr/local/bin/pip
    which ls -> /usr/bin/ls
    

### 权限修改（chmod)
权限修改 字母和数字法
字母：

    u: user
    g: group
    o: other
    a: all
    + - =： 增加 减少 设定
    r w x: 读写执行
    
    # user---group---all--- 权限分布
    rwxrw-rw- 1 long long  18 8月   9 15:27 ee.txt
    -rw-r--r-- 1 long long 302 8月   9 15:09 name.zip
    -rw-r--r-- 1 long long   0 8月   9 14:52 qq.txt
如上的权限比如 `ee.txt` 文件的权限
 - user有rwx权限 : 减权限 chmod u-x ee.txt
 - group有rw权限:chmod u=rwx,g-w,a=rw ee.txt
 - all 有 r权限
 
 `qq.txt`的权限
 - user -> rw : 加权限 chmod u+x qq.txt
 - group -> r: 加权限 chmod g+w qq.txt
 - all -> r : 加权限 chmod a+w qq.txt

数字表示
    
    r -> 4
    w -> 2
    x -> 1
    - -> 0
`chmod 777 file.txt` 表示 u g a 的权限数字加起来


### 修改密码

    
    sudo -s             | 进入super user
    passwd username     | 修改密码
    exit                | 退出root
### who
查看用户登陆
    
      -q    | 用户登陆的数量
      
### 注销，重启
    
    reboot              |    重启
    shutdown -r now     | 重启，但会给别的用户提示
    shutdown -h now     | 关机 现在
    shutdown -h 12:00   | 12: 00关机
    shutdown -h +10     | 系统再过十分钟关闭

### SSH

SSH为`Secure Shell`的缩写，由 `IETF` 的网络工作小组（Network Working Group）所制定；
SSH 为建立在应用层和传输层基础上的安全协议。

SSH是目前较可靠，专为远程登录会话和其他网络服务提供安全性的协议。常用于远程登录，以及用户之间进行资料拷贝。

利用SSH协议可以有效防止远程管理过程中的信息泄露问题。SSH最初是 UNIX 系统上的一个程序，后来又迅速扩展到其他操作平台。SSH 在正确使用时可弥补网络中的漏洞。SSH 客户端适用于多种平台。几乎所有 UNIX 平台—包括 HP-UX、Linux、AIX、Solaris、Digital UNIX、Irix，以及其他平台，都可运行SSH。

使用SSH服务，需要安装相应的服务器和客户端。客户端和服务器的关系：如果，A机器想被B机器远程控制，那么，A机器需要安装SSH服务器，B机器需要安装SSH客户端。

### vim
    
    u            | 撤销
    ctrl+r       | 反撤销
    yy           | 复制
    p            | 粘贴
    /            | 查找 ->回车后 n N 上下选择
    %s/abc/123  | 替换 -> 将abc 替换成123 % 可以为数字区间1,10
    
### top
动态查看进程


