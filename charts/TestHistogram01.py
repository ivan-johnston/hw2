# =====================================================
# TestHistogram01.py ...
# =====================================================

import matplotlib.pyplot as plt
import numpy as np

# main method ...

def main():
    print("--- Enter TestHistogram01.main()             ... ");
    print("--- ======================================== ... ");

    # Use numpy to generate a bunch of random data in a bell curve around 5.

    n = 5 + np.random.randn(1000)
    m = [m for m in range(len(n))]

    # Histogram of raw data ...

    plt.bar(m, n)
    plt.title("Raw Data")
    plt.show()

    # Regular histogram ...

    plt.hist(n, bins=20)
    plt.title("Histogram")
    plt.show()

    # Histogram of cumlulative distribution ...

    plt.hist(n, cumulative=True, bins=20)
    plt.title("Cumulative Histogram")
    plt.show()

    print("--- ======================================== ... ");
    print("--- Leave TestHistogram01.main()             ... ");

# call the main method ...

main()

