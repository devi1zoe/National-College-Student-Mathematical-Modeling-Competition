import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'SimSun'

data = pd.read_excel('每季度销售总量.xlsx')
months = data['销售季度'].fillna(method='ffill').unique()  # 填充年份的缺失值
categories = data['分类名称'].unique() # 提取分类名称列
category_data = {}  # 创建一个空字典来存储每个分类的销量数据
for category in categories:
    category_data[category] = []
for category in categories: # 提取每个分类的销量数据
    category_sales = data[data['分类名称'] == category]['销量(千克)'].tolist()
    category_data[category] = category_sales
plt.figure(figsize=(10, 7)) # 绘制折线图
for category in categories:
    plt.plot(months, category_data[category], marker='o', label=category)
plt.xlabel('销售季度')
plt.xticks(rotation=45)  # 设置横坐标标签斜向显示
plt.ylabel('销量量(千克)')
plt.legend()
plt.grid(True)
plt.show()





data = pd.read_excel('每月销售总量.xlsx')
months = data['销售月份'].fillna(method='ffill').unique()  # 填充年份的缺失值
categories = data['分类名称'].unique() # 提取分类名称列
category_data = {}  # 创建一个空字典来存储每个分类的销量数据
for category in categories:
    category_data[category] = []
for category in categories: # 提取每个分类的销量数据
    category_sales = data[data['分类名称'] == category]['销量(千克)'].tolist()
    category_data[category] = category_sales
plt.figure(figsize=(10, 7)) # 绘制折线图
for category in categories:
    plt.plot(months, category_data[category], marker='o', label=category)
plt.xlabel('销售月份')
plt.xticks(rotation=45)  # 设置横坐标标签斜向显示
plt.ylabel('销量量(千克)')
plt.legend()
plt.grid(True)
plt.show()
