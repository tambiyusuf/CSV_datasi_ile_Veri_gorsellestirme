import pandas as pd
import matplotlib.pyplot as plt

veri = pd.read_csv("cpu.csv")
plt.figure()
plt.plot(veri["Product"], veri["Transistors(million)"], color = "red", alpha = 0.9) # alpha saydamlık
plt.title('CPU-TRANSİSTÖR')
plt.xlabel("CPU MODEL")
plt.ylabel("TRANSİSTÖR SAYISI")
plt.grid(True)
plt.show()


