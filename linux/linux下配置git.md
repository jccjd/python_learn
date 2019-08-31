### linux下配置 SSH 密钥
配置git 的SSH 密钥让本地和远程建立连接然后可以实现同步代码仓库

#### 查看本机是否存在 SSH keys
    
    cd ~/.ssh

#### 创建一对新的 SSH keys
    
    ssh-keygen -t rsa -C "email@example.cpm"
可以直接回车三连，不设置密码，设置密码的话每次提交都会让输入很难受的
得到公钥如下结构
    long@King:~/.ssh$ ls
    id_rsa  id_rsa.pub  known_hosts
将 `id_rsa.pub` 打开复制下来，添加`github`中的setting>SSH and GPG keys>new SSH key
随便起个名字将 公钥内容粘到下面直接生成即可
#### 测试SSH
出现以下内容即可

    long@King:~/.ssh$ ssh -T git@github.com
    Hi jccjd! You've successfully authenticated, but GitHub does not provide shell access
        
