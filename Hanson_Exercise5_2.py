# import libraries
import numpy as np
import pandas as pd
import math

# define f(x) for second part of exercise
f = lambda x: math.sqrt(4 - x**2)

# define python function that takes in matematical function f, a and b, and n
def r_riemann(a,b,n,f):
    del_x = (b-a)/n
    values = [f(a + k * del_x) * del_x for k in range(1, n + 1)]
    df = pd.Series(values)
    return df.sum()

# (b) assign values
a = 0
b = 2
n = 4

print(r_riemann(a,b,n,f))
# (b) Answer: R4 = 2.4957090681024408

# (c) area under the curve
n2 = 50
n3 = 100
n4 = 1000
n5 = 1000000

print(r_riemann(a,b,n2,f))
print(r_riemann(a,b,n3,f))
print(r_riemann(a,b,n4,f))
print(r_riemann(a,b,n5,f))

# (c) values: 3.0982685110984995, 3.120417031779045, 3.1395554669110277, 3.1415906524138117
# (c) Answer: It's pi!! Looking at the graph, I see now that we're finding the area of 1/4
# of a circle with a radius of 2. 
