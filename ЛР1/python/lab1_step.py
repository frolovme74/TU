# Один шаг h = 0,1 методами Эйлера, модифицированным Эйлера и Рунге-Кутты
# для системы (3) варианта 10: y = 1, начальные условия [0  0]
import os

import matplotlib.pyplot as plt
import numpy as np

os.chdir(os.path.dirname(os.path.abspath(__file__)))

a0, a1, a2, b0 = 25, 1, 1, 25
h = 0.1
X0 = np.array([0.0, 0.0])


def f(X):
    return np.array([X[1], (b0 * 1 - a0 * X[0] - a1 * X[1]) / a2])


# Эйлер
X_e = X0 + h * f(X0)

# модифицированный Эйлер (наклон в середине шага)
X_mid = X0 + h / 2 * f(X0)
X_me = X0 + h * f(X_mid)

# Рунге-Кутта 4-го порядка
k1 = f(X0)
k2 = f(X0 + h / 2 * k1)
k3 = f(X0 + h / 2 * k2)
k4 = f(X0 + h * k3)
X_rk = X0 + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)

# точное решение: x2(t) = w(t) - импульсная (весовая) функция
wd = np.sqrt(a0 / a2 - (a1 / (2 * a2)) ** 2)
t = np.linspace(0, 0.1, 200)
x2_exact = b0 / (a2 * wd) * np.exp(-a1 / (2 * a2) * t) * np.sin(wd * t)
x2_exact_h = b0 / (a2 * wd) * np.exp(-a1 / (2 * a2) * h) * np.sin(wd * h)

print('f(X0) =', f(X0))
print('Эйлер:', X_e)
print('середина шага:', X_mid, ' наклон в ней:', f(X_mid))
print('модиф. Эйлер:', X_me)
print('k1..k4:', k1, k2, k3, k4)
print('Рунге-Кутта:', X_rk)
print('точно x2(0,1) =', round(x2_exact_h, 4))

plt.figure(figsize=(9, 5.5))
plt.plot(t, x2_exact, 'k-', linewidth=2, label='точное решение x2(t)')
plt.plot([0, h], [X0[1], X_e[1]], 'r--', linewidth=2,
         label=f'метод Эйлера (наклон в начале шага {f(X0)[1]:g})')
plt.plot([0, h / 2], [X0[1], X_mid[1]], 'g:', linewidth=2, label='полшага по Эйлеру до середины')
plt.plot([0, h], [X0[1], X_me[1]], 'g--', linewidth=2,
         label=f'модиф. метод Эйлера (наклон в середине {f(X_mid)[1]:g})')
plt.plot(0, X0[1], 'ko')
plt.plot(h / 2, X_mid[1], 'go', mfc='none')
plt.plot(h, X_e[1], 'rs')
plt.plot(h, X_me[1], 'gs')
plt.plot(h, X_rk[1], 'b^', markersize=9, label='метод Рунге-Кутты 4-го порядка')
arrow = dict(arrowstyle='-', lw=0.8)
plt.annotate(f'Эйлер: {X_e[1]:.4g}', (h, X_e[1]), xytext=(0.108, 2.55), color='r', arrowprops=arrow)
plt.annotate(f'модиф. Эйлер: {X_me[1]:.4g}', (h, X_me[1]), xytext=(0.108, 2.36), color='g', arrowprops=arrow)
plt.annotate(f'Рунге-Кутта: {X_rk[1]:.4f}\nточно: {x2_exact_h:.4f}', (h, X_rk[1]), xytext=(0.108, 2.02),
             color='b', arrowprops=arrow)
plt.xlim(-0.005, 0.15)
plt.grid(True)
plt.xlabel('t, c')
plt.ylabel('x2(t)')
plt.title('Один шаг h = 0,1 для системы (3): y = 1, начальные условия [0  0]')
plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.12), ncol=2)
plt.savefig('ris_step.png', dpi=200, bbox_inches='tight')
plt.show()
