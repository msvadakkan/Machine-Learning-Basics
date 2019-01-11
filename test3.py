import matplotlib.pyplot as plt
x=[1,2,3]
y=[4,5,6]
z=[5,6,7]
w=[9,0,1]
plt.plot(x,y,label="what")
plt.plot(x,z,label="ookey")
plt.plot(x,w,label="okey")
plt.legend(loc='upper right',fontsize='small')
plt.show()
