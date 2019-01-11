#sk_learn
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

d=[[1],[2],[3],[4]]
f=[[2],[4],[6],[8]]
d_train,d_test,f_train,f_test=train_test_split(d,f,test_size=0.4)
# print("d_train\n",d_train,"\nd_test\n",d_test,"\nf_train\n",f_train,"\nf_test\n",f_test)
model=LinearRegression()
model.fit(d_train,f_train)
# f_predict=model.predict(d_test)
# print("---output------\n",f_predict)
z=[[5],[6]]
z_predict=model.predict(z)
print(z_predict)
