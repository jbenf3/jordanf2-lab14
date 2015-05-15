import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate
from matplotlib import cm
t,v = np.loadtxt("droptower_vdata.txt", unpack =
               True)
#print t
#print v

pos = scipy.integrate.cumtrapz(v,t,initial=0)

acc = np.gradient(v)

#print acc

pos = pos + 30

fig = plt.figure(figsize=(15,10))

plt.subplot(2,2,2)
plt.plot(t,pos, c='green', marker='o', label='$Position\,(m)$')
plt.ylabel('$Position$')
plt.xlabel('$Time$')
plt.legend(prop={'size':12})

plt.subplot(2,2,3)
plt.plot(t,v, c='blue', marker='v', label='$Velocity\,(m/s)$')
plt.xlabel('$Time$')
plt.ylabel('$Velocity$')
plt.ylim([-25,25])
plt.axhline(dashes=[1,5])
plt.legend(prop={'size':12})

plt.subplot(2,2,4)
plt.plot(t,acc, c='red', marker='^', label='$Acceleration\,(m/s^2)$')
plt.xlabel('$Time$')
plt.ylabel('$Acceleration$')
plt.ylim([-15,25])
plt.axhline(dashes=[1,5])
plt.legend(prop={'size':12})

plt.subplot(2,2,1)
plt.plot(t,pos, color='green', marker='o', label='$Position\,(m)$')
plt.plot(t,v,color='blue', marker='v', label='$Velocity\,(m/s)$')
plt.plot(t,acc,color='red', marker='^', label='$Acceleration\,(m/s^2)$')
plt.axhline(dashes=[1,5])
plt.xlabel('$Time$')
plt.ylim([-30,75])
plt.title('$Position,\,Velocity,\,and\,Acceleration$', fontsize=10)
plt.legend(prop={'size':12})

fig.savefig('prettyplots.pdf')

plt.show()
