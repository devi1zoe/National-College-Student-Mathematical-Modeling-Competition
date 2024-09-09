import pandas as pd
df = pd.read_excel('data.xlsx')

df['销售日期'] = pd.to_datetime(df['销售日期'])
daily_sales = df.groupby(['销售日期', '分类名称']).sum()
df['销售月份'] = df['销售日期'].dt.to_period('M')
monthly_sales = df.groupby(['销售月份', '分类名称']).sum()
df['销售季度'] = df['销售日期'].dt.to_period('Q')
session_sales = df.groupby(['销售季度', '分类名称']).sum()

daily_sales.to_excel('每天销售总量.xlsx')
monthly_sales.to_excel('每月销售总量.xlsx')
session_sales.to_excel('每季度销售总量.xlsx')


