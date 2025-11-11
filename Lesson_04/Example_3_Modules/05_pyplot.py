from matplotlib import pyplot as plt

xs = list(range(10))
ys = []
for x in xs:
    ys.append(x*x)

plt.plot(xs, ys)
plt.show()