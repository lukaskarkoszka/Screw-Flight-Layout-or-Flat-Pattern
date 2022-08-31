import math
from matplotlib.patches import Wedge
import matplotlib.pyplot as plt

print('add diameter mm')
d = input()
d=d.replace(',', '.')
d = float(d)

print('add Diameter mm')
D = input()
D=D.replace(',', '.')
D = float(D)

print('add Pitch mm')
P = input()
P=P.replace(',', '.')
P = float(P)

l = math.sqrt((d*3.14)**2 + (P**2))
L = math.sqrt((D*3.14)**2 + (P**2))
dprim = (D-d)/((L/l)-1)
Dprim = (D-d)+dprim
Dangle = 360 - (L/(Dprim*3.14/360))
dangle = 360 - (l/(dprim*3.14/360))

print("dprim " + str(dprim))
print("Dprim " + str(Dprim))
print("Dangle " + str(Dangle))
dpi = 300
fig, ax = plt.subplots()
ax.axis('off')
fig.set_size_inches(Dprim/25.4, Dprim/25.4)
fig.set_dpi(dpi)

wedge = Wedge(Dprim/2, Dprim/2, Dangle, 360, width=(Dprim-dprim)/2, facecolor='black')
ax.add_artist(wedge)
plt.xlim([0,Dprim])
plt.ylim([0,Dprim])
plt.subplots_adjust(left=0, bottom=0, right=1, top=1, wspace=None, hspace=None)
base_filename= str(P)+"_"+str(D)+"_"+str(d)
plt.savefig(r"C:\Users\youUser\Desktop\cnc\%s.png" % base_filename, dpi=dpi)
plt.show()
