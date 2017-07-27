import glob
import numpy as np
import random as random
import matplotlib.pylab as pylab
import matplotlib.pyplot as plt
import locale
import decimal


def drange(x, y, jump):
    while x < y:
        yield float(x)
        x = x + float(decimal.Decimal(jump))


# ============================================================
# - Setup.
# ============================================================

# - Number of burn-in samples to be ignored.
nbi = 0
# - Dimensions of interest.
dim_1 = 0
dim_2 = 1
# - Incremental displacement for duplicate points.
epsilon_1 = 0.0003
epsilon_2 = 0.0003
params = {'legend.fontsize': 'x-large',
          'figure.figsize': (16, 8),
          'axes.labelsize': 16,
          'axes.titlesize': 'x-large',
          'xtick.labelsize': 16,
          'ytick.labelsize': 16
          }
pylab.rcParams.update(params)
locale.setlocale(locale.LC_ALL, 'en_US.utf8')  # Used for number formatting (thousands separators)

# ============================================================
# - Read samples and plotting0
# ============================================================

columns = 4
rows = 2
f, axes = plt.subplots(rows, columns, sharex=True, sharey=True)

# Creating an underlying subplot using some magic, to label the axes
f.patch.set_facecolor('white')
ax = f.add_subplot(111)
ax.spines['top'].set_color('none')
ax.spines['bottom'].set_color('none')
ax.spines['left'].set_color('none')
ax.spines['right'].set_color('none')
ax.tick_params(labelcolor='w', top='off', bottom='off', left='off', right='off')
ax.set_zorder(-1)
ax.set_xlabel('parameter 1')
ax.set_ylabel('parameter 2')

# Create dictionary of all read folders
fileNames = glob.glob('../results/2d_naive/*/samples.txt')
sampleAmounts = map(lambda fileName: float(fileName.replace("../results/2d_naive/", "").replace("/samples.txt", "")),
                    fileNames)
dictFiles = dict(zip(sampleAmounts, fileNames))

# Shamefully, looping through a dictionary with an increasing index requires an extra variable,
# and of course every variable kills a kitten.
iterator = 0

for key, value in iter(sorted(dictFiles.iteritems())):  # The sorting here is very important for nice plots
    fid = open(value)
    print value
    dummy = fid.read().strip().split()
    fid.close()  # Close it!

    # Parsing all that data
    dimension = int(dummy[0])
    iterations = int(dummy[dummy.__len__() - 1]) - nbi
    x = np.zeros(iterations)
    y = np.zeros(iterations)
    x_plot = np.zeros(iterations)
    y_plot = np.zeros(iterations)
    q_opt = np.zeros(dimension)
    chi = 1.0e100

    # Black magic happening below, please ignore
    for i in range(iterations):
        x[i] = float(dummy[2 + dim_1 + (i + nbi) * (dimension + 1)])
        y[i] = float(dummy[2 + dim_2 + (i + nbi) * (dimension + 1)])
        x_plot[i] = x[i]
        y_plot[i] = y[i]
        chi_test = float(dummy[2 + dimension + (i + nbi) * (dimension + 1)])
        if chi_test < chi:
            chi = chi_test
            print 'chi_min=', chi_test
            for k in range(dimension):
                q_opt[k] = float(dummy[2 + k + (i + nbi) * (dimension + 1)])

        if i > 0 and x[i] == x[i - 1] and x[i] > 0 and y[i] == y[i - 1]:
            x_plot[i] += epsilon_1 * random.gauss(0.0, 1.0)
            y_plot[i] += epsilon_2 * random.gauss(0.0, 1.0)

    # =========================================== #
    # - The actual interesting stuff, plotting  - #
    # =========================================== #

    # Linearly stepping through all the subplots in an nd array requires some creativity. (I did this myself!!)
    verIndex = int(np.floor(iterator / columns))
    horIndex = iterator % columns

    # Now choose either of these lines to plot histograms ...
    # axes[verIndex][horIndex].hist(x, color='k', normed=True, bins=list(drange(-1-0.075, 3.5+0.075, '0.075')))
    # axes[verIndex][horIndex].hist(x, color='k', normed=True, bins=list(drange(1.5, 4.5, '0.05')))

    # ... or this block to plot 2D histograms
    h = axes[verIndex][horIndex].hist2d(x, y, bins=40, normed=True, cmap='binary')
    PCM = axes[verIndex][horIndex].get_children()[9]
    cHandle = plt.colorbar(PCM, ax=axes[verIndex][horIndex])

    if iterator == 0:
        cHandle.set_label('probability', labelpad=-2)
    if iterator != 0:
        cHandle.set_label('probability')

    axes[verIndex][horIndex].set_title('%s samples' % locale.format("%d", float(key), grouping=True))

    # iterator += 1
plt.show()
plt.close()
