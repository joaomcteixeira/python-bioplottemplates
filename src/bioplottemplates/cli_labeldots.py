import argparse

from bioplottemplates.libs import libcli
from bioplottemplates.plots import label_dots


ap = libcli.CustomParser(
    description=__doc__,
    formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

ap.add_argument(
    'data_csv',
    help='The CSVs files to plot',
    nargs='+',
    )


ap.add_argument(
    '-v',
    '--plotvars',
    help=(
        'Plot variables. '
        'Example: -v xlabel=frames ylabel=RMSD color=red.'
        ),
    nargs='*',
    action=libcli.ParamsToDict,
    )


def maincli():
    cmd = load_args()
    main(**vars(cmd))


def main(csv_files, plot_params):
    
    labels = extract_labels(csv_files)
    data = extract_data(csv_files)
    
    label_dots.plot(
        labels,
        data,
        **plot_params,
        )

    pass


if __name__ == '__main__':
    maincli()
