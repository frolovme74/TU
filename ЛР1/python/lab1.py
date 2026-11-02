# Лабораторная работа №1, вариант 10
# Решение уравнения  a2*x'' + a1*x' + a0*x = b0*y
import os

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp

os.chdir(os.path.dirname(os.path.abspath(__file__)))  # графики сохраняются рядом со скриптом

# ---------- коэффициенты уравнения (таблица 1) ----------
a0 = 25
a1 = 1
a2 = 1
b0 = 25

# ---------- начальные условия (таблица 2) ----------
# порядок чисел в списке: x(0), x'(0)
x0_zero = [0, 0]        # нулевые начальные условия
x0_var = [1, 0]         # начальные условия по варианту

# ---------- входные сигналы ----------
def step(t):
    return 1 + 0 * t    # y = 1(t), единичный ступенчатый сигнал

def sinus(t):
    return np.sin(t)    # y = sin(t)

# ---------- правые части системы уравнений ----------
# x[0] - это x1 = x,   x[1] - это x2 = x'
def ode(t, x, y):
    dx = np.zeros(2)
    dx[0] = x[1]
    dx[1] = (b0 * y(t) - a0 * x[0] - a1 * x[1]) / a2
    return dx

# ---------- один опыт: решить систему и построить график ----------
def experiment(y, x0, y_name, title, file_name):
    t_end = 15                                  # время наблюдения, с
    t_points = np.linspace(0, t_end, 1501)      # моменты времени для графика
    sol = solve_ivp(ode, [0, t_end], x0, method='RK45', args=(y,),
                    t_eval=t_points, rtol=1e-6, atol=1e-9)

    t = sol.t
    x1 = sol.y[0]
    x2 = sol.y[1]

    plt.figure(figsize=(10, 6))
    plt.plot(t, x1, 'b-', linewidth=2, label='x1(t) = x(t)')
    plt.plot(t, x2, 'g--', linewidth=2, label="x2(t) = x'(t)")
    plt.plot(t, y(t), 'r:', linewidth=2, label=y_name)
    plt.grid(True)
    plt.xlabel('t, c')
    plt.ylabel('x1(t), x2(t), y(t)')
    plt.title(title)
    plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.12), ncol=3)
    plt.savefig(file_name, dpi=200, bbox_inches='tight')

# ---------- четыре опыта ----------
experiment(step, x0_zero, 'y(t) = 1(t)',
           'y = 1(t), начальные условия [0  0]', 'ris1.png')
experiment(sinus, x0_zero, 'y(t) = sin(t)',
           'y = sin(t), начальные условия [0  0]', 'ris2.png')
experiment(step, x0_var, 'y(t) = 1(t)',
           'y = 1(t), начальные условия [1  0]', 'ris3.png')
experiment(sinus, x0_var, 'y(t) = sin(t)',
           'y = sin(t), начальные условия [1  0]', 'ris4.png')

plt.show()
