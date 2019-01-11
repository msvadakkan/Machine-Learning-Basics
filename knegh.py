from  sklearn import datasets
import pandas as pd
iris=datasets.load_iris()
x=iris.data
y=iris.target
columns=iris.target_names
print(x)
print(y)
print(columns)