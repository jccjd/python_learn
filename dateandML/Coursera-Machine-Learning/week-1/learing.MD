#### What is Machine Learning?
Two definitions of Machine Learning are offered. Arthur Samuel described it as: "the field of study that gives computers the ability to learn without being explicitly programmed." This is an older, informal definition.

Tom Mitchell provides a more modern definition: "A computer program is said to learn from experience E with respect to some class of tasks T and performance measure P, if its performance at tasks in T, as measured by P, improves with experience E."

##### Example: playing checkers.
- E = the experience of playing many games of checkers
（训练经验）

- T = the task of playing checkers.
（任务）

- P = the probability that the program will win the next game.（预测正确的概率）

> In general, any machine learning problem can be assigned to one of two broad classifications:
Supervised learning and Unsupervised learning.

#### Supervised Learning

In supervised learning, we are given a data set and already know what our correct output should look like, having the idea that there is a relationship between the input and the output.

Supervised learning problems are categorized into "regression" and "classification" problems. In a regression problem, we are trying to predict results within a continuous output, meaning that we are trying to map input variables to some continuous function. In a classification problem, we are instead trying to predict results in a discrete output. In other words, we are trying to map input variables into discrete categories.

##### Example 1:

- Given data about the size of houses on the real estate market, try to predict their price. Price as a function of size is a continuous output, so this is a regression problem.

- We could turn this example into a classification problem by instead making our output about whether the house "sells for more or less than the asking price." Here we are classifying the houses based on price into two discrete categories.

##### Example 2:

- (a) Regression - Given a picture of a person, we have to predict their age on the basis of the given picture
- (b) Classification - Given a patient with a tumor, we have to predict whether the tumor is malignant or benign.


#### Unsupervised Learning
Unsupervised learning allows us to approach problems with little or no idea what our results should look like. We can derive structure from data where we don't necessarily know the effect of the variables.
We can derive this structure by clustering the data based on relationships among the variables in the data.
With unsupervised learning there is no feedback based on the prediction results.

##### Example:

- Clustering: Take a collection of 1,000,000 different genes, and find a way to automatically group these genes into groups that are somehow similar or related by different variables, such as lifespan, location, roles, and so on.

- Non-clustering: The "Cocktail Party Algorithm", allows you to find structure in a chaotic environment. (i.e. identifying individual voices and music from a mesh of sounds at a cocktail party).

#### The difference between the two
> F(x)->y,x(A),y(b),

##### 我们不难看到，回归问题与分类问题本质上都是要建立映射关系：
1. 而两者的区别则在于：对于回归问题，其输出空间B是一个度量空间，即所谓“定量”。也就是说，回归问题的输出空间定义了一个度量  去衡量输出值与真实值之间的“误差大小”。例如：预测一瓶700毫升的可乐的价格（真实价格为5元）为6元时，误差为1；预测其为7元时，误差为2。这两个预测结果是不一样的，是有度量定义来衡量这种“不一样”的。（于是有了均方误差这类误差函数）。
2. 对于分类问题，其输出空间B不是度量空间，即所谓“定性”。也就是说，在分类问题中，只有分类“正确”与“错误”之分，至于错误时是将Class 5分到Class 6,还是Class 7，并没有区别，都是在error counter上+1。而非很多回答所提到的“连续即回归，离散即分类”。事实上，在实际操作中，我们确实常常将回归问题和分类问题互相转化（分类问题回归化：逻辑回归；回归问题分类化：年龄预测问题——>年龄段分类问题），但这都是为了处理实际问题时的方便之举，背后损失的是数学上的严谨性。
 ##### REVIEW
 ###### Question 1
 A computer program is said to learn from experience E with respect to some task T and some performance measure P if its performance on T, as measured by P, improves with experience E. Suppose we feed a learning algorithm a lot of historical weather data, and have it learn to predict weather. In this setting, what is E?
 
 Answer The process of the algorithm examining a large amount of historical weather data.
 
 > 分析：
 T := The weather prediction task.
 P := The probability of it correctly predicting a future date's weather.
 E := The process of the algorithm examining a large amount of historical weather data.
 
 ###### Question 2
 Suppose you are working on weather prediction, and you would like to predict whether or not it will be raining at 5pm tomorrow. You want to use a learning algorithm for this. Would you treat this as a classification or a regression problem?
 
 Answer Classification
 
 > 分析：
 当我们试图预测少量离散值输出之一时，分类是合适的，比如是否会下雨（我们可能指定为0级），或者不会（例如1级）。
 
 ###### Question 3
 Suppose you are working on stock market prediction, and you would like to predict the price of a particular stock tomorrow (measured in dollars). You want to use a learning algorithm for this. Would you treat this as a classification or a regression problem?
 
 Answer Regression
 
 > 分析：
 当我们试图预测连续价值的产出时，回归是合适的，因为作为一种股票的价格（类似于讲座中的房价例子）。
 
 ###### Question 4
 Some of the problems below are best addressed using a supervised learning algorithm, and the others with an unsupervised learning algorithm. Which of the following would you apply supervised learning to? (Select all that apply.) In each case, assume some appropriate dataset is available for your algorithm to learn from.
 
 > 分析：
 Take a collection of 1000 essays written on the US Economy, and find a way to automatically group these essays into a small number of groups of essays that are somehow "similar" or "related".
 这是一个无监督的学习/聚类问题（类似于讲座中的Google新闻示例）
 
 > Given a large dataset of medical records from patients suffering from heart disease, try to learn whether there might be different clusters of such patients for which we might tailor separate treatements.
 这可以通过使用无监督学习，聚类算法来解决，我们将患者分组到不同的群中。
 
 > Given genetic (DNA) data from a person, predict the odds of him/her developing diabetes over the next 10 years.
 这可以作为监督学习，分类问题来解决，我们可以从包含不同人的遗传数据的标记数据集中学习，并告诉我们他们是否患有糖尿病。
 
 > Given 50 articles written by male authors, and 50 articles written by female authors, learn to predict the gender of a new manuscript's author (when the identity of this author is unknown).
 这可以作为监督学习，分类问题来解决，我们从标记数据中学习以预测性别。
 
 > In farming, given data on crop yields over the last 50 years, learn to predict next year's crop yields.
 这可以解决为一个监督学习问题，我们从历史数据中学习（用历史作物产量标记）以预测未来作物产量。
 
 > Examine a large collection of emails that are known to be spam email, to discover if there are sub-types of spam mail.
 这可以使用聚类（无监督学习）算法来解决，以将垃圾邮件聚类为子类型。
 
 > Examine a web page, and classify whether the content on the web page should be considered "child friendly" (e.g., non-pornographic, etc.) or "adult."
 这可以作为监督学习，分类问题来解决，我们可以从已被标记为“儿童友好”或“成人”的网页数据集中学习。
 
 > Examine the statistics of two football teams, and predicting which team will win tomorrow's match (given historical data of teams' wins/losses to learn from).
 这可以通过监督式学习来解决，我们从历史记录中学习如何进行赢/输预测。
 
 ###### Question 5
 Which of these is a reasonable definition of machine learning?
 
 Answer: Machine learning is the field of study that gives computers the ability to learn without being explicitly programmed.
