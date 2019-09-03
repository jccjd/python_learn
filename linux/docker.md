### 常用命令
    
    docker pull training/webapp 载入镜像
    docker run -d -P training/webapp python app.py 将端口映射到主机
    docker logs -f bf08b7 # 打印日志
    docker stop wizardly_chandrasekhar 停止应用
    

### docker-compose
直接可以使用 pip安装
    
    sudo pip install -U docker-compose
    $ curl -L https://raw.githubusercontent.com/docker/compose/1.24.1/contrib/completion/bash/docker-compose > /etc/bash_completion.d/docker-compose
    