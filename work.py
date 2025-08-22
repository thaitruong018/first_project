import pandas as pd

df = pd.read_csv(r"C:\Users\admin\git_file\revenue_data.csv")

df.head()

df.describe()

df['Revenue'].mean()