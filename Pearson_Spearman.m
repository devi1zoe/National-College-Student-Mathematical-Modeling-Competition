clc;clear
% Pearson相关系数：必须满足连续数据+正态分布+线性关系，否则用Spearman
data = readmatrix('.\data.xlsx', 'Sheet', 1, 'Range', 'A2: F1086'); 
title = readcell('.\data.xlsx', 'Sheet', 1, 'Range', 'A1:F1');
%% 做散点图判断是否存在线性关系
[n, m] = size(data);  % 获取矩阵的行数和列数
figure;               % 创建一个新的图形窗口
k = 1;
for i = 1:m
    for j = 1:m
        subplot(m, m, k)  % 在子图中显示每对列的散点图
        scatter(data(:, i), data(:, j))
        xlabel([title(i)])  % x轴标签为第i列
        ylabel([title(j)])  % y轴标签为第j列
        k = k + 1;
    end
end
%% 正态分布检验
disp("偏度和峰度")
skewness(data(:,1))  %偏度
kurtosis(data(:,1))  %峰度
% 用循环检验所有列的数据
n_c = size(data,2);  
H = zeros(1,n_c);  
P = zeros(1,n_c);
for i = 1:n_c
    [h,p] = jbtest(data(:,i),0.05);
    H(i)=h;
    P(i)=p;
end
disp(H)
disp(P)
disp("h为1表示不是正态分布")
