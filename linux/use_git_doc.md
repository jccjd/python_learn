### 常用
    
    git init
    git add (new filename changed filename).md
    git commit -m 'some message'
    git status
    git diff filename.md
    
    git log --pretty=oneline
    
    回滚到前一个版本
    git reset --hard HEAD^
    回滚到后一个版本，需要知道版本号只要知道前几个数字即可
    git reset --hard version_name

    可以知道每次version 的内容，方便找到版本号
    git reflog
    