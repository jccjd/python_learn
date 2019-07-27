import numpy as np
import csv
def readData():
    x = []
    y = []
    with open('Housing.csv') as f:
        rdr = csv.reader(f)
        next(rdr)
        for line in rdr:
            xline = [1.0]
            for s in line[:-1]:
                xline.append(float(s))
            x.append(xline)
            y.append(float(line[-1]))
    return (x,y)
x0, y0 = readData()
d = len(x0) - 10
X = np.array(x0[:d])
y = np.transpose(np.array([y0[:d]]))

Xt = np.transpose(X)
XtX = np.dot(Xt, X)
Xty = np.dot(Xt,y)
beta = np.linalg.solve(XtX,Xty)
print(np.shape(beta))
for data, actual in zip(x0[d:],y0[d:]):
    x = np.array([data])
    prediction = np.dot(x, beta)
    print('prediction = ' + str(prediction[0,0]) + ' actual = ' + str(actual))

