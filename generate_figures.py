import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np

mpl.rcParams['pdf.fonttype'] = 42
mpl.rcParams['ps.fonttype'] = 42
mpl.rcParams['font.family'] = 'serif'
mpl.rcParams['font.size'] = 16
mpl.rcParams['xtick.labelsize'] = 'small'
mpl.rcParams['ytick.labelsize'] = 'small'
mpl.rcParams['text.usetex'] = False
mpl.rcParams['axes.linewidth'] = 2

colors = cm.get_cmap("tab10", 2)
col1 = colors(0)
col2 = colors(1)

fig = plt.figure(figsize=(12, 6))
ax1 = plt.axes((0.1, 0.1, 0.35, 0.9))
ax2 = plt.axes((0.55, 0.1, 0.35, 0.9))

ax1.spines['right'].set_visible(False)
ax1.spines['top'].set_visible(False)
ax1.grid(True,which='major',axis='both',alpha=0.3)
ax1.set_xlabel(r"$x$")
ax1.set_ylabel(r"$\sin (x)$")

ax2.spines['right'].set_visible(False)
ax2.spines['top'].set_visible(False)
ax2.grid(True,which='major',axis='both',alpha=0.3)
ax2.set_xlabel(r"$x$")
ax2.set_ylabel(r"$\sin (x)$")

x = np.linspace(0, 4*np.pi, 1001)
y = np.sin(x)

ax1.plot(x,y, color='k', label='Frequency')
ax2.plot(x,y, color='k', label='Frequency')
plt.xlim(0, 4*np.pi)

ax1.set_xticks(np.arange(0, 4*np.pi+0.01, np.pi/2))
ax2.set_xticks(np.arange(0, 4*np.pi+0.01, np.pi/2))
labels = ['$0$', r'$\frac{\pi}{2}$', r'$\pi$', r'$\frac{3\pi}{2}$', r'$2\pi$',
          r'$\frac{5\pi}{2}$', r'$3\pi$', r'$\frac{7\pi}{2}$', r'$4\pi$']
ax1.set_xticklabels(labels)
ax2.set_xticklabels(labels)

ax1.axvline(2 * np.pi, color='black', linestyle='dashed', ymax=0.5)
ax2.axvline(2 * np.pi, color='black', linestyle='dashed', ymax=0.5)


window = 250
x0 = 500
# central approximation

lower, upper = y[lower_idx := x0-window], y[upper_idx := x0+window]
slope = (upper - lower) / (upper_idx - lower_idx)

# slope * x0 + n = f(x0)
y_intersect = y[x0] - slope * x0

ax1.plot(domain := x[lower_idx: upper_idx + 1], slope * domain + y_intersect, color=col1, linestyle='dashed', label='central approximation')

ax1.plot(x[x0], 0.0, marker='o', color='k')
ax1.plot(x[upper_idx], 0.0, marker='o', color=col2)
ax1.plot(x[lower_idx], 0.0, marker='o', color=col2)

ax1.text(x[upper_idx] + 0.2, 0.1, r'$f(x_0) + \pi$')
ax1.text(x[lower_idx] + 0.2, 0.1, r'$f(x_0) - \pi$')
ax1.text(x[x0] + 0.2, -0.1, r'$x_0$')


window = 188
lower, upper = y[lower_idx := x0-window], y[upper_idx := x0+window]
slope = (upper - lower) / ((upper_idx - lower_idx) / 1000 * 4 * np.pi)
# slope * x0 + n = f(x0)
y_intersect = y[x0] - slope * x0

ax2.plot(domain := x[lower_idx: upper_idx + 1], slope * domain + y_intersect / 1000 * 4 * np.pi, color=col1, linestyle='dashed', label='central approximation')

ax2.plot(x[x0], 0.0, marker='o', color='k')
ax2.plot(x[upper_idx], y[upper_idx], marker='o', color=col2)
ax2.plot(x[lower_idx], y[lower_idx], marker='o', color=col2)

ax2.text(x[upper_idx] + 0.2, y[upper_idx] + 0.1, r'$f(x_0) + \frac{3\pi}{4}$')
ax2.text(x[lower_idx] - 3, y[lower_idx] - 0.1, r'$f(x_0) - \frac{3\pi}{4}$')
ax2.text(x[x0] + 0.2, -0.1, r'$x_0$')

plt.savefig('figures/central_periodic.svg')
