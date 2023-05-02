import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from mpl_toolkits.axes_grid1 import make_axes_locatable
from mpl_toolkits.axes_grid1.inset_locator import (inset_axes, InsetPosition,
                                                  mark_inset)
from matplotlib.font_manager import FontProperties
from matplotlib.ticker import MultipleLocator,FormatStrFormatter
from matplotlib.font_manager import FontProperties
import matplotlib.patheffects as PathEffects

from distutils.spawn import find_executable
if find_executable('latex'):
    plt.rc('text', usetex=True)
plt.rc('font', family='serif',size='10')
    
def plot_sol(x, t, q_pre, q_ori, time_instant, cmap_name, c_1, c_2, title):
    fig, ax = plt.subplots(figsize=(5, 7))
    ax.axis('off')

    ####### Row 0: h(t,x) ##################    
    #-----------------------------predicted----------------------------
    gs0 = gridspec.GridSpec(1, 2)
    gs0.update(top=1-0.06, bottom=0.8, left=0.15, right=0.9, wspace=0.2)
    ax = plt.subplot(gs0[:, :])

    h = ax.imshow(q_pre.T, interpolation='nearest', cmap=cmap_name, 
                extent=[t.min(), t.max(), x.min(), x.max()], 
                origin='lower', aspect='auto')
    divider = make_axes_locatable(ax)
    cax = divider.append_axes("right", size="5%", pad=0.05)
    fig.colorbar(h, cax=cax)
    ax.set_xlabel('$t$')
    ax.set_ylabel('$x$')
    ax.annotate("(a)", xy=(0.3, 0.47), xycoords='axes fraction', fontsize='medium',
           xytext=(-15, -15), textcoords='offset points', color='k',
           path_effects=[PathEffects.withStroke(linewidth=1, foreground='k')],
           horizontalalignment='right', verticalalignment='top')
    line = np.linspace(x.min(), x.max(), 2)[:,None]
    ax.plot(t[time_instant[0]]*np.ones((2,1)), line, 'b-', linewidth = 2)
    ax.plot(t[time_instant[1]]*np.ones((2,1)), line, 'b-', linewidth = 2)
    ax.plot(t[time_instant[2]]*np.ones((2,1)), line, 'b-', linewidth = 2)
    ax.set_title('Predicted '+ title)

    #-----------------------------Exact----------------------------
    gs2 = gridspec.GridSpec(1, 2)
    gs2.update(top=0.7, bottom=0.58, left=0.15, right=0.9, wspace=0.2)
    ax = plt.subplot(gs2[:, :])
    h = ax.imshow(q_ori.T, interpolation='nearest', cmap=cmap_name, 
                extent=[t.min(), t.max(), x.min(), x.max()], 
                origin='lower', aspect='auto')
    divider = make_axes_locatable(ax)
    cax = divider.append_axes("right", size="5%", pad=0.05)
    fig.colorbar(h, cax=cax)
    ax.set_xlabel('$t$')
    ax.set_ylabel('$x$')
    ax.annotate("(b)", xy=(0.3, 0.47), xycoords='axes fraction', fontsize='medium',
           xytext=(-15, -15), textcoords='offset points', color='k',
           path_effects=[PathEffects.withStroke(linewidth=1, foreground='k')],
           horizontalalignment='right', verticalalignment='top')
    ax.set_title('Exact '+title)

    #-----------------------------error----------------------------
    gs3 = gridspec.GridSpec(1, 2)
    gs3.update(top=0.48, bottom=0.36, left=0.15, right=0.9, wspace=0.2)
    ax = plt.subplot(gs3[:, :])
    h = ax.imshow((q_pre-q_ori)**2, interpolation='nearest', cmap=cmap_name, 
                extent=[t.min(), t.max(), x.min(), x.max()], 
                origin='lower', aspect='auto')
    divider = make_axes_locatable(ax)
    cax = divider.append_axes("right", size="5%", pad=0.05)
    cbar = fig.colorbar(h, cax=cax)
    cbar.formatter.set_powerlimits((0, 0))
    ax.set_xlabel('$t$')
    ax.set_ylabel('$x$')
    ax.annotate("(c)", xy=(0.3, 0.47), xycoords='axes fraction', fontsize='medium',
           xytext=(-15, -15), textcoords='offset points', color='k',
           path_effects=[PathEffects.withStroke(linewidth=1, foreground='k')],
           horizontalalignment='right', verticalalignment='top')
    ax.set_title('Error')
    
    ####### Row 2: h(t,x) slices ##################    
    gs1 = gridspec.GridSpec(1, 3)
    gs1.update(top=0.25, bottom=0.13, left=0.13, right=0.9, wspace=0.5)
    ax = plt.subplot(gs1[0, 0])
    ax.plot(x, q_ori[time_instant[0],:], c=c_1, ls='-', linewidth = 3, label = 'Exact')       
    ax.plot(x, q_pre[time_instant[0],:], c=c_2, ls='--', linewidth = 2, label = 'Prediction')
    ax.set_xlabel('$x$')
    ax.set_ylabel(title)    
    ax.annotate("(d)", xy=(0.6, 0.5), xycoords='axes fraction', fontsize='medium',
           xytext=(-15, -15), textcoords='offset points', color='k',
           path_effects=[PathEffects.withStroke(linewidth=1, foreground='k')],
           horizontalalignment='right', verticalalignment='top')
    ax.set_title('$t = %.2f$' % (t[time_instant[0]]))
    
    ax = plt.subplot(gs1[0, 1])
    ax.plot(x, q_ori[time_instant[1],:], c=c_1, ls='-', linewidth = 3, label = 'Exact')       
    ax.plot(x, q_pre[time_instant[1],:], c=c_2, ls='--', linewidth = 2, label = 'Prediction')
    ax.set_xlabel('$x$')
    ax.annotate("(e)", xy=(0.6, 0.5), xycoords='axes fraction', fontsize='medium',
           xytext=(-15, -15), textcoords='offset points', color='k',
           path_effects=[PathEffects.withStroke(linewidth=1, foreground='k')],
           horizontalalignment='right', verticalalignment='top')
    ax.set_title('$t = %.2f$' % (t[time_instant[1]]))
    ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.5), ncol=5, frameon=True)
    
    ax = plt.subplot(gs1[0, 2])
    ax.plot(x, q_ori[time_instant[2],:], c=c_1, ls='-', linewidth = 3, label = 'Exact')       
    ax.plot(x, q_pre[time_instant[2],:], c=c_2, ls='--', linewidth = 2, label = 'Prediction')
    ax.set_xlabel('$x$')
    ax.set_title('$t = %.2f$' % (t[time_instant[2]]))
    ax.annotate("(f)", xy=(0.6, 0.5), xycoords='axes fraction', fontsize='medium',
           xytext=(-15, -15), textcoords='offset points', color='k',
           path_effects=[PathEffects.withStroke(linewidth=1, foreground='k')],
           horizontalalignment='right', verticalalignment='top')
    return fig