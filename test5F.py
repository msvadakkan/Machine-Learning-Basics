import pandas as pd
d=pd.read_csv('people.csv')
d=d.dropna()
# x=d.iloc[:].values
# y=d.iloc[:,-1].values

print(d.shape)