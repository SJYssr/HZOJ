
import math

a, b, t = map(float, input().split())
c = math.sqrt(a**2 + b**2 - 2 * a * b * math.cos(math.radians(t)))
print("%.6lf" % c)

