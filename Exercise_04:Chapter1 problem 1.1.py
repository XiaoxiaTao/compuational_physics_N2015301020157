import numpy as np
import matplotlib.pyplot as plt
V = []
t = []
g = 9.8
dt = 1
V.append(0)
t.append(0)
end_time = 10
 
for i in range(int(end_time / dt)):
        tmp = V[i] - g * dt
        V.append(tmp)
        t.append(dt * (i + 1))
        print t[-1], V[-1]
        
plt.figure(figsize=(6,4))
plt.plot(t,V,label="V(t)",color="black",linewidth=1)
plt.xlabel("t(s)")
plt.ylabel("V(m/s)")
plt.legend()
plt.show()

 
 
[实验报告](https://www.zybuluo.com/Xiaoxia-/note/901840)
