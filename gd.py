import matplotlib.pyplot as plt
y_values = [1, 3, 5 , 3, 7, 6, 8, 4, 6, 7, 9]
x_values = [x for x in range(len(y_values))]
plt.scatter(x_values, y_values)

m = 0
b = 0
alpha = 0.01
y = lambda x: m*x + b

def costFunction(x_values, y_values, y):
    total1 = 0
    total2 = 0
    count = 0
    while count < len(y_values):
        total1 += (y(x_values[count]) - y_values[count])
        total2 += (y(x_values[count]) - y_values[count]) * x_values[count]
        count+=1
    return (total1/len(y_values)), (total2/len(y_values))

count = 0
while count < 100:
    intercept, slope = costFunction(x_values, y_values, y)
    m = m - slope * alpha
    b = b - intercept * alpha
    count += 1

solution = []
for i in x_values:
    solution.append(y(i))

plt.scatter(x_values, y_values)
plt.plot(x_values, solution)
plt.show()
