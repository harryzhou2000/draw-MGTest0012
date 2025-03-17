from LogErrLoader import LoadDNDSLogErr
import numpy as np
import matplotlib.pyplot as plt


data_MG = LoadDNDSLogErr("NACA0012-AOA5-MGLP1_.log")
data = LoadDNDSLogErr("NACA0012-AOA5_.log")
data_ILU2_MG = LoadDNDSLogErr("NACA0012-AOA5-ILU2-MGLP1_.log")
data_ILU2 = LoadDNDSLogErr("NACA0012-AOA5-ILU2_.log")
data_GILU2 = LoadDNDSLogErr("NACA0012-AOA5-GILU2_.log")
print(data.keys())

plt.figure(figsize=(12,8), dpi= 160)

def plotOne(data,label):
    plt.plot(data["tWall"][0:-1], data["res0"][0:-1], label = label)
plotOne(data_MG)
plotOne(data)
plotOne(data_ILU2_MG)
plotOne(data_ILU2)


plt.yscale("log")

plt.savefig("out.png")
