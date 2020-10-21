a = 4.5
b = 5.9
c = 9
p = (a + b + c) / 2
s = float((p*(p-a)*(p-b)*(p-c))**(1/2))
print("%.2f" % s)
