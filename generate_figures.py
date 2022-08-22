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

plt.savefig('figures/central_periodic.pdf')

def plot_central(x, y, idx, window, ax):
    # central approximation
    lower, upper = y[lower_idx := idx - window // 2], y[upper_idx := idx + window // 2]
    slope = (upper - lower) / (upper_idx - lower_idx)

    # slope * x0 + n = f(x0)
    y_intersect = y[idx] - slope * idx
    
    ax.plot(domain := x[idx - window: idx + 1 + window], slope * domain + y_intersect, color=col1, label='central approximation')

    ax.plot(x[idx], y[idx], marker='o', color='k')
    
def plot_forward(x, y, idx, window, ax):
    lower, upper = y[lower_idx := idx], y[upper_idx := idx + window]
    slope = (upper - lower) / (upper_idx - lower_idx)
    
    y_intersect = y[idx] - slope * idx
    
    ax.plot(domain := x[idx - window: idx + 1 + window], slope * domain + y_intersect, color=col2, label='forward approximation')
    
def plot_backward(x, y, idx, window, ax):
    lower, upper = y[lower_idx := idx - window], y[upper_idx := idx]
    slope = (upper - lower) / (upper_idx - lower_idx)
    
    y_intersect = y[idx] - slope * idx
    
    ax.plot(domain := x[idx - window: idx + 1 + window], slope * domain + y_intersect, color=col3, label='backward approximation')
    
    
def plot_combined(x, y, idx, window, ax):
    plot_forward(x,  y, idx, window, ax)
    plot_central(x,  y, idx, window, ax)
    plot_backward(x, y, idx, window, ax)
    
colors = cm.get_cmap("tab10", 3)
col1 = colors(0)
col2 = colors(1)
col3 = colors(2)

#fig = plt.figure(figsize=(12, 6))

fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize = (15, 6), sharey=True)

#ax1 = plt.axes((0.1, 0.1, 0.2, 0.6))
#ax2 = plt.axes((0.4, 0.1, 0.2, 0.6))
#ax3 = plt.axes((0.7, 0.1, 0.2, 0.6))

ax1.spines['right'].set_visible(False)
ax1.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)
ax2.spines['top'].set_visible(False)
ax3.spines['right'].set_visible(False)
ax3.spines['top'].set_visible(False)



ax1.grid(True,which='major',axis='both',alpha=0.3)
ax2.grid(True,which='major',axis='both',alpha=0.3)
ax3.grid(True,which='major',axis='both',alpha=0.3)

ax1.set_xlabel(r"$x$")
ax1.set_ylabel(r"$f(x)$")
# ax2.set_xlabel(r"$x$")
# ax2.set_ylabel(r"$f(x)$")
# ax3.set_xlabel(r"$x$")
# ax3.set_ylabel(r"$f(x)$")

x = list(range(700))
y1 = (-np.square(range(200, 0, -1)) + 200**2).reshape(-1,1)
y2 = (np.array([200**2]*300)).reshape(-1,1)
y3 = (-np.square(range(200))+ 200**2).reshape(-1, 1)
y = np.concatenate((y1, y2, y3), axis=0) / 1000


ax1.plot(x,y, color='k', label='Frequency')
ax2.plot(x,y, color='k', label='Frequency')
ax3.plot(x,y, color='k', label='Frequency')

plt.xlim(0, 700)

p1 = 200
p2 = 350
p3 = 500

ax1.axvline(p1, color='black', linestyle='dashed', ymax=0.62)
ax2.axvline(p2, color='black', linestyle='dashed', ymax=0.62)
ax3.axvline(p3, color='black', linestyle='dashed', ymax=0.62)

ax1.set_yticks(np.arange(0, 50.1, 10))
ax2.set_yticks(np.arange(0, 50.1, 10))
ax3.set_yticks(np.arange(0, 50.1, 10))

window = 150

# central approximation
plot_combined(x, y, p1, window, ax1)
plot_combined(x, y, p2, window, ax2)
plot_combined(x, y, p3, window, ax3)

ax1.text(220, 36, r'$x_0$')
ax2.text(330, 43, r'$x_1$')
ax3.text(420, 36, r'$x_2$')

ax2.legend(loc='upper center', fontsize='small')

plt.savefig('figures/approximations.pdf')
