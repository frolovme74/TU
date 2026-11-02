% Лабораторная работа №1, вариант 10
% a2*x'' + a1*x' + a0*x = b0*y,  a0 = 25, a1 = 1, a2 = 1, b0 = 25
clc; clear; close all;

a  = [25 1 1];               % [a0 a1 a2]
b  = 25;                     % b0
x0 = [1 0];                  % ненулевые НУ по таблице 2: x(0) = 1, x'(0) = 0
n  = numel(a) - 1;
tspan = [0 10];

cases = { zeros(1,n), 'step', 'нулевые НУ, y = 1(t)';
          zeros(1,n), 'sin',  'нулевые НУ, y = sin(t)';
          x0,         'step', 'НУ x(0) = 1, x''(0) = 0, y = 1(t)';
          x0,         'sin',  'НУ x(0) = 1, x''(0) = 0, y = sin(t)' };

for k = 1:4
    [t, x] = ode45(@(t,x) lab1_ode(t, x, a, b, cases{k,2}), tspan, cases{k,1});
    if strcmp(cases{k,2}, 'sin')
        y = sin(t);
    else
        y = ones(size(t));
    end
    figure(k);
    plot(t, x(:,1), 'b-', t, x(:,2), 'g-', t, y, 'k--', 'LineWidth', 1.5);
    grid on;
    legend('x_1(t)', 'x_2(t)', 'y(t)', 'Location', 'best');
    xlabel('t, c'); ylabel('x_i(t), y(t)');
    title(sprintf('Вариант 10: %s', cases{k,3}));
    saveas(gcf, sprintf('case%d.png', k));
end

% --- проверка через передаточную функцию ---
W = tf(b, fliplr(a))         % W(s) = 25 / (s^2 + s + 25)
p = roots(fliplr(a))         % корни характеристического уравнения
h_inf = b / a(1)             % установившееся значение h(t)

[t, x] = ode45(@(t,x) lab1_ode(t, x, a, b, 'step'), tspan, zeros(1,n));
figure(5);
subplot(2,1,1);
step(W, tspan(2)); hold on; plot(t, x(:,1), 'r--'); hold off; grid on;
legend('step(W)', 'x_1(t) из ode45'); title('Переходная характеристика h(t)');
subplot(2,1,2);
impulse(W, tspan(2)); hold on; plot(t, x(:,2), 'r--'); hold off; grid on;
legend('impulse(W)', 'x_2(t) из ode45'); title('Импульсная характеристика w(t)');
saveas(gcf, 'check.png');
