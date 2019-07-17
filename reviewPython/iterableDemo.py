class myrange:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

iters = myrange()
iters = iter(iters)

list = [1,2,3,4]
iters = iter(list)
while True:
    try:
        print(next(iters))
    except StopIteration:
        break
