### what is Docker

    Docker是一款针对程序开发人员和系统管理员来开发、部署、运行应用的一款虚拟化平台。
    Docker 可以让你像使用集装箱一样快速的组合成应用，并且可以像运输标准集装箱一样，
    尽可能的屏蔽代码层面的差异。Docker 会尽可能的缩短从代码测试到产品部署的时间。


docker是一种虚拟机技术,于传统的虚拟机技术,不同docker是直接使用宿主的的内核,他没有对硬件进行
虚拟,因此从此方面将要虚拟设备跟轻便.

它是一种对开发而言更为适合的虚拟方式, 在开发过程中 docker可以提供除了内核外完成的开发运行环境,可以保证应用环境的一致性,解决了历史性难题`这代码在我的电脑上没问题,在你电脑上就有bug了`


**docker 要求linux的内核要在3.10以上,安装前要查看linux的内核版本`uname -r`**

### docker的三个基本概念
- Image
- Container
- Repository

### *Image*

Docker 镜像是一个特殊的文件系统，除了提供容器运行时所需的程序、库、资源、配置等文件外，还包含了一些为运行时准备的一些配置参数（如匿名卷、环境变量、用户等）。镜像不包含任何动态数据，其内容在构建之后也不会被改变。

### *Container*
容器和镜像和的关系相当于类和实例的关系,容器是镜像运行的实体.

**如果要删除某个镜像, 需要先删除该镜像的创建出的所有容器, 因为容器在运行时会有守护进程**

### *Repository*

### docker安装
docker可以直接使用`pip`进行安装

    sudo pip install -U docker-compose

### 常用命令

#### 启动/关闭/重启/docker
    sudo service docker start/stop/restart
#### 镜像列表
    sudo docker image ls
#### 从仓库获取镜像
    sudo docker pull imagename

#### 查看镜像的container
    docker ps -a

#### 删除container
    docker rm containerid
#### 运行container
    docker start Containerid
#### 删除镜像
    sudo docker image rm imagename/imageid
在删除镜像之前要先停止该镜像的容器

### 启动容器

#### 交互式容器
    sudo docker run -it --name=name1 imagename cmd

#### 守护式容器

    sudo docker run -dit --name=ubuntu1 ubuntu cmd

    * -i 表示以《交互模式》运行容器。
    * -t 表示容器启动后会进入其命令行。加入这两个参数后，容器创建就能登录进去。即分配一个伪终端
    * --name 为创建的容器命名。
    * -v 表示目录映射关系，即宿主机目录:容器中目录。注意:最好做目录映射，在宿主机上做修改，然后共享到容器上。
    * -d 会创建一个守护式容器在后台运行(这样创建容器后不会自动登录容器)。
    * -p 表示端口映射，即宿主机端口:容器中端口。
    * --network=host 表示将主机的网络环境映射到容器中，使容器的网络与主机相同。

### 进入容器

    sudo docker exec -it Containerid/name cmd

#### 将端口映射到主机
docker run -d -P training/webapp python app.py

#### 打印日志
docker logs -f bf08b7


### docker-compose
直接可以使用 pip安装

    sudo pip install -U docker-compose

    $ curl -L https://raw.githubusercontent.com/docker/compose/1.24.1/contrib/completion/bash/docker-compose > /etc/bash_completion.d/docker-compose

### 将容器做成镜像

    docker commit containername/id imagename

### 打包镜像
    docker save -o filename imageid
### 镜像重新装载到 docker中
    docker load -i localpath/filename

###  FastDFS的Docker配置
