import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'SimSun'
data = pd.read_excel('处理后的每天数据.xlsx')

sales_date = data['销售日期']
water_stem = data['水生根茎类']
leafy_vegetable = data['花叶类']
cauliflower = data['花菜类']
eggplant = data['茄类']
pepper = data['辣椒类']
edible_fungus = data['食用菌']

fig, ax = plt.subplots(figsize=(12, 6))  # 设置图形的大小为12x6

ax.plot(sales_date, water_stem, label='水生根茎类') # 绘制折线图
ax.plot(sales_date, leafy_vegetable, label='花叶类')
ax.plot(sales_date, cauliflower, label='花菜类')
ax.plot(sales_date, eggplant, label='茄类')
ax.plot(sales_date, pepper, label='辣椒类')
ax.plot(sales_date, edible_fungus, label='食用菌')

ax.grid(True)
ax.legend()
ax.set_xlabel('销售日期')
ax.set_ylabel('销量量(千克)')
fig.autofmt_xdate()

plt.show()