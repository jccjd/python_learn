### 所常用命令
1. 卸载软件包

    sudo apt-get autoremove [packagename]

**更换pip的源**

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
### 重定向
    
    ls > test.txt ls的输出会存储在test.txt中

### 管道
一个命令的输出是另一个命令的输入
    
    ls -lh | more
    
### ln
默认 是硬链接
软链接:源文件失效也失效
硬链接:只能链接普通文件

    硬链接：ln 源文件 链接文件
    软链接：ln -s 源文件 链接文件

### grep
匹配
    
    grep -[] 'target' filename.txt
    
    -V 取反
    -n 显示行号
    -i 不区分大小写

    