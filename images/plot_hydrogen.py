from numpy import loadtxt
from pylab import (plot, show, title, xlim, ylim, legend, xlabel, ylabel,
        savefig)

print "Loading data..."
A = loadtxt("u_hydrogen.data")
x = A[:, 0]
n = A.shape[1]-1
u = []
for i in range(n):
    u.append(A[:, i+1])
print "    Done."
print "Plotting..."
l = 0
for i in [0, 1, 2]:
    y = u[i].copy()
    y /= y[0]
    n = i+1
    plot(x, y, lw=3, label="$R_{%d,%d}$" % (n, l))
print "    Done."
title("Eigenvectors (l=%d, Z=1)" % l)
legend()
xlabel("$\\rho$ [a.u.]")
ylabel("$R_{n,l}(\\rho)$")
xlim([-1, 40])
ylim([-0.2, 1.1])
savefig("hydrogen_vec.pdf")
#show()
