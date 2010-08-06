from numpy import loadtxt
from pylab import (plot, show, title, xlim, ylim, legend, xlabel, ylabel,
        savefig)
from h5py import File

print "Loading data..."
f = File("data.hdf5")
x = f["/hydrogen/x"]
eigs = f["/hydrogen/eigs"]
n = eigs.shape[1]
u = []
for i in range(n):
    u.append(eigs[:, i])
print "    Done."
print "Plotting..."
l = 0
for i in [0, 1, 2]:
    y = u[i].copy()
    y /= y[0]
    n = i+1
    plot(x, y, lw=3, label="$R_{%d,%d}$" % (n, l))
print "    Done."
title("Eigenfunctions (l=%d, Z=1)" % l)
legend()
xlabel("$\\rho$ [a.u.]")
ylabel("$R_{n,l}(\\rho)$")
xlim([-1, 40])
ylim([-0.2, 1.1])
savefig("hydrogen_vec.pdf")
#show()
