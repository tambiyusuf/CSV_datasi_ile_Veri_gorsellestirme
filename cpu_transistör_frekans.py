
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#veri çektiğimiz sütun
veri = pd.read_csv("cpu.csv")
x = np.arange(len(veri))
fig, ax = plt.subplots()
width = 0.25

rects1 = ax.bar(x - width/2,veri["Transistors"], width, label='Transistors')
rects2 = ax.bar(x + width, veri["Freq"], width, label='Freq')
#işlemci isimlerini liste formatına çevirmek için yazdım.
labelss = []
while len(labelss) < 10:
    for i in (veri["Product"]):
      labelss.append(i)


ax.set_ylabel('değerler')
ax.set_xlabel("cpu")
ax.set_title('cpu-transistör-frekans grafiği')
ax.legend()
#x ekseni isimleri çevirdiğimiz list formatını buraya ekledim.
ax.set_xticks([0,1,2,3,4,5,6,7,8,9],labels = labelss)

ax.bar_label(rects1, padding=3)
ax.bar_label(rects2, padding=3)

fig.tight_layout()

plt.show()

