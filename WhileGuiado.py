
"""
autor: Alejandra Jiménez Soto
date: 10/20/2022

"""

x=2
y=0
delta = 1
while(y**2)<x:
    print("Start with:",y)
    y = y + delta
    if (y**2)>x:
        y = y-delta
        delta = delta/10
print(y)
