import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

veri = pd.read_csv("cpu.csv")
plt.figure()
plt.plot(veri["Product"], veri["Freq(MHz)"],  color = "green", alpha = 0.9) # alpha saydamlık
plt.title("cpu-frekans")
plt.xlabel("CPU MODEL")
plt.ylabel("Frekans(MHz)")
plt.grid(True)
plt.show()


