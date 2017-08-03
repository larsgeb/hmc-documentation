import glob
import numpy as np
import random as random
import matplotlib.pylab as pylab
import matplotlib.pyplot as plt
import locale
import decimal


# from matplotlib import rc


def drange(x, y, jump):
    while x < y:
        yield float(x)
        x = x + float(decimal.Decimal(jump))


# ============================================================
# - Setup.
# ============================================================

params = {'legend.fontsize': 'x-large',
          'figure.figsize': (8, 4),
          'axes.labelsize': 16,
          'axes.titlesize': 'x-large',
          'xtick.labelsize': 16,
          'ytick.labelsize': 16
          }
pylab.rcParams.update(params)
locale.setlocale(locale.LC_ALL, 'en_US.utf8')  # Used for number formatting (thousands separators)

amount = [4, 6, 8, 12, 16, 24, 30, 45, 70]
accepted = [25542.0, 20672.0, 17095.0, 11444.0, 8102.0, 4059.0, 2468.0, 996.0, 133.0]
time = [4.48501, 5.95428, 6.54415, 9.79743, 13.5715, 19.4229, 25.4179, 37.5877, 62.3415]

percentage_accepted = []
for i in accepted:
    percentage_accepted.append(100*i/50000)

plt.grid(b=True, which='major', color='r', linestyle='-',alpha=.25)
plt.grid(b=True, which='minor', color='r', linewidth=0.1, linestyle='-',alpha=.05)
plt.minorticks_on()
plt.plot(amount, percentage_accepted, 'k', linewidth=2, zorder=1000)
plt.xlim([4, 70])
plt.xlabel('parameters')
plt.ylabel('% accepted')
plt.gcf().subplots_adjust(bottom=0.15)
# plt.show()
plt.savefig('../../results/higher_dim/acceptance_rate.pdf')
plt.close()

plt.grid(b=True, which='major', color='r', linestyle='-',alpha=.25)
plt.grid(b=True, which='minor', color='r', linewidth=0.1, linestyle='-',alpha=.05)
plt.minorticks_on()
plt.plot(amount, time, 'k', linewidth=2, zorder=1000)
plt.xlim([4, 70])
plt.xlabel('parameters')
plt.ylabel('algorithm runtime [seconds]')
plt.gcf().subplots_adjust(bottom=0.15)
# plt.show()
plt.savefig('../../results/higher_dim/performance.pdf')
plt.close()
