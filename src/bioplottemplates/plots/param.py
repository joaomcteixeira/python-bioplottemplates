"""Plot a single parameter."""
import itertools
import numpy as np

from matplotlib import pyplot as plt

from bioplottemplates import log
from bioplottemplates.libs import libmsg, libutil
from bioplottemplates.logger import S, T


def plot(
        x_data,
        y_data,
        *,
        labels="No label provided",
        suptitle=None,
        xlabel=None,
        ylabel=None,
        colors='blue',
        alpha=0.7,
        grid=True,
        grid_color="lightgrey",
        grid_ls="-",
        grid_lw=1,
        grid_alpha=0.5,
        legend=True,
        legend_fs=6,
        legend_loc=4,
        vert_lines=None,
        filename='plot_param.pdf',
        **kwargs
        ):
    """
    Plot a single plot with the combined RMSD.
    
    Bellow parameters concern data representation and are considered
    of highest importance because their incorrect use can mislead
    data analysis and consequent conclusions.
    
    Plot style parameters concernning only plot style, i.e., colors,
    shapes, fonts, etc... and which do not distort the actual data,
    are not listed in the paremeter list bellow. We hope these
    parameter names are self-explanatory and are listed in the function
    definition.
    
    Parameters
    ----------
    x_data : interable of numbers
        Container of the X axis data. Should be accepted
        by matplotlib.
    
    y_data : np.ndarray, shape=(M,)
        Container of the Y axis data.
        Where M is the RMSDs data for the combined chains.
    
    label : str, optional
        The label to represent in plot legend.
        Defauts to: "no labels provided".
    
    fig_name : str, optional
        The file name with which the plot figure will be saved
        in disk. Defaults to rmsd_individual_chains_one_subplot.pdf.
        You can change the file type by specifying its extention in
        the file name.
    """
    log.info(T("Plotting parameter:"))
    
    # prepares data in
    y_data = np.array(y_data)
    if y_data.ndim == 1:
        y_data = y_data[np.newaxis, :]
    
    plot_labels = libutil.make_list(labels)
    plot_colors = libutil.make_list(colors)
    plot_colors = itertools.cycle(plot_colors)
    
    assert y_data.shape[0] == len(plot_labels), (
        '{} vs {}'.format(y_data.shape[0], len(plot_labels)))
    # done data preparation

    fig, ax = plt.subplots(nrows=1, ncols=1)
    
    plt.tight_layout(rect=[0.05, 0.02, 0.995, 0.985])
    
    fig.suptitle(
        suptitle,
        x=0.5,
        y=0.990,
        va="top",
        ha="center",
        )
    
    for yy, ll in zip(y_data, plot_labels):
        ax.plot(
            x_data,
            yy,
            label=ll,
            color=next(plot_colors),
            alpha=alpha,
            )
    
    ax.set_xlabel(xlabel, weight='bold')
    ax.set_ylabel(ylabel, weight='bold')
    
    ax.set_xlim(x_data[0], x_data[-1])
    ax.set_ylim(0)
    
    if grid:
        ax.grid(
            color=grid_color,
            linestyle=grid_ls,
            linewidth=grid_lw,
            alpha=grid_alpha,
            )
    if isinstance(vert_lines, (list, tuple)):
        for line in vert_lines:
            ax.axvline(x=float(line), color='k')

    if legend:
        ax.legend(
            fontsize=legend_fs,
            loc=legend_loc,
            )
    
    fig.savefig(filename)
    log.info(S(libmsg.fig_saved.format(filename)))
        
    plt.close("all")
    
    return
