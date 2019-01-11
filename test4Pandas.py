import pandas as pd
import numpy as np
d=np.array(['b','b','c'])
s=pd.Series(d)
d1=[['safvan',18],['merin',20],['arun',21]]
df=pd.DataFrame(d1,columns=['Aame','Age'])
d2={'Name':['Safvan','Merin','Arun'],'Age':[18,20,21]}
df1=pd.DataFrame(d2)

print(s)
print(df)
print(df1)