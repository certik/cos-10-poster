#! /usr/bin/env python

from matplotlib.patches import Ellipse
from pylab import plot, show, savefig, grid, gca, legend, figure, title, \
        xlabel, ylabel, ylim

import hydrogen_uniformpfem
import hydrogen_romanowski
import hydrogen_hpfem
import hydrogen_pfem
import hydrogen_pfem_uniform_init

def do_plot(x, y, n, l, color="k", label=""):
    n_r = n - l - 1
    if n_r == 0:
        plot(x, y, color + "-o", label=label)
    else:
        plot(x, y, color + "-o")

    grid(True)
    ax = gca()
    xlabel("DOFs")
    ylabel("$E_{\\rm FE}-E_{\\rm exact}$ [Ha]")
    ax.set_yscale("log")
    ylim(ymin=1e-8)
    title("Eigenvalues (l=%d, Z=1)" % l)
    legend()

n_eig = 3
l = 0
print "Saving to hydrogen_l_0.pdf"
for i in range(n_eig):
    n = l+1+i
    do_plot(hydrogen_uniformpfem.R_x[l], hydrogen_uniformpfem.R_y[n, l],
            n, l, "k", "uniform-$p$-FEM (L)")
for i in range(n_eig):
    n = l+1+i
    do_plot(hydrogen_romanowski.R_x[l], hydrogen_romanowski.R_y[n, l],
            n, l, "m", "$h$-FEM (Romanowski, U)")
for i in range(n_eig):
    n = l+1+i
    do_plot(hydrogen_pfem.R_x[l], hydrogen_pfem.R_y[n, l],
            n, l, "y", "$p$-FEM (L)")
for i in range(n_eig):
    n = l+1+i
    do_plot(hydrogen_pfem_uniform_init.R_x[l],
            hydrogen_pfem_uniform_init.R_y[n, l],
            n, l, "b", "$p$-FEM (U)")
for i in range(n_eig):
    n = l+1+i
    do_plot(hydrogen_hpfem.R_x[l], hydrogen_hpfem.R_y[n, l],
            n, l, "r", "$hp$-FEM (U)")

#ax = gca()
#el = Ellipse((20, 3e-5), 5, 0.5e-4)
#ax.add_patch(el)
#ax.annotate('hp/p-FEM', xy=(.35, .35),  xycoords='axes fraction',
#        xytext=(0.2, 0.2), textcoords="axes fraction",
#        arrowprops=dict(facecolor="black", shrink=0.05),
#                        horizontalalignment='right',
#                        verticalalignment='top')
#ax.annotate('h-FEM', xy=(.70, .45),  xycoords='axes fraction',
#        xytext=(0.95, 0.45), textcoords="axes fraction",
#        arrowprops=dict(facecolor="black", shrink=0.05),
#                        horizontalalignment='right',
#                        verticalalignment='top')


savefig("hydrogen_l_0.pdf")
#show()
