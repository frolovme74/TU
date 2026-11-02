function dx = lab1_ode(t, x, a, b, inp)
% Правая часть системы в форме Коши
% a   - коэффициенты [a0 a1 a2 a3] (для n=2: [a0 a1 a2])
% b   - коэффициент входа b0
% inp - 'step' (y = 1) или 'sin' (y = sin(t))
if strcmp(inp, 'sin')
    y = sin(t);
else
    y = 1;
end
n = numel(a) - 1;            % порядок системы
dx = zeros(n, 1);            % обнуление массива dx
dx(1:n-1) = x(2:n);          % x1' = x2
dx(n) = (b*y - a(1:n)*x) / a(n+1);   % x2' = (b*y - a0*x1 - a1*x2)/a2
end
