from sklearn import svm
x = [[3,3],[4,3],[1,1]]
y = [1,1,-1]
model = svm.SVC(kernel='linear')
model.fit(x,y)
#打印支持向量
print(model.support_vectors_)
#第2和第0个点是支持向量
print(model.support_)
#有几个支持向量
print(model.n_support_)
model.predict([[4,3]])
print(model.coef_)

print(model.intercept_)
