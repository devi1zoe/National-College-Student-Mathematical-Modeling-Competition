import pandas as pd
df = pd.read_excel('每天销售总量.xlsx')

def merge_cells(df):
    for i in range(len(df.columns)):
        for j in range(len(df)):
            if pd.isnull(df.iloc[j, i]):
                df.iloc[j, i] = df.iloc[j-1, i] if j > 0 else ''
merge_cells(df)
df = df.ffill()  # 填充缺失值为前面非空值

df_pivot = pd.pivot_table(df, values='销量(千克)', index='销售日期', columns='分类名称')

writer = pd.ExcelWriter('out_data.xlsx')
df_pivot.to_excel(writer, sheet_name='Sheet1')
writer.save()
