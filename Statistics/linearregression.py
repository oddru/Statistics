import statistics as st
import math
#hello
#Linear Regression Statistics

#Column X

x_list = []
num_valueX = int(input("Enter the amount of X values: "))

for i in range(0, num_valueX):
    user_inputX = int(input("Enter Number {0}: ".format(i+1)))
    x_list.append(user_inputX)
   
#Column Y

y_list = []
num_valueY = int(input("Enter the amount of Y values: "))

for i in range(0, num_valueY):
    user_inputY = int(input("Enter Number {0}: ".format(i+1)))
    y_list.append(user_inputY)

print(f"X: {x_list}\nY: {y_list}")

#XY Table
xy = [x * y for x, y in zip(x_list, y_list)]
print(f"XY: {xy}")

#X Squared Table
x_sqr = [math.pow(x, 2) for x in x_list]
print(f"X ** 2: {x_sqr}")

#Y Squared Table
y_sqr = [math.pow(y, 2) for y in y_list]
print(f"Y ** 2: {y_sqr}")

#Sum of All 

sum_x = sum(x_list)
sum_y = sum(y_list)
sum_xy = sum(xy)
sum_xsqrd = sum(x_sqr)
sum_ysqrd = sum(y_sqr)

print(f"Sum Of X: {sum_x}\nSum of Y: {sum_y}\nSum of XY: {sum_xy}\nSum of X Squared: {sum_xsqrd}\nSum of Y Squared: {sum_ysqrd}")

#Formulas

n = len(x_list)

#SSxy = (sum_xy - (sum_x * sum_y) / n)
SSxy = sum_xy - (sum_x * sum_y) / n

#SSxx = (sum_xsqrd - (sum_x * sum_x) / n)
SSxx = sum_xsqrd - (sum_x * sum_x) / n

#Slope (b)
b = SSxy / SSxx

#Intercept (a)
a = st.mean(y_list) - b * st.mean(x_list)

print(f"y = {a} + {b}x")
