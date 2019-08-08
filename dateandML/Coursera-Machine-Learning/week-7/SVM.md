### SVM
最早是由 Vladimir N.Vapnik 和 Alexey Ya. Chervonenkis 在1963年提出

目前的版本（soft margin)是由Corinna Cortes 和 VaPnik 在1993年提出，并在1995年发表

深度学习（2012）出现之前，svm被认为机器学习中近十几年来最成功，表现最好的算法

![image](https://github.com/jccjd/Coursera-Machine-Learning/blob/master/week-7/image/SVM1.PNG?raw=true)

svm寻找区分两类的超平面（hyper plane)使边际（margin）最大

![image](https://github.com/jccjd/Coursera-Machine-Learning/blob/master/week-7/image/SVM1.PNG?raw=true)


### 向量内积

x = {x1,x2,x3....xn}

y = {y1,y2,y3....yn}

向量内积：

![image](https://github.com/jccjd/Coursera-Machine-Learning/blob/master/week-7/image/向量内积1.PNG?raw=true)


![image](https://github.com/jccjd/Coursera-Machine-Learning/blob/master/week-7/image/向量内积2.PNG?raw=true)

几何表示：

![image](https://github.com/jccjd/Coursera-Machine-Learning/blob/master/week-7/image/向量内积5.PNG?raw=true)


范数：

![image](https://github.com/jccjd/Coursera-Machine-Learning/blob/master/week-7/image/向量内积3.PNG?raw=true)

当||x|| =/ 0 ，||y||=/0 时，可以求余弦相似度：

![image](https://github.com/jccjd/Coursera-Machine-Learning/blob/master/week-7/image/向量内积4.PNG?raw=true)


### 线性不可分的情况

![image](https://github.com/jccjd/Coursera-Machine-Learning/blob/master/week-7/image/线性不可分1.PNG?raw=true)

如果出现这种情况发生线性不可分需要进行改进，松弛变量与惩罚函数
    
    yi(wi*xi + b) >1 -εi,εi>0
    约束条件没有体现错误分类的点要尽量究竟分类边界
    
    min(||w||^2 / 2) + C * sum(εi)
    使得分错的点越少越好，距离分类边界越近越好
线性不可分情况下的对偶问题

![image](https://github.com/jccjd/Coursera-Machine-Learning/blob/master/week-7/image/线性不可分1.PNG?raw=true)

> s.t.,C>аi>0, i =1,
### SVM低维映射

![image](https://github.com/jccjd/Coursera-Machine-Learning/blob/master/week-7/image/SVM4.PNG?raw=true)

非线性情况把低维空间的非线性问题映射到高维空间，变成求解线性问题

![image](https://github.com/jccjd/Coursera-Machine-Learning/blob/master/week-7/image/SVM5.PNG?raw=true)

演示：
https://v.qq.com/x/page/k05170ntgzc.html

### 核函数

我们可以构建核函数使得运算结果等同于非线性映射，同时运算量要远远小于非线性映射

    K(x1,ji) = φ(xi)φ(xj)
    
h次多项式核函数：K(xi,xj) = (xi,xj+1)^h
高斯径向基数核函数：K(xi,xj) = e^-(||xi,xj||)^2/2σ^2
S型核函数：K(xi,xj) = tanh(k Xi*Xj -σ)

核函数举例

假设定义两个向量： x = (x1,x2,x3);y=(y1,y2,y3)

定义高维映射方程：f(x) = (x1x1,x1x2,x1x3,x2x1,x2x2,x2x3,x3x1,x3x2,x3x3)

假设x = (1,2,3),y=(4,5,6)

f(x) = (1,2,3,2,4,6,3,6,9)

f(y) = (16,20,24,20,25,36,24,30,36)

求内积<f(x),f(y)> = 16 +40+72+40+100+180+72+180+324=1024


定义核函数：K(x,y)=(<f(x),f(y)>^2

K(x,y) = (4+10+18)^2=1024

同样的结果，使用核函数方法计算容易得多



### svm优点

- 训练好的模型的算法复杂度是由支持向量的个数决定的而不是由数据的维度决定的。所以svm不太容易产生overfitting
- svm训练出来的模型完全依赖于支持向量，即使训练集里面所有非支持向量的点都被去除，重复训练过程，结果任会得到完全一样的模型。
- 一个svm如果训练得出的支持向量个数比较小，svm训练出的模型比较容易被泛化。














