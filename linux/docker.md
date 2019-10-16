它是一种对开发而言更为适合的虚拟方式, 在开发过程中 docker可以提供除了内核外完成的开发运行环境,可以保证应用环境的一致性,解决了历史性难题`这代码在我的电脑上没问题,在你电脑上就有bug了`
### 常用命令

    docker pull training/webapp 载入镜像
    docker run -d -P training/webapp python app.py 将端口映射到主机
    docker logs -f bf08b7 # 打印日志
    docker stop wizardly_chandrasekhar 停止应用


### docker-compose
直接可以使用 pip安装

    sudo pip install -U docker-compose
    $ curl -L https://raw.githubusercontent.com/docker/compose/1.24.1/contrib/completion/bash/docker-compose > /etc/bash_completion.d/docker-compose


###  FastDFS的Docker配置
