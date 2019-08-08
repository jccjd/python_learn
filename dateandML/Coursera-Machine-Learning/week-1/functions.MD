#### Model Representation 

To describe the supervised learning problem slightly more formally, our goal is, given a training set, to learn a function h : X → Y so that h(x) is a “good” predictor for the corresponding value of y. For historical reasons, this function h is called a hypothesis. Seen pictorially, the process is therefore like this:


在给定训练集的情况下，学习函数h：X——>Y,使得h(x) 是y的相应值的好预测器。由于历史原因，这个函数h被称为假设。从图中可以看出这个过程是这样的：

 ![image](https://camo.githubusercontent.com/32d1402d812f48fa3a9078f8acec0fa1e41c6396/68747470733a2f2f696d672e68616c66726f73742e636f6d2f426c6f672f41727469636c65496d6167652f36385f305f312e706e67)
> 图中输入住房面积x，经函数h，输出房子的估价y

#### Cost function （代价函数）
我们可以使用成本函数来衡量我们的假设函数的准确性。 这需要假设的所有结果与来自x和实际输出y的输入的平均差异（实际上是平均值的更高版本，即使平方差公式）

 ![image](https://github.com/jccjd/Coursera-Machine-Learning/blob/master/week-1/tu/costfunction.PNG?raw=true)
 
 代价函数是线性回归中的一个应用，在线性回归中，要解决的一个问题就是最小化问题，
 假设直线方程 如何使得函数更加拟合于训练集
 那么就需要costFunction来找到最小误差的方程
 > hθ(X) = 1(θ0) + x(θ1)

#### Gradient Descent(梯度下降)
梯度下降的主要思想：
1. 初始化θ0和θ1，θ0 = 0，θ1 = 0;
2. 不断的改变θ0和θ1的值 ，不断减少f（θ0，θ1）直到最小值或局部最小


![image](https://github.com/jccjd/Coursera-Machine-Learning/blob/master/week-1/tu/gradient.png?raw=true)
 
当成本函数位于图中凹坑的最底部时，即当它的值最小时，我们就知道我们已经成功了。红色箭头显示图表中的最小点

这样做的方法是采用成本函数的导数（一个函数的切线）。 切线的斜率是该点的导数，它将为我们提供朝向的方向。 我们在最陡下降的方向上降低成本函数。 每个步骤的大小由参数α确定，该参数称为学习率。

较小的α将导致较小的步长，较大的α将导致较大的步长。

梯度下降算法是：

![image](https://github.com/jccjd/Coursera-Machine-Learning/blob/master/week-1/tu/functions_gradient.PNG?raw=true)

然后不断更新直到收敛

![image](https://github.com/jccjd/Coursera-Machine-Learning/blob/master/week-1/tu/functions_gradient_2.PNG?raw=true)

> 注意θ1 和 θ0 要同时更新

如果 α 被设置的很小，需要很多次循环才能到底最低点。 如果 α 被设置的很大，来来回回可能就会离最低点越来越远，会导致无法收敛，甚至发散。
当快要到最低点的时候，梯度下降会越来越慢。

#### Gradient Descent For Linear Regression

当实际运用到线性回归中可以导出新的方程：

![image](https://github.com/jccjd/Coursera-Machine-Learning/blob/master/week-1/tu/functions_gradient3.PNG?raw=true)
> 1. m:训练集大下
> 2. xi，yi：训练集数据的值
> 3. θ1 和 θ0 要同时更新

