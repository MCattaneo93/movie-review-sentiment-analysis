import subprocess
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

etas = np.arange(0.1, .4, 0.1)
feature_sizes = np.arange(10, 120, 20)

accuracy_values = np.empty((len(etas), len(feature_sizes)))
max_val = 0.0
for i, feature_size in enumerate(feature_sizes):
    subprocess.run(['python','pre-process.py','--loop', str(feature_size)])
    
    for j, eta in enumerate(etas):
        
        accuracy = 0
        for k in range(10):
            val = (subprocess.check_output(['python','LR.py','--loop', str(eta)]).decode())
            accuracy += float(val)
        accuracy_values[j,i]=(accuracy / 10)
        if(accuracy/10 > max_val):
            max_val = accuracy/10
    
file = open("accuracies.txt", "w")
for i in accuracy_values:
    file.write(str(i))

x_vals, y_vals = np.meshgrid(etas, feature_sizes)
z_vals = accuracy_values.flatten()

fig, ax = plt.subplots()
sc = ax.scatter(x_vals.flatten(), y_vals.flatten(), c=z_vals, cmap='viridis')
ax.set_xlabel('Eta')
ax.set_ylabel('Feature Size')
ax.set_title('Accuracy vs. Eta and Feature Size')
cbar = fig.colorbar(sc)
plt.savefig('plot.png')
print(max_val)       