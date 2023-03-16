import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from matplotlib.ticker import FormatStrFormatter

y0 = [3.14, 4.71] # [species 1 (x1), species 2 (x2)] units in hundreds

t = np.linspace(0, 50, num=40)  # unitless time (maybe weeks or months?)

# params
r1 = 1
r2 = 1
a1 = 0.53
a2 = 0.54
k1 = 3.5
k2 = 5.33

x1_s = (k1 - a1 * k2) / (1 - a2 * a1)
x2_s = (k2 - a2 * k1) / (1 - a1 * a2)

y0 = [3.14, 4.71]  # [species 1 (x1), species 2 (x2)] units in hundreds

params = [r1, r2, a1, a2, k1, k2]


def sim(variables, t, params):
    # species1 population level
    x1 = variables[0]
    # species2 population level
    x2 = variables[1]
    r1 = params[0]
    r2 = params[1]
    a1 = params[2]
    a2 = params[3]
    k1 = params[4]
    k2 = params[5]

    dx1dt = r1 * x1 * (1 - ((x1 + a2 * x2)/k1))
    dx2dt = r2 * x2 * (1 - ((x2 + a1 * x1)/k2))

    return ([dx1dt, dx2dt])

y = odeint(sim, y0, t, args=(params,))

 

#print(y)

f, (ax1, ax2) = plt.subplots(2)
ax1.yaxis.set_major_formatter(FormatStrFormatter('%.1f'))
line1, = ax1.plot(t, y[:, 0], color="b")
line2, = ax2.plot(t, y[:, 1], color="r")
ax1.set_ylabel("Population density of V. germanica")
ax1.set_xlabel("Time")

ax2.set_ylabel("Population density of V. vulgaris")
ax2.set_xlabel("Time")

plt.show()