import pandas as pd
data = pd.read_excel('./out_data.xlsx', sheet_name='Sheet1', header=None, usecols='B:G', skiprows=1)

# 统计描述
MIN = data.min()  # 每一列的最小值
MAX = data.max()  # 每一列的最大值
MEAN = data.mean()  # 每一列的均值
MEDIAN = data.median()  # 每一列的中位数
SKEWNESS = data.skew()  # 每一列的偏度
KURTOSIS = data.kurtosis()  # 每一列的峰度
STD = data.std()  # 每一列的标准差

RESULT1 = pd.DataFrame([MIN, MAX, MEAN, MEDIAN, SKEWNESS, KURTOSIS, STD])
RESULT1.to_excel('./static_des.xlsx', sheet_name='Sheet1', index=False)