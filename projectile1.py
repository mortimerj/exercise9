# import math
#
# theta = 80 * (math.pi / 180)
# print(theta)
#
# a = 2
# b = 44
# a *(b math.cos(theta))
import math

g = 9.81
v0 = 44
theta = 80 * (math.pi / 180)
x = 0.5
y0 = 1

y = y0 + (x * (math.tan(theta)) - (g*x**2)/(2*(v0 * math.cos(theta)**2)))
print(y)

