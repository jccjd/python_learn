在服务器端配置nginx + uwsgi+ django,简单来讲就是将django的项目通过nginx跑起来，在阅读djang
文档的时候就读到一句非常有意思的话，
> 我们是框架方面的专家， 但在在服务方面不是

在实际的项目中显然是不能使用django自带的wsgi去跑的， 我们希望的是由nginx来提供服务的.

### 下载uwsgi
首先三者之间的顺序是 nginx -> （uwsgi ->djangoapp）, uwsgi 和写的django项目相连，在启动项目时，不在是由 manage.py 去启动项目，而是在项目根目录下配置的`uwsgi.ini` 用uwsgi去运行这个文件，来运行项目， 下载 uwsgi,可以直接通过pip安装
    
    pip install uwsgi
    
    uwsgi uwsgi.ini # 运行项目

这时候显然还是不能运行的要配置 `uwsgi.ini`
    
    [uwsgi]
    chdir = /root/mysite //项目根目录-要是绝对路径
    module = mysite.wsgi:application //指定wsgi模块

    socket = 0.0.0.0:8000 //这里一定要和下面uginx的一致
    #vhost = true          //多站模式
    #no-site = true        //多站模式时不设置入口模块和文件
    #workers = 2           //子进程数
    #reload-mercy = 10
    #vacuum = true         //退出、重启时清理文件
    #max-requests = 1000
    #limit-as = 512
    #buffer-size = 30000
    #pidfile = /var/run/uwsgi9090.pid    //pid文件，用于下脚本启动、停止该进程
    daemonize = /home/feixue/python/www/for_test/run.log    // 日志文件这个文件一般是没有的要自己新建
    disable-logging = true   //不记录正常信息，只记录错误信息
配置完就可以在本地跑了，不出意外的话，一般这里没啥意外，有的话可以看一下报错信息，
第一次配置的错误是chdir 路径填错了找不到

### 安装nginx和配置
nginx直接apt-get即可安装,主要配置在目录/etc/nginx/sites-available/default,关键配置如下

    
    # include snippets/snakeoil.conf;

    # root /var/www/html;

    # Add index.php to the list if you are using PHP
    # index index.html index.htm index.nginx-debian.html;

    server_name _;

    location / {
        # First attempt to serve request as file, then
        # as directory, then fall back to displaying a 404.
        # try_files $uri $uri/ =404;
        include  uwsgi_params;
                uwsgi_pass  0.0.0.0:8000; # 和uwsgi的是一样的  
    }
    # pass the PHP scripts to FastCGI server listening on 127.0.0.1:9000

然后就是阿里云的安全组的问题，默认的阿里云是开放公网端口的所以需要，为nginx的80端口添加允许通过网关的安全组，在其中有一栏的端口要 `0.0.0.0：80`，开放之后即使不配置nginx 启动nginx，也可以通过公网ip加端口直接访问.



