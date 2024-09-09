clear;clc        
data = xlsread('data.xlsx');

% Pearson相关系数计算部分
R_Pearson = corrcoef(data);

% Spearman相关系数计算_p值>0.05则相关性不显著
R_Spearman = corr(data, 'type', 'Spearman');

xlswrite('.\1.xlsx', R_Spearman);
xlswrite('.\2.xlsx', R_Pearson);
%%  Kolmogorov-Smirnov 检验
% 检验原假设，具有相同分布的总体的原假设。
% 返回值 h = 0 表明 kstest2 在默认的 5% 显著性水平上未拒绝原假设。
[n, m] = size(data);  % 获取矩阵的行数和列数
for i = 1:m
    for j = 1:m
        [h, p, ksstat] = kstest2(data(:, i), data(:, j))
        % 显示 KS 统计量和 p 值
        fprintf('KS统计量: %f\n', ksstat);
        fprintf('p值: %f\n', p);
        % 判断是否拒绝原假设（即两个样本来自同一分布）
        if h == 1
        fprintf('拒绝原假设，两个样本不来自同一分布.\n');
        else
        fprintf('接受原假设，两个样本来自同一分布.\n');
        end
    end
end


%%
% 初始化 01 矩阵和 p 值矩阵
[n, m] = size(data);
matrix = zeros(m, m);
p_values = zeros(m, m); % 使用 p_values 作为 p 值的矩阵
ks_stats = zeros(m, m); % 使用 ks_stats 存储 KS 统计量

% 进行 KS 检验并更新矩阵和 p 值矩阵、ks统计量矩阵
for i = 1:m
    for j = 1:m
        [h, p, ksstat] = kstest2(data(:, i), data(:, j));
        matrix(i, j) = h;
        p_values(i, j) = p; % 将 p 值存储在 p_values 矩阵中
        ks_stats(i, j) = ksstat; % 将 KS 统计量存储在 ks_stats 矩阵中
    end
end

% 显示 01 矩阵、p 值矩阵和 KS 统计量矩阵
disp(matrix);
disp(p_values);
disp(ks_stats);
