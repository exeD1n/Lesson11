from sympy import *
import numpy as np
import matplotlib.pyplot as plt
from math import *

def uprostil():
    x = Symbol('x')
    y = -12*x**4-18*x**3+5*x**2+10*x-30
    yprime = y.diff(x)
    z = yprime.diff(x)
    print(yprime, "Первая производная")
    print(z, "Вторая производная")

    
def reshil():
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('zero')
    
    # Eliminate upper and right axes
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    
    # Show ticks in the left and lower axes only
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    
    
    def fx(x):
        # return -48*x**3 - 54*x**2 + 10*x + 10
        return -144*x**2 - 108*x + 10

    x = np.linspace(-6, 6, 30)
    y = [fx(n) for n in x]
    
    plt.fill_between(x, y, where=(x <= -1), color='g')
    plt.fill_between(x, y, where=(x >= -1), color='r')
    
    plt.plot(x, y, marker='o') #Отображаем корни

    min_y = min(x)
    min_x_index = np.argmin(y)
    min_x = x[min_x_index]
    plt.plot(min_x, min_y, marker='o')
    
    fminx = min(x)
    fminy = min(y)
    fmaxx = max(x)
    fmaxy = max(y)
    print(f'f<0 = [{fminx}, {fminy}]\nf<0 = [{fmaxx}, {fmaxy}]')
    
    plt.show()
    

if __name__ == "__main__":
    uprostil()
    reshil()
    
    