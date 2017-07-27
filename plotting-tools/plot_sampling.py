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
# font = {'family': 'normal',
#         'weight': 'bold',
#         'size': 22}
#
# rc('font', **font)
#
# # rc('font', **{'family': 'sans-serif', 'sans-serif': ['Helvetica']})
# rc('text', usetex=True)

means1 = [1.11702566667,
          1.24513575,
          1.20420687097,
          1.22881791935,
          1.1883001875,
          1.20404536539,
          1.20493197189,
          1.19987591143]
means2 = [3.12158888889,
          2.9289925,
          2.94578,
          2.89333322581,
          2.9398928869,
          2.94154793962,
          2.94279767944,
          2.94130887439]
stdx = [0.721992507513,
        0.5743872578,
        0.702090055291,
        0.620473290286,
        0.814212915858,
        0.889274576329,
        0.917201077196,
        0.928201386875]
stdy = [0.498351188475,
        0.384954833057,
        0.220285123171,
        0.331295314475,
        0.231492907228,
        0.216582110647,
        0.215764002743,
        0.215389520556]
covxy = [-0.287855108075,
         -0.00379498183062,
         -0.0132059810855,
         -0.0768415538817,
         -0.0246957139022,
         -0.00214150808749,
         -0.0108139354006,
         0.00543019184187]

accepted = [9.0, 16.0, 31.0, 62.0, 336.0, 1325.0, 6576.0, 32880.0]
total = [10.0, 20.0, 50.0, 100.0, 500.0, 2000.0, 10000.0, 50000.0]
percentageAccepted = []
i = 0
for accept in accepted:
    percentageAccepted.append(accept / total[i])
    i += 1
plt.semilogx(total, percentageAccepted, 'k', linewidth=1, zorder=1)
plt.grid(b=True, which='major', color='r', linestyle='-')
plt.grid(b=True, which='minor', color='r', linestyle='--')
plt.xlim([10, 50000])
plt.xlabel('iterations')
plt.ylabel('percentage accepted')
plt.gcf().subplots_adjust(bottom=0.15)
plt.savefig('../results/2d_naive/accepted.png')
plt.savefig('../results/2d_naive/accepted.pdf')
plt.close()

plt.semilogx(total, means1, 'k', linewidth=1, zorder=1)
plt.grid(b=True, which='major', color='r', linestyle='-')
plt.grid(b=True, which='minor', color='r', linestyle='--')
plt.xlim([10, 50000])
plt.xlabel('iterations')
plt.ylabel('$\mu_1$')
plt.gcf().subplots_adjust(bottom=0.15)
plt.savefig('../results/2d_naive/means1.png')
plt.savefig('../results/2d_naive/means1.pdf')
plt.close()

plt.semilogx(total, means2, 'k', linewidth=1, zorder=1)
plt.grid(b=True, which='major', color='r', linestyle='-')
plt.grid(b=True, which='minor', color='r', linestyle='--')
plt.xlim([10, 50000])
plt.xlabel('iterations')
plt.ylabel('$\mu_2$')
plt.gcf().subplots_adjust(bottom=0.15)
plt.savefig('../results/2d_naive/means2.png')
plt.savefig('../results/2d_naive/means2.pdf')
plt.close()
#
# plt.semilogx(total, stdx, 'k', linewidth=1, zorder=1)
# plt.grid(b=True, which='major', color='r', linestyle='-')
# plt.grid(b=True, which='minor', color='r', linestyle='--')
# plt.xlim([10, 50000])
# plt.xlabel('iterations')
# plt.ylabel('$\sigma_1$')
# plt.savefig('../results/2d_naive/std1.png')
# plt.savefig('../results/2d_naive/std1.pdf')
# plt.close()
#
# plt.semilogx(total, stdy, 'k', linewidth=1, zorder=1)
# plt.grid(b=True, which='major', color='r', linestyle='-')
# plt.grid(b=True, which='minor', color='r', linestyle='--')
# plt.xlim([10, 50000])
# plt.xlabel('iterations')
# plt.ylabel('$\sigma_2$')
# plt.savefig('../results/2d_naive/std2.png')
# plt.savefig('../results/2d_naive/std2.pdf')
# plt.close()
#
# plt.semilogx(total, covxy, 'k', linewidth=1, zorder=1)
# plt.grid(b=True, which='major', color='r', linestyle='-')
# plt.grid(b=True, which='minor', color='r', linestyle='--')
# plt.xlim([10, 50000])
# plt.xlabel('iterations')
# plt.ylabel('mu1')
# plt.savefig('../results/2d_naive/cov12.png')
# plt.savefig('../results/2d_naive/cov12.pdf')
# plt.close()

# plt.close()
