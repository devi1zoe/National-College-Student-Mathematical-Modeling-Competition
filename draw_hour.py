import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'SimSun'
data = pd.read_excel('处理后的每小时数据.xlsx')

time = data['小时'] # 提取时间和不同类别的数据
categories = ['花菜类', '花叶类', '辣椒类', '茄类', '食用菌', '水生根茎类']
values = [data[category] for category in categories]

fig = plt.figure()

ax = fig.add_subplot(1, 1, 1)
for i, category in enumerate(categories):
    ax.plot(time, values[i], label=category)
ax.legend()
ax.set_xlabel('小时')
ax.set_ylabel('销量量(千克)')

plt.show()