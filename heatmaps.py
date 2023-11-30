# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 10:43:41 2023

@author: erik-
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 10:35:20 2023

@author: erik-
"""

import matplotlib.pyplot as plt
import numpy as np

# Generate data for the plots
x = np.linspace(0, 1, 100)
y = x
X, Y = np.meshgrid(x, y)


Z1 = X/(np.ones_like(X)+(X+Y)**2)  # Quadratic colormap 1

Z2 = Y/(1+(X+Y)**2)  # Quadratic colormap 1

# Create a figure and subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))#, sharey = True)

# Plot the first quadratic colormap
quad1 = ax1.pcolormesh(X, Y, Z1, cmap='plasma')
ax1.set_title('Utility Player 1')

# Plot the second quadratic colormap
quad2 = ax2.pcolormesh(X, Y, Z2, cmap='plasma')
ax2.set_title('Utility Player 2')


vmin_common = min(quad1.get_clim()[0], quad2.get_clim()[0])
vmax_common = max(quad1.get_clim()[1], quad2.get_clim()[1])

# Normalize the colormaps based on the common color limits
quad1.set_clim(vmin_common, vmax_common)
quad2.set_clim(vmin_common, vmax_common)


cbar = fig.colorbar(quad2, ax=[ax1, ax2], orientation='vertical')
#cbar.set_label('Utility')

#plt.subplots_adjust(wspace=0.5)

#plt.tight_layout()

plt.show()
#for i in range(10)
plt.plot(x,x/(1+(x+x)**2))
plt.plot(x,x/(1+((0.1+x)+x)**2))
plt.plot(x,x/(1+((0.2+x)+x)**2))
plt.plot(x,x/(1+((0.3+x)+x)**2))
#plt.show()
