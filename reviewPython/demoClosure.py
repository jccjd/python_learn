def addx(x):
    def adder(y): return x + y
    return adder
c = addx(1)
print(c(10))