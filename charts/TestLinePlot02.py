# =====================================================
# TestLinePlot02.py ...
# =====================================================

import numpy as np
import matplotlib.pyplot as plt

# main method ...

def main():
    print("--- Enter TestLinePlot02.main()              ... ");
    print("--- ======================================== ... ");

    x = np.arange(14)
    y = np.sin(x / 2)

    plt.step(x, y + 2, label='pre (default)')
    plt.plot(x, y + 2, 'o--', color='grey', alpha=0.3)

    plt.step(x, y + 1, where='mid', label='mid')
    plt.plot(x, y + 1, 'o--', color='grey', alpha=0.3)

    plt.step(x, y, where='post', label='post')
    plt.plot(x, y, 'o--', color='grey', alpha=0.3)

    plt.grid(axis='x', color='0.95')
    plt.legend(title='Parameter where:')
    plt.title('plt.step(where=...)')
    plt.show()

    print("--- ======================================== ... ");
    print("--- Leave TestLinePlot02.main()              ... ");

# call the main method ...

main()



