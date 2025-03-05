# =====================================================
# TestLinePlot01.py: Very simple line plot ....
# =====================================================

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# main method ...

def main():
    print("--- Enter TestLinePlot01.main()              ... ");
    print("--- ======================================== ... ");

    # Data for plotting

    t = np.arange(0.0, 2.0, 0.01)
    s = 1 + np.sin(2 * np.pi * t)

    fig, ax = plt.subplots()
    ax.plot(t, s)

    ax.set(xlabel='time (s)', ylabel='voltage (mV)',
           title='About as simple as it gets, folks')
    ax.grid()

    # Save figure to test.png

    fig.savefig("test.png")
    plt.show()

    print("--- ======================================== ... ");
    print("--- Leave TestLinePlot01.main()              ... ");

# call the main method ...

main()

