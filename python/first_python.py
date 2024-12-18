import pandas as pd
from pandas import DataFrame
majors = ['CS','CSE','EE','Physics','Chemistry']
students = [15, 15, 35, 3, 2]
enrolled = list(zip(majors, students))
df = DataFrame(enrolled, columns=['major', 'count'])
df['new_column'] = 10  # 新增一個常數列

print(df)
grouped = df.groupby('major').sum()  # 依據 'major' 分組並計算總和
print("grouped: ",grouped)
# df.to_csv('enrollment.csv', index=False)  # 將資料寫入 CSV
# df = pd.read_csv('enrollment.csv')        # 從 CSV 讀取資料
# print(df.head())          # 顯示前五行
# print(df.describe())      # 顯示數據的描述統計資訊

