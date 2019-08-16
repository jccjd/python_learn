class Car(object):
    def __init__(self, name=None, loss=None):
        self.name = name
        self.loss = loss

    def getName(self):
        return self.name

    def getPrice(self):
        loss  = self.loss
        return loss[0]

    def getLoss(self):
        loss = self.loss
        return loss[1] * loss[2]

def battle(car1, car2):
    if car1.getPrice() > car2.getPrice():
        batter_price = car1
    else:
        batter_price = car2

    if car1.getLoss() > car2.getLoss():
        batter_loss = car1
    else:
        batter_loss = car2
    print(f'{batter_price.getName()}的价格更便宜,{batter_loss.getName()}的损失值比较低')


Bmw = Car('宝马', [60,9,500])
Benz = Car('奔驰', [80,7,600])

