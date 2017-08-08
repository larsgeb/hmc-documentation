import glob
import numpy as np
import random as random
import matplotlib.pylab as pylab
import matplotlib.pyplot as plt
import locale
import decimal
import matplotlib.ticker as plticker

intervals = 5

loc = plticker.MultipleLocator(base=intervals)

# ============================================================
# - Setup.
# ============================================================

params = {'legend.fontsize': 'x-large',
          'figure.figsize': (5, 5),
          'axes.labelsize': 21,
          'axes.titlesize': 'x-large',
          'xtick.labelsize': 21,
          'ytick.labelsize': 21
          }
pylab.rcParams.update(params)
locale.setlocale(locale.LC_ALL, 'en_US.utf8')  # Used for number formatting (thousands separators)
datapoints = [15, 30, 45, 90, 180, 1080, 3240]
times = [118.324, 116.043, 116.959, 123.445, 116.847, 118.251, 115.802]

plt.semilogx(datapoints, times)
plt.xlim([0, 3200])
plt.ylim([90, 150])
plt.xlabel('Number of datapoints')
plt.ylabel('Runtime [s]')
plt.tight_layout()
plt.grid(b=True, which='major', color='r', linestyle='-', alpha=.25)
plt.grid(b=True, which='minor', color='r', linewidth=0.1, linestyle='-', alpha=.05)

# major_ticks = [100,250,1000,3000]
# # minor_ticks = np.arange(50, 1001, 50)
#
# plt.gca().set_xticks(major_ticks)
# plt.gca().set_xticklabels(major_ticks)
# plt.gca().set_xticks(minor_ticks, minor=True)

plt.minorticks_on()
plt.savefig("performanceData.pdf")
# plt.show()
