import pandas as pd
import numpy as np

# 从Excel文件读取数据（在Sheet2中）
correlation_matrix = pd.read_excel('2.xlsx', sheet_name='Sheet2', index_col=0)

# 将对角线置为NaN
np.fill_diagonal(correlation_matrix.values, np.nan)

# 找到前十个最接近+1的值及其行列标签
top_10_values_1 = []
top_10_labels_1 = []

# 找到前十个最接近-1的值及其行列标签
top_10_values_minus_1 = []
top_10_labels_minus_1 = []

processed_indices = set()  # 用于存储已处理过的行列索引

for _ in range(10):
    max_value = np.nanmax(correlation_matrix.values)  # 找到矩阵中的最大值（不包括对角线和NaN）
    min_value = np.nanmin(correlation_matrix.values)  # 找到矩阵中的最小值（不包括对角线和NaN）

    if abs(max_value - 1) < abs(min_value + 1):
        row_label, col_label = np.unravel_index(np.nanargmax(correlation_matrix.values), correlation_matrix.shape)
        value = max_value
        top_10_values_1.append(value)
        top_10_labels_1.append((correlation_matrix.index[row_label], correlation_matrix.columns[col_label]))
    else:
        row_label, col_label = np.unravel_index(np.nanargmin(correlation_matrix.values), correlation_matrix.shape)
        value = min_value
        top_10_values_minus_1.append(value)
        top_10_labels_minus_1.append((correlation_matrix.index[row_label], correlation_matrix.columns[col_label]))

    # 如果已经处理过（i，j）或（j，i），则跳过
    if (row_label, col_label) in processed_indices or (col_label, row_label) in processed_indices:
        correlation_matrix.iloc[row_label, col_label] = np.nan
        continue

    processed_indices.add((row_label, col_label))
    correlation_matrix.iloc[row_label, col_label] = np.nan  # 将找到的值置为NaN

# 输出结果
print("前十个最接近+1的值及其行列标签（不包括1）：")
for i in range(10):
    value = top_10_values_1[i]
    label = top_10_labels_1[i]
    print("值：{}，行列标签：{}".format(value, label))

print("前十个最接近-1的值及其行列标签（不包括-1）：")
for i in range(10):
    value = top_10_values_minus_1[i]
    label = top_10_labels_minus_1[i]
    print("值：{}，行列标签：{}".format(value, label))